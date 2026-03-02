# Making Faces faces.py
# Andrew S


# Defining `convert` into a function
def convert(faces):
    # String to emoji 1
    faces = faces.replace(":)", "🙂")
    # String to emoji 2
    faces = faces.replace(":(", "🙁")
    return faces


# Input from user 1
mood_input = input("end sentences with either a :), or a :(. ")
# Print the conversion
print(convert(mood_input))
