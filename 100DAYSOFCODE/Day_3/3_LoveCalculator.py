"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



digit1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e")

digit2 = name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")

love_score = digit1 + digit2

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")