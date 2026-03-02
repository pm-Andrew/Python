# demo2.py
# Andrew

# first you are going to have to install `pip install cowsay`
import cowsay
import sys

if len(sys.argv) == 2:
	cowsay.d("hello, " + sys.argv[1])
