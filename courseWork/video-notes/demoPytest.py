# pytest.py
# Andrew

def main():
    while True:
        au = input("AU: ")
        try:
            # au is a float
            au = float(au)
            break
        except ValueError:
            continue
    # print converted AU
    print(f"{au} AU is {convert(au)} m")

def convert(au):
    # checks if au is int or float
    if not isinstance(au, (int,float)):
        # if input is not a int or float
        raise TypeError("au must be an int or float")
    # if int ot float run convert
    return au * 149597870700

if __name__ == "__main__":
    main()
