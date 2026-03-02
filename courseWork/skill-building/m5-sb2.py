# m5-sb2.py
# Andrew


"""
Check to make sure there is either just one argument in the command line
or that there are 3 arguments

One command line argument would be the name of the file m6-sb2.py
Three commnand line arguments would the name of the file, the -f or --font and
the name of the font

VAlID COMMAND LINE
python m6-sb2.py

VALID COMMAND LINE
python m6-sb2.py -f Arial

VALID COMMAND LINE
python m6-sb2.py --font Arial

INVALID COMMAND LINE
python m6-sb2.py -f

INVALID COMMAND LINE
python m6-sb2.py --font

INVALID COMMAND LINE
python m6-sb2.py Arial

"""
import sys

if len(sys.argv) == 1:
    print("Ok, cool. No command line arguments were specified.")
elif len(sys.argv) == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    sys.exit("A font name is required")  # note use of sys.exit()
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    print(f"I received the argument of {sys.argv[2]} and the font of {sys.argv[2]}")

