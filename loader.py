import os
import yaml
from config import config
import itertools

def find_files(root_dir, filename):
    for root, dirs, files in os.walk(root_dir):
        if filename in dirs:
            file_path = os.path.join(root, filename)
            return file_path

def load_cves():
    l = []
    start_line = config['fromm'] - 1
    end_line = config['to']

    with open(config['file'], 'r') as file:
        for line in itertools.islice(file, start_line, end_line):
            l.append(line.strip("\n"))

    return l


def load_files(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

def write_files(filename, content):
    with open(filename, 'w') as file:
        return yaml.safe_dump(content,file,  default_flow_style=False)


def load_contents():
    root_dir = config['root_dir']
    target_filenames = load_cves()
    print(target_filenames)

    docker_compose_files = []
    for filename in target_filenames:
        docker_compose_files.append(find_files(root_dir, filename) + "/docker-compose.yml")

    contents = []
    for filename in docker_compose_files:
        content = load_files(filename)
        contents.append(tuple([filename, content]))

    return contents

def write_contents(contents):
    for filename, content in contents:
        write_files(filename, content)