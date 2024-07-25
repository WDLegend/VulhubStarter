import os
from loader import load_contents, write_contents
from parser import parse_arguments
from starter import change_compose_files, start_by_cve
from config import config

def init():
    path = os.path.join(config['root_dir'], "jeecg-boot/CVE-2023-4450/")
    special_one = os.path.join(path, 'docker-compose.yaml')
    print(special_one)
    if os.path.exists(special_one):
        os.rename(special_one, os.path.join(path, 'docker-compose.yml'))

if __name__ == "__main__":
    parse_arguments()
    init()
    # change all compose files.
    contents = load_contents()
    contents = change_compose_files(contents)
    write_contents(contents)
    start_by_cve(contents)

    print('done')
