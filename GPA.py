def calculate_gpa():
    print("Welcome to the CGPA Calculator!")
    
    num_subjects = int(input("Enter the number of subjects: "))
    total_credits = 0
    total_grade_points = 0
    
    for i in range(1, num_subjects + 1):
        print(f"\nSubject {i}:")
        credits = int(input("Enter the credit hours: "))
        grade_point = float(input("Enter the grade point "))
       
        
        
        total_credits += credits
        total_grade_points += grade_point * credits
    
    
    if total_credits == 0:
        print("Total credits cannot be zero!")
        return
    
    cgpa = total_grade_points / total_credits
    print(f"\nYour CGPA is: {cgpa:.2f}")
    
calculate_gpa()