# water_short.py
# Andrew

# for soil import sample - this is an outside program

def main():
    moisture = 28
    days = 0
    print(f"Days {days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = 28
        print(f"Moisture is {moisture}%")
        # This break is to prevent
        break

    print("Time to water!")



main()

