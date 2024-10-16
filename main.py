#Pyhton project
name = ""
st_enter = ""
while((name.lower() != "exit") and (st_enter.lower() != "exit") ):
    name = input("Enter your name: ")
    st_enter = input("Are you a student(yes/no)")
    is_student = False

    if st_enter == "yes":
        is_student = True

    if is_student == True:
        print("Welcome to the class")
