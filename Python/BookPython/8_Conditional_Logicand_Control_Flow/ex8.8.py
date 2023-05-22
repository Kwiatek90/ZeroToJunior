#Suppose you flip a fair coin repeatedly until it lands on both heads
#and tails at least once each. In other words, after the first flip, you
#continue to flip the coin until it lands on something different.
#Doing this generates a sequence of heads and tails. For example, the
#first time you do this experiment, the sequence might be heads, heads,
#then tails.
#On average, how many flips are needed for the sequence to contain
#both heads and tails?
#Write a simulation that runs 10,000 trials of the experiment and
#prints the average number of flips per trial
#head orzeł
#trails - reszka

#notatki moje

import random


def coin_flip():
    flip = random.randint(0,1)
    if flip == 1:
        return "head"
    else:
        return "trail"
    
flips = 0
for trail in range(10_000):
    first_flip = coin_flip()
    flips += 1
    
    while first_flip == coin_flip():
        flips += 1
    
    flips = flips + 1
    
avg_flips_per_trial = flips / 10_000
print(f"The average number of flips per trial is {avg_flips_per_trial}.")
    
