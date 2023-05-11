#Write a script called translate.py that asks the user for some input
#with the following prompt: Enter some text:. Then use the .replace()
#method to convert the text entered by the user into “leetspeak” by making the following changes to lower-case letters:
#• The letter a becomes 4
#• The letter b becomes 8
#• The letter e becomes 3
#• The letter l becomes 1
#• The letter o becomes 0
#• The letter s becomes 5
#• The letter t becomes 7
#Your program should then display the resulting string as output. Below is a sample run of the program:
#Enter some text: I like to eat eggs and spam.
#I 1ik3 70 347 3gg5 4nd 5p4m.

text = input("Enter some text: ")
new_text = text.replace("a", "4").replace("b","8").replace("e","3").replace("l","1").replace("o","0").replace("s","5").replace("t","7")
print(new_text)

