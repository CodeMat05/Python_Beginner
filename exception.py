class Student:
    age = 0

def compute_av(student_count = 0, s:Student = None):
    try:
        s.age = 0
        sum_funds = 500
        average_stud_funds = sum_funds / student_count
        return average_stud_funds
    except ZeroDivisionError as error:
        print("Invalid student count", error)
    except:
        print("Something Went wrong")

compute_av(0)