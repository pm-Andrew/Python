# try2.py

# import request

url = 'http://clark.edu' # The URL of the Clark Website

print("Program has started")

try: # try and connect to the Clark website
    r = request.get(url) # request the Clark web page using Python
    print("I have connected to the Clark website :-)")
    for i in range(10):
        print("We are connected!")
except: # if something goes wrong while trying to connect
    print("I could not connect to the Clark website :(")
    # we can't do anything since we cannot connect

print("Program has ended")
