
import argparse

from course import Course


def parse_args():
    parser = argparse.ArgumentParser(prog='Learning Objectives',
                                     description='Learning objective analysis',
                                     epilog='')

    parser.add_argument('-c', '--config', default="conf.txt")
    # parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def read_config(config_file_name):
    config = []
    for line in open(config_file_name):
        if line != "":
            config.append(line.strip().split(";"))
    return config


def main():

    args = parse_args()

    config = read_config(args.config)
    courses = {}
    for code, filename in config:
        assert code not in courses
        courses[code] = Course(code, filename)


if __name__ == "__main__":
    main()
