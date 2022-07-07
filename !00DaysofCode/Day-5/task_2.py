"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

    The highest score in the class is: x

Example Input

78 65 89 86 55 91 64 89
78 65 89 86 55 91 64 89

In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output

The highest score in the class is: 91
The highest score in the class is: 91

e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg
"""

heights = input("Enter the heights in comma seperated")

heights = heights.split(",")

inital_count = 0


for individual_heights in heights:
    individual_heights = int(individual_heights)
    if individual_heights > inital_count:
        inital_count = individual_heights

print(f"heighest number is {inital_count}")