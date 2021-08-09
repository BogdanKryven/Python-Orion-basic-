import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file", help="Please write path to file")
parser.add_argument("--write", help="You can write something to file")
args = parser.parse_args()

if args.write:
    f = open(args.file, 'w')
    f.write(args.write)
else:
    f = open(args.file, 'r')
    print(f.readline())
f.close()