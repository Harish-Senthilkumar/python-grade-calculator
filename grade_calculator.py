def calculate_average(list_of_grades):
    #add all scores using sum()
    total = sum(list_of_grades)
    #count the number of scores using len()
    count = len(list_of_grades)
    #divide the total by the count to get the average
    average = total /count
    return average

print("Welcome to the Grade Calculator")

scores = []

#After the empty list, asking the user #of enterable grades: and store the answer in a variable
grade_count = int(input("How many assignment grades do you want to enter? "))

#asking the user to enter scores one at a time and store each score in the list using a for loop that runs for the number of grades specified by the user. Inside the loop, convert the input to a float and append it to the scores list.
for i in range(grade_count):
    grade = float(input(f"Enter score #{i + 1}: "))
    scores.append(grade) #appending each user score to the empty list called scores

#calling the average function with the updated scores list
average_score = calculate_average(scores)

#printing the scores entered by the user
print("The scores you entered are:")
for score in scores:
    print(score)
print()

#Final formatting and layout of grade stats
print(" -- Calculating Summary Statistics --")
print()
print(f"The average score is: {average_score}")
print()
print(f"The highest score is: {max(scores)}")
print(f"The lowest score is: {min(scores)}")
print()
print(" -- End of Summary Statistics --")

#check if the student passed or not

if average_score >=70:
    print("Congratulations! You passed the course.")
else:
    print("Did not pass the course. Better luck next time.")

