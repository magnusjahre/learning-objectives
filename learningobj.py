
import pandas as pd
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
                prog='Learning Objectives',
                description='Learning objective analysis',
                epilog='')

    parser.add_argument('filename')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag

    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)


def main():

    parse_args()

    FILENAME = "tdt4255-laeringsmaal.xlsx"

    df = pd.read_excel(FILENAME)

    print(df)


if __name__ == "__main__":
    main()
