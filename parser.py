import argparse
from config import config
import os

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start-port',  default=config['start_port'], type=int)
    parser.add_argument('-r', '--root-dir', required=True, type=str)
    parser.add_argument('-f', '--fromm', required=True, type=int)
    parser.add_argument('-t', '--to', required=True, type=int)
    parser.add_argument('-c', '--force-recreate', type=bool, default=config['force_recreate'])
    parser.add_argument('-x', '--file', default=config['file'] ,type=str)

    args = parser.parse_args()

    if args.fromm <= 0:
        print('Invalid')
        exit()

    if args.fromm > args.to:
        print('Invalid')
        exit()

    args.root_dir = os.path.abspath(args.root_dir)

    config.update(vars(args))
    return config

# 示例调用
if __name__ == "__main__":
    config = parse_arguments()
    print(config)