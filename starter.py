from config import config
import subprocess
import sys
import os

def change_compose_files(contents):
    start_port = config['start_port']
    # print(contents)
    for content in contents:
        service = content[1]['services']
        for value in service.values():
            # print(value)
            if 'ports' in value.keys():
                tmp = start_port
                port_list = []
                for port in value['ports']:
                    data = str(port).split(':')
                    data[0] = str(tmp)
                    changed = data[0] + ":" + data[1]
                    port_list.append(changed)

                    tmp += 1
                value['ports'] = port_list
                start_port += 10

    return contents

def run_docker_compose(recreate):
    command = ["docker-compose", "up", "-d"]

    if recreate:
        command.append('--force-recreate')

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 实时输出命令的输出
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            sys.stdout.write(output)
            sys.stdout.flush()

    # 打印stderr中的内容
    stderr_output = process.communicate()[1]
    if stderr_output:
        sys.stderr.write(stderr_output)
        sys.stderr.flush()

def start_by_cve(contents):
    # run docker-compose up -d
    for i in range(0, config['to'] - config['fromm'] + 1):
        content = contents[i]
        directory = os.path.dirname(content[0].strip('docker-compose.yml'))
        os.chdir(directory)
        run_docker_compose(False)

