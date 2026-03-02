distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft]) # accessing library's converts str to float
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float") # If there is a problem converting
        return # we aren't converting anything

    m = convert(au)
    print(f"{m} m away")


def convert(au):
    return au * 149597870700


main()
