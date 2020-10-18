answer = (input('Which type of average would you like to calculate? (Enter "1" for arythmetic average or "2" for weight average): '))
if answer != "1" and answer != "2":
    print("Input error! Try again!")
else:
    number_of_grades = int(input("Enter the number of grades: "))
    grades = ()
    weights = ()
    sum_of_grades = 0
    sum_of_weights = 0
    pointer = 0
    average = 0

    if answer == "2":
        for i in range(1, number_of_grades+1):
            grade = float(input("Enter grade: "))
            list_of_grades = list(grades)
            list_of_grades.append(grade)
            grades = tuple(list_of_grades)
            weight = int(input("Enter grade's weight: "))
            list_of_weights = list(weights)
            list_of_weights.append(weight)
            weights = tuple(list_of_weights)
        for i in grades:
            o = weights[pointer]
            sum_of_grades += i * o
            pointer += 1 
        for i in weights:
            sum_of_weights += i
        if sum_of_weights <= 0:
            print("Wrong sum of the weights. No answer displayed.")
        else:
            average = sum_of_grades/sum_of_weights
    elif answer == "1":
        for i in range(1, number_of_grades+1):
            grade = float(input("Enter grade: "))
            list_of_grades = list(grades)
            list_of_grades.append(grade)
            grades = tuple(list_of_grades)
        for i in grades:
            sum_of_grades += i
        average = sum_of_grades/number_of_grades
    print("Your average is: ", average)