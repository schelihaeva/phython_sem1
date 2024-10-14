def normalize_grades(grades) :
    valid_grades = [grade for grade in grades if grade >= 0]
    return sorted(valid_grades, reverse=True)
grades = [95, -10, 80, 90, 77]
print(normalize_grades(grades))
