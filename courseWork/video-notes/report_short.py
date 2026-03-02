# report_short.py
# Andrew


def main():
    # creating a dictionary with
    spacecraft = {"name": "James Webb Space Telescope"}
    # add data via update
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    # creating a idk yet but you can input values via this return
    return f"""
    ========== REPORT ========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Uknown")}

    =========================
    """

main()
