'''
Lucio
January 17, 2022
This code will make a gradebook for three students
'''
lloyd = {'name' : 'Lloyd', 'homework' : [90.0, 97.0, 75.0, 92.0], 'quizzes' : [88.0, 40.0, 94.0], 'tests' : [75.0, 90.0]}
alice = {'name' : 'Alice', 'homework' : [72.0, 91.0, 40.0, 59.0], 'quizzes' : [20.0, 75.0, 68.0], 'tests' : [80.0, 72.0]}
tyler = {'name' : 'Tyler', 'homework' : [100.0, 100.0, 95.0, 97.0], 'quizzes' : [100.0, 92.0, 99.0], 'tests' : [100.0, 80.0]}
#Creates dictionaries that say the students name, homework, quizzes, and tests

students = [lloyd, alice, tyler] #List of students

#for x in students:
    #print(x)

def average(num): #Function of how to average something out
    total = float(sum(num))
    avg = total / len(num)
    return avg

def get_avg(students): #Function that gets an average grade of one student
    hw = students['homework']
    q = students['quizzes']
    t= students['tests']
    avg = average(hw) * 0.1 + average(q) * 0.3 + average(t) * 0.6
    return avg

def letter_grade(score): #Function that gets letter grade from student or class
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
def class_avg(students): #Function that gets the average grade from the class
    results = []
    for y in students:
        results.append(get_avg(y))
    return average(results)

print("Lloyd's grade average is " + str(get_avg(lloyd))) #Prints Lloyd's grade average
print("Lloyd's letter grade is a " + str(letter_grade(get_avg(lloyd)))) #Print's Lloyd's letter grade
print("The class' grade average is " + str(class_avg(students))) #Print's the class' grade average
print("The class' letter grade is a " + str(letter_grade(class_avg(students)))) #Print's the class' letter grade