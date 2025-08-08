student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# function for returning the class grade
def scores_calc(scores, grades):
    for name, score in student_scores.items():
        if (score >= 91) & (score <= 100):
            student_grades[name] = "Outstanding"
        elif (score >= 81) & (score <= 90):
            student_grades[name] = "Exceeds Expectations"
        elif (score >= 71) & (score <= 80):
            student_grades[name] = "Acceptable"
        elif (score <= 70):
            student_grades[name] = "Fail"
    
    print(student_grades)

# created empty dictionary
student_grades = {}
# calling the function
scores_calc(student_scores, student_grades)