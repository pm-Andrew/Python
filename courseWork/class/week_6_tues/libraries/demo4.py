# demo4.py
# Andrew

# import sys

# print(sys.argv)

# print(f"Hello, {name}")

# ------------
# import sys

# first_name = sys.argv[1]
# last_name = sys.argv[2]

# print(f"Hello, {first_name} {last_name}")

# -----
import sys

if len(sys.argv) == 3:
    first_name = sys.argv[1]
    last_name = sys.argv[2]

print(f"Hello, {first_name} {last_name}")
