import sys, os
import argparse as arg
from usefulFuncs import check_int
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
    selection = input()
elif not args.n:
    # no args
    # display all tools
    [print(f"{i+1}: {tool}") for i, tool in enumerate(found_tools)]
    selection = input()
else:
    selection = int(args.n)
while True:
    if check_int(selection):
        break
    else:
        print('Please enter a valid number')


# process inputs
drive  = drive[int(selection)+1].split('\n')[1:-1]
script = f'Tools/{drive[0].split(' = ')[1].strip()}'
inputs = [input(d.split(' = ')[1]) for d in drive[1:-1]]
run    = drive[-1].split(' = ')[1].split('{}')
run[0] = run[0][:7] + "Tools/" + run[0][7:]
run = ''.join([run[i]+inputs[i] for i in range(len(inputs)) if inputs[i] != ''])

# run inputs
print("="*50)
print(run)
os.system(run)