# Module 6 Skill-Building Exercise 2
# Andrew

def main():
    # user input
    feedback = input("How was the services ")
    # calling value insie the main
    print(value(feedback))
# value() calling feedback
def value(feedback):
    # conditional finding keywords
    # if "excellent" is lower cased in sentence
    if "excellent" in feedback.lower().strip():
        return "Thank you for an excellent rating"
    # if "good" is lower cased in sentence
    elif "good" in feedback.lower().strip():
        return "Thank you for that good rating"
    # other values
    else:
        return "All feedback is good feedback"

if __name__ == "__main__":
    main()
