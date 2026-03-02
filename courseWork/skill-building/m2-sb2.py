# Odd or even m2-sb2.py
# Andrew


# Function that checks if number is even or odd w/ if-else
def even_odd():
    x = int(input("What's x? "))
    # odd or even by modulo
    if x % 2 == 0:
        # Output for even
        print(f"{x} is Even")
        return
    # Output if odd
    else:
        print(f"{x} is Odd")
        return


# Callout results
even_odd()
# Print program end
print("[END PROGRAM]")
