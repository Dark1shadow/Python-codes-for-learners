marks1= int(input("The marks obtainted by the student in first subject"))
marks2=  int(input("The marks obtainted by the student in second subject"))
marks3= int(input("The marks obtainted by the student in third subject"))
if(marks1<33 or marks2<33 or marks3<33):
    print("You are failed because of low marks in each subject")
if(marks1+marks2+marks3)/3<40:
    print("You are failed because of low percentage")
else:
    print("You have passed the exam")