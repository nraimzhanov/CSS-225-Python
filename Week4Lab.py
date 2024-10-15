#Nurtilek Raimzhanov
#10/15/2024

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))#the year was declared with == the right was just = the input was incorrect I corrected it

if year <= 1900: #this part needed colon
    print ("Woah, that's the past!") #here I add double quotes
elif year > 1900 & year < 2020: #here was && however we need jut &
    print ("That's totally the present!")
else: #here should be  else not elif because it is the finish line
    print ("Far out, that's the future!!")
#---------------------------------------------------------------------------
# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {  # spelling mistake
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}#added curly brace

for author, date in authors.items():  # changed `author date` to `author, date` and `items{}` to `items():`
    print("%s died in %s." % (author, date))  # fixed the print statement to use parentheses and corrected the format
#-------------------------------------------------------------------------------------------------------------------
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #added 'int'

exam_three = int(input("Input exam grade three: ")) #added 'int' instead of 'str' and changed 3 to three

grades = [exam_one, exam_two, exam_three]# added commas between them
sumGrades = 0 #changes sum to sumGrade
for grade in grades: #changes grade to grades
  sumGrades += grade #chaged the logic

avg = sumGrades / len(grades)

if avg >= 90:
    letter_grade = "A"
elif 80 <=avg < 90: #simplifies the logic
    letter_grade = "B"
elif 69 < avg < 80:  #simplifies the logic
    letter_grade = "C" # added double quote
elif 65 <= avg <= 69 : #simplifies the logic
    letter_grade = "D"
else: #here should be else not elif because it is the finish line
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F": #put _ instead of -
    print("Student is failing.")# added a parenthesis
else:
    print("Student is passing.")# added a parenthesis
#-------------------------------------------------------------------------------


greeting = input("Hello, possible pirate! What's the password?") #here add double quote
if greeting in ["Array"]: #put the correct version of array
 print("Go away, pirate.")
else: #here should be else not elif because it is the finish line
 print("Greetings, hater of pirates!")
#-------------------------------------------------------------------------------

currentTimeStr = int(input("What is the current time (in hours 0-23)?"))# add int otherwise input will return a str
waitTimeStr = int(input("How many hours do you want to wait"))# add int otherwise input will return a str

currentTimeInt = int(currentTimeStr)# Changed `current_time_str` to `currentTimeStr`
waitTimeInt = int(waitTimeStr) # Changed `wait_time_str` to `waitTimeStr

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt) # Changed `finalTime_Int` to `finalTimeInt`
#-----------------------------------------------------------------------------------
str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = float(str_time)#added float because time will be more integers
wait_time = float(str_wait_time)#added float because time will be more integers

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
