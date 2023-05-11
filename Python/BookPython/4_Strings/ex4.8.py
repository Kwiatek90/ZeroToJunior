#1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1.
text = "AAA"
test = text.find("a")
print(test)

#2. Replace every occurrence of the character "s" with "x" in the string
#"Somebody said something to Samantha.".
text1 = "Somebody said something to Samantha"
new_tex1 = text1.replace("s","x")
print(new_tex1)


#3. Write and test a script that accepts user input using the input()
#function and displays the result of trying to .find() a particular
#letter in that input

text2 = input("Give me a word: ")
letter = input("Which letter you want to find in your word: ")
result = text2.find(letter)
print(f"Your letter is on {result} postion in word, but first letter starts with 0 postion")