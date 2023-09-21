#enter student fullname, id#, course, section
name = input("enter fullname: ")
identificationNumber = input("enter i.d no.: ")
course = input("enter course: ")
section = input("enter section: ")

#enter first quarter grade to fourth quarter grade
FirstQuarterGrade = int(input("enter first quarter grade: "))
SecondQuarterGrade = int(input("enter second quarter grade: "))
ThirdQuarterGrade = int(input("enter third quarter grade: "))
FourthQuarterGrade = int(input("enter fourth quarter grade: "))

print("fullname:",name)
print(" i.d no.:", identificationNumber)
print (" course: ", course)
print (" section: ", section)

print("first quarter grade:", int(FirstQuarterGrade))
print("second quarter grade:", SecondQuarterGrade)
print("third quarter grade:", ThirdQuarterGrade)
print("fourth quarter grade:", FourthQuarterGrade)
#compute the average grade from first quarter to fourth quarter
avg = FirstQuarterGrade + SecondQuarterGrade + ThirdQuarterGrade + FourthQuarterGrade / 4
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")

print("fullname:",name)
print(" i.d no.:", identificationNumber)
print (" course: ", course)
print (" section: ", section)

#If grade is greater than 90 grade A is printed
#If grade is between 80 and 90 grade B is printed
#if grade is between 70 and 80 grade C is printed
#if grade is between 60 and 70 grade D is printed
#if grade is below 60 then grade F is printed


