#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    multiple = 5
    newGrades = []
    for i in grades:
        resto = i % multiple
        nextMultiple = (i - resto) + multiple
        if (i < 38) or (nextMultiple - i) == 3:
            newGrades.append(i)
        elif (nextMultiple - i) < 3:
            newGrades.append(nextMultiple)
        else:
            newGrades.append(i)
    return newGrades