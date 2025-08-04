import sys, os
import argparse as arg
from usefulFuncs.py import check_int
import argcomplete

parser = arg.ArgumentParser()
parser.add_argument('-m')
parser.add_argument('-n')
argcomplete.autocomplete(parser)
args = parser.parse_args()

found_tools = os.listdir('Tools')
driver = open('driver.txt')
drive = driver.read()
driver.close()

drive = drive.split('='*50)

if args.m:
    # -m
    # filter through tools based on words in name of tool
    [print(f"{i+1}: {tool}") for i, tool in enumerate(found_tools) if args.m.lower() in tool.lower()]
elif args.n:
    # -n
    # filter through tools based on the number of the tool
    print(os.listdir(args.n))
else:
    # no args
    # display all tools
    [print(f"{i+1}: {tool}") for i, tool in enumerate(found_tools)]

selection = input()
while True:
    if check_int(selection):
        break
    else:
        print('Please enter a valid number')

drive = drive[int(selection)+1].split('\n')[1:-1]
script = f'Tools/{drive[0].split(' = ')[1].strip()}'
inputs = [input.split(' = ')[1].strip() for input in drive[1:-1]]
run = drive[-1].split(' = ')[1].split('{}')
run = ''.join([run[i]+inputs[i] for i in range(len(inputs))])
print(f"")