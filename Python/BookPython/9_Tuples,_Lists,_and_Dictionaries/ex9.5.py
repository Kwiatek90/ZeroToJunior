#In this challenge, you’ll write a program that generates poetry.

#Create five lists for different word types:

#• Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango",
#"extrovert", "gorilla"]
#• Verbs: ["kicks", "jingles", "bounces", "slurps", "meows",
#"explodes", "curdles"]
#• Adjectives: ["furry", "balding", "incredulous", "fragrant",
#"exuberant", "glistening"]
#• Prepositions: ["against", "after", "into", "beneath", "upon",
#"for", "in", "like", "over", "within"]
#• Adverbs: ["curiously", "extravagantly", "tantalizingly",
#"furiously", "sensuously"

#Randomly select the following number of elements from each list:
#• 3 nouns
#• 3 verbs
#• 3 adjectives
#• 2 prepositions
#• 1 adverb

#You can do this with the choice() function in the random module. This#
#function takes a list as input and returns a randomly selected element
#of the list.

#For example, here’s how you use random.choice() to get random element from the list ["a", "b", "c"]:

#import random
#random_element = random.choice(["a", "b", "c"])

#Using the randomly selected words, generate and display a poem with
#the following structure inspired by Clifford Pickover:

#{A/An} {adj1} {noun1}

#{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
#{adverb1}, the {noun1} {verb2}
#the {noun2} {verb3} {prep2} a {adj3} {noun3}

#Here, adj stands for adjective and prep for preposition.

#Here’s an example of the kind of poem your program might generate:

#A furry horse

#A furry horse curdles within the fragrant mango
#extravagantly, the horse slurps
#the mango meows beneath a balding extrovert

#Every time your program runs, it should generate a new poem.

nouns =  ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

adjectivies = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    
import random

noun1 = random.choice(nouns)
noun2 = random.choice(nouns)
noun3 = random.choice(nouns)

verb1 = random.choice(verbs)
verb2 = random.choice(verbs)
verb3 = random.choice(verbs)

adj1 = random.choice(adjectivies)
adj2 = random.choice(adjectivies)
adj3 = random.choice(adjectivies)

prep1 = random.choice(prepositions)
prep2 = random.choice(prepositions)

adverb1 =  random.choice(adverbs)



print(f"""
    A {adj1} {noun1} 
    A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adverb1}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} a {adj3} {noun3}
    """)