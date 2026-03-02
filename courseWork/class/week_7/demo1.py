# demo1.py
# Andrew

# python demo1.py cheese 5

import sys

if len(sys.argv) == 3:
    if sys.argv[1] not in ['cheese', 'plain']:
        sys.exit("Please specify a vaild type of pizza")
    if int(sys.argv[2]) < 1:
        sys.exit("Please enter a vaild quantity")
else:
    sys.exit("Please include the type of pizza and qty")

print("we have recieved your order")
