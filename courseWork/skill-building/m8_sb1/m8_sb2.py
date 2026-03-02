# m8_sb2.py
# Andrew


"""
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
<iframe></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay;clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
"""

import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    result = re.search(r'src\s*=\s*"(.+?)"', s)
    if result != None:
        result = result.group()
        result = result.split("=")

        if "youtube.com" in result[1]:
            result = result[1].replace("youtube.com/embed", "youtube.be")
            return result
        else:
            return None

if __name__ == "__main__":
    main()
