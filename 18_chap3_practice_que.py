#Question no.1 solution
name = input("Enter your name")
print("Good afternoon:\n" + name)
# Question no.2 solution
letter = '''Dear </name>
Congrautations on your visa approval!!!!!!!!!!
Most gratefully i want to inform about your selection in our college.
I hope you will be a sencire and obedient student at our college during your college hours.
Date:<|date|> '''
name = input("Enter your name\n")
date = input("Enter the date\n")
letter =letter.replace("</name>", name )
letter = letter.replace("<|date|>", date)
print(letter)