import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--hell', help="Add hell option")
args = parser.parse_args()
print(args.hell)