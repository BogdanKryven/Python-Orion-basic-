import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Your user username")
parser.add_argument("--first_name", help="Your user first name")
parser.add_argument("--last_name", help="Your user last name")
args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username

if args.first_name:
    user_dict['first_name'] = args.first_name

if args.last_name:
    user_dict['last_name'] = args.last_name

user_file = open('users.json', 'r')
users_data = json.loads(user_file.readline())
user_file.close()

users_data.append(user_dict)

user_file = open('users.json', 'w')
user_file.write(json.dumps(users_data))
user_file.close()
