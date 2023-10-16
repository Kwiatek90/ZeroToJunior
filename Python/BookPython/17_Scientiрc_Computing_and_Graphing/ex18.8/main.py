#For this challenge, you’ll write a GUI application for generating poetry.
#This application is based off the poem generator from Chapter 9.
import tkinter as tk
import random
from tkinter.filedialog import asksaveasfilename

#programmer, laptop, code
#typed, napped, cheered
#greet, smelly, robust
#to, from, on, like
#gracefully


def generate_poem():
    nouns = split_words(ent_nouns)
    verbs = split_words(ent_verbs)
    adjectives = split_words(ent_adjectives)
    prepositions = split_words(ent_prepositions)
    adverbs = split_words(ent_adverbs)

    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)

    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)

    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)

    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)

    adverb1 =  random.choice(adverbs)
    
    poem = "Your poem\n\n" + adj1 + noun1 + "\n\nA " + adj1 + noun1 + verb1 + prep1 + " the " + adj2 + noun2 + "\n" + adverb1 + ", the " + noun1 + verb2 + "\nthe " + noun2 + verb3 + prep2 + " a " + adj3 + noun3
    lbl_poem["text"] = poem


def split_words(entry_words):
    words = entry_words.get()
    words_splited = words.split(",")
    return words_splited

def check_poem():
    if len(split_words(ent_nouns)) < 3 or len(split_words(ent_verbs)) < 3 or len(split_words(ent_adjectives)) < 3 or len(split_words(ent_prepositions)) < 3 or len(split_words(ent_adverbs)) < 1:
        lbl_poem["text"] = "You Didn't Enter Enough Words"
    else:
        generate_poem()
        
        
def save_to_file():
    filepath = asksaveasfilename( defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text_to_save = lbl_poem["text"]
        output_file.write(text_to_save)
    
        window.title(f"Poem to save")

window = tk.Tk()
window.rowconfigure([0,1,2], minsize=50, weight=0)
window.columnconfigure(0, minsize=600, weight=1)
window.rowconfigure(3, minsize=100, weight=1)

#first text
lbl_text = tk.Label(master=window, text="Enter your favourite word, separated by commas.")
lbl_text.grid(row=0, column=0)

#words
frm_words = tk.Frame(master=window)
frm_words.grid(row=1, column=0)

lbl_nouns = tk.Label(master=frm_words, text="Nouns:")
ent_nouns = tk.Entry(master=frm_words, width=85)
lbl_nouns.grid(row=0, column=0, sticky="e")
ent_nouns.grid(row=0, column=1)

lbl_verbs = tk.Label(master=frm_words, text="Verbs:")
ent_verbs = tk.Entry(master=frm_words, width=85)
lbl_verbs.grid(row=1, column=0, sticky="e")
ent_verbs.grid(row=1, column=1)

lbl_adjectives = tk.Label(master=frm_words, text="Adjectives:")
ent_adjectives = tk.Entry(master=frm_words, width=85)
lbl_adjectives.grid(row=2, column=0, sticky="e")
ent_adjectives.grid(row=2, column=1)

lbl_prepositions = tk.Label(master=frm_words, text="Prepositions:")
ent_prepositions = tk.Entry(master=frm_words, width=85)
lbl_prepositions.grid(row=3, column=0, sticky="e")
ent_prepositions.grid(row=3, column=1)

lbl_adverbs = tk.Label(master=frm_words, text="Adverbs:")
ent_adverbs = tk.Entry(master=frm_words, width=85)
lbl_adverbs.grid(row=4, column=0, sticky="e")
ent_adverbs.grid(row=4, column=1)

#button
btn_generate = tk.Button(master=window, text="Generate", command=generate_poem)
btn_generate.grid(row=2, column=0)

#generated text
frm_poem = tk.Frame(window, relief=tk.GROOVE, borderwidth=4)
frm_poem.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
frm_poem.columnconfigure(0, weight=1)
frm_poem.rowconfigure(1, weight=1)

lbl_poem = tk.Label(master=frm_poem, text="Your poem")
lbl_poem.grid(row=0, column=0)

btn_save = tk.Button(master=frm_poem, text="Save to File", command=save_to_file)
btn_save.grid(row=1, column=0, padx=10, pady=10, sticky="s")

window.mainloop()




