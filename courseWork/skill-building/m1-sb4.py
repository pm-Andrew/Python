#Module 1 Skill Building Ex.4
#Andrew Sabourin


#Ask a user to input a sentence. The input should convert the input to lowercase.
sentence = input("Provide a short sentence, about animals.")
# The program should then replace any occurrence of the letter e with the emoji 🌎
sentence = sentence.replace("e", "🌎")
# The program should then replace any occurrence of the letter z with the emoji 🦓
sentence = sentence.replace("z", "🦓")
#Print the sentence with the replaced values
print(sentence)
#Test 1 - Input: "The zoo has a lot of zebras" Output: "th🌎 🦓oo has a lot of 🦓🌎bras"
#Test 2 - Input: "Zoom is a very useful tool" Output: "🦓oom is a v🌎ry us🌎ful tool"
