Andrew Sabourin
CTEC 121 - Intro to Programming - Final Project
## 48 Laws of Power Learning Program
#### Video Demo:  [loom video](https://www.loom.com/share/2b3791308ad44958b522b6caf0222c08?sid=73c41c8d-eb07-46b0-93d4-f6d9f81e01f5)

#### Description:
The 48 Laws of Power Learning Program, is a program that summarizes Robert Greens National Best Seller *"The 48 Laws of Power."* This book highlights psychology, history and the figures that used this law to rise to the top.

#### Usage
- Start up program.
- Valid values are inputted (1-48) or an empty string
- Then choose either the summary of the law or a historical figure.
- Pressing enter at the beginning of the program prints random law then exits program.
**Valid Input**
```
final-project/ $ python project.py
Welcome!
This program Summarizes The 48 Laws of Power
------
What Law would you like to learn? 45

        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Law: 45. Preach the Need for Change but Never Reform Too Much at Once
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
```

**Invalid**
```
What Law would you like to learn? 49
What Law would you like to learn? 50
What Law would you like to learn? 51
What Law would you like to learn? cat
What Law would you like to learn? dog
```
**Random**
```
Welcome!
This program Summarizes The 48 Laws of Power
------
What Law would you like to learn?
{'number': '37', 'law': '37. Create Compelling Spectacles', 'summary': 'Dramatic visuals captivate.', 'figure': 'Leni Riefenstahl'}
```
#### Functionality:
The function of this program is to briefly summarize the book *"The 48 Laws of Power,"* by inputting a number that is correlated to one of the laws, which then returns a law, if no law is entered a random law dictionary is returned and the program ends. A valid number entered displays the law, and then prompts if the user wants to display a short summary of the law or a historical person that is tied to the law. Valid input displays the either the summary or historical figure, yet the option to display both is hidden if a user presses enter/ return.

>[!note]
>The program is a rough draft for the CS50 final project, the fact the program is working the way I want it to work, is exciting. I know there is more I can do to improve so this program will be used as CTEC 121 - Final Project, for now.
>

---
### Under the Hood
##### CSV.file
This program uses a CSV file that has is in the format `number,"law","summary","figure"`, while law, summary, and figure are strings number is an integer, for ease of comparing.
```
number,law,summary,figure
1, "Never Outshine the Master", "Make those above you feel superior.", "King Louis XIV"
```

The CSV houses most of the information of the laws which has each law in row with the summaries and figures related to them.
This file named `48_laws.csv` is then imported to the Python File via `import csv` and the functions that come with the CSV package, which includes how the file is then read into by the Python file. `DictReader` is used to read `48_laws.csv` inside the `main()`. The laws are then stored in a empty dictionary called `all_laws`

##### main()
Under the `DictReader` logic, a indefinite loop is used to gather and verify user input, with then the main simple decision structure that displays either `summary` or `figure` from `48_laws.csv`.

The `while True` is where the program asks for user input, it then tries to strip any whitespace which is then stored in the variable `user_law` and used as an argument to `is_law` to verify `user_law` matches the data in `48_laws.csv` stored in `all_laws`. If returned true, the law is printed out, and moves on to the main conditional part of the program.
```
What Law would you like to learn? 45
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Law: 45. Preach the Need for Change but Never Reform Too Much at Once
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
```
If `user_law` is invalid the program continues to prompt, until valid, also there is another function named `random_law` which uses `random.choice()` from the `random` package. Which pulls random laws from `48_law.csv` if the `user_law` has no input or user press the enter/ return button. The `sys` package comes into play to exit the program if this happens.

>[!note]
>The reason for the `random_law` is purely Easter Egg type hinting.

With valid values entered into `user_law`, it is stored with `all_laws` in another variable called `law` which is then goes through a bool condition. If True this progress to the next step of the program, a simple decision structure that validates a multi-way decision structure located in the function `lawFork.` Here `law` is still storing the `user_law` and seeing if the user wants either the `summary` or `figure` from the law they choose. If an invalid value is inputted a hint message is displayed, telling the user how to input the next time.

##### is_law()
`is_law` takes `user_law` and `all_laws` as arguments and iterates though the list provided from the `main()` to see if the value entered into `user_law` matches one of the rows in `all_laws`. If true the matching row is sent back to the `main()`, if false the prompt for a number between 1-48 continues until true or enter/ return is the value. The row will be stored to be used in `lawFork()`.
##### lawFork()
If valid, the `row` variable  in which the `dict` is stored in the variable `law` in the `main()` along with  the variable `figSum`. `figSum` is an input that is asking the user wether they want two decisions, summary or figure, once though they enter an invalid value, they discover the error message is a hint to what can be entered.
The function `lawFork()` when either of it's six valid values entered are related to the list of  dictionaries now in `law`, which is storing the matched list of dictionaries called by `user_law`, `lawFork` outputs the `summary` and `figure` dictionaries, or both, then ends the program.
###### Examples
**Summary**
```
Would you like to a short summary or a historical figure? (summary or figure): summary
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Summary: Gradual change prevents resistance.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
```
**Figure**
```
Would you like to a short summary or a historical figure? (summary or figure): figure
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Figure: Franklin D. Roosevelt
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
```
**Invalid**
```
Would you like to a short summary or a historical figure? (summary or figure):

        ~~~~~~Hints~~~~~~~
        |- summary OR sum |
        |- figure OR fig |
        |- sum and fig OR both |
        ~~~~~~~~~~~~~~~~~~~~~
```
##### random_law()
As mentioned before `random_law()` is a function that outputs a random law from `all_laws` dictionary. In the `main()` inside the in the `while True`, if the value the user enters a empty string by pressing enter/ return, the `random.choice()` library is used to pull a random row from `all_laws` then return back to the `main()` as the variable `law`, which is then used as a `sys.exit()` message ending the program.

##### Acknowledgments
- Inspired by The 48 Laws of Power by Robert Greene.
- Developed as a CS50 final project and for CTEC 121.
