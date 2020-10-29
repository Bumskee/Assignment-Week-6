#assigning dictionaries that contain the keys and values of the students information
eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

#assigning a dictionary that contains the information regarding the weighting values of the scores
weights = {
"homework": 10,
"quizzes": 30,
"tests": 60
}

#assigning a list with values that will be referred later
students = [eren, mikasa, armin]

#A loop that will go through all the data in the student information and then printing it on the console
for student in students:
    print("\nStudents Data:")
    for data in student:
        print(data, "=", str(student.get(data)))

#A function that will take a sequence of numbers and calculate it's average
def average(numbers):
    '''This function will take a sequence of number,
    calculate the sum of all of the elements inside it,
    divides the sum with the amount of elements inside the sequence,
    and then returning the result'''
    total = float(sum(numbers))
    result = float(total / len(numbers))
    return result

#A function that will take a dictionary and then process the data in that dictionary
def get_average(student):
    '''This function will take the average of the element of the keys in the dictionary and then assign them in their respective variables
    then it will average all of weighted averages inside another variable. Then it will return the variable.'''
    homework = average(student.get("homework"))
    quizzes = average(student.get("quizzes"))
    tests = average(student.get("tests"))
    grade = float((homework * weights.get("homework") / 100) + (quizzes * weights.get("quizzes") / 100) + (tests * weights.get("tests") / 100))
    return grade

#A function that compares the result of the get_average function
def get_letter_grade(score):
    '''This will return either A, B, C, D, E, F depending if the score is
    above 90, above 80, above 70, above 60, or under 60 respectively'''
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#A function that is going to incorporate all the functions above and get result of the average grade of the students
def get_class_average(students):
    '''This function will insert the weighted average on a variable called results.
    Then it will use the average() function to take the average of the results variable and assign it to the result variable
    Finally it will then return the result value'''
    results = []
    for student in students:
        results.append(get_average(student))
    result = average(results)
    return result

#prints the class's average score and grade
print("\n" + "The class's average score is", str(get_class_average(students)))
print("The class's average grade is", get_letter_grade(get_class_average(students)))