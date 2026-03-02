# File Extensions extensions.py
# Andrew

"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix, output
application/octet-stream instead, which is a standard default.
You also need to ensure no spaces at the beginning or end of a user's input.
"""




def main():
    # ask user for file name
    file = input("File Name: ").strip().lower()
    # run if-else to determine results based on extension type print the media type
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
