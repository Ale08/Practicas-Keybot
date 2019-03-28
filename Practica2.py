
def final_grade(exam, projects):
	if exam >= 90 or projects > 10:
		finalGrade = 100
	elif exam > 75 and projects >= 5:
		finalGrade = 90
	elif exam > 50 and projects >= 2: 
		finalGrade = 75
	else:
		finalGrade = 0

	return finalGrade