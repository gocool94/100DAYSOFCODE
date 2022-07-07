"""
Instructions

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
Example Input

156 178 165 171 187
156 178 165 171 187

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output

171
171

e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP
Hint

    Remember to use the round() function to round the average height before you print it.


"""

heights = input("Enter the heights in comma seperated")

heights = heights.split(",")

sum = 0
count = 0

for individual_heights in heights:
    individual_heights = int(individual_heights)
    sum += individual_heights
    count+=1

print(f"Average height is {sum/count}")