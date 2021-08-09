import sys

try:
    if sys.argv[1] == 'rain':
        if sys.argv[2] == 'wind':
            print('Візьми парасольку і курточку')
        else:
            print('Візьми парасольку')
    elif sys.argv[1] == 'sunny':
        print('Ти ще тут ? Бери плавки і в басєйнік')
    else:
        print("Please provide a valid arument")
except IndexError:
    print("Error: please provide an argument")