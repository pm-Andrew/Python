# watch.py
# Andrew

# import regex library
import re


def main():
    # asks for input &  prints results of parse()
    print(parse(input("HTML: ")))


def parse(s):
    # parse the YouTube URL s is HTML str
    # using search to locate src="..." in s and capture the expression in ""
    # then return the match
    result = re.search(r'src=\s*\"(.+)\"', s)

    # result is valid
    if result != None:
        # group extracting the match
        result = result.group()
        # split the HTML at "="
        result = result.split("=")

        if "youtube.com" in result[1]:
            # replace and shorten the URL
            result = result[1].replace(
                "youtube.com/embed", "youtu.be").replace("www.", "").strip('"')
            # replaces any http:// to https://
            result = result.replace("http://", "https://")
            # returns the valid results
            return result
        else:
            # returns None if not valid
            return None


if __name__ == "__main__":
    main()
