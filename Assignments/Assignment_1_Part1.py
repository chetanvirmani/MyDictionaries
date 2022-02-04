
courseRoom = {"CS101":"3004",
    "CS102":"4501",
    "CS103":"6755",
    "NT110":"1244",
    "CM241":"1411"}

courseInstructor = {"CS101":"Haynes",
    "CS102":"Alvarado",
    "CS103":"Rich",
    "NT110":"Burke",
    "CM241":"Lee"}

courseTime = {"CS101":"8:00 a.m.",
    "CS102":"9:00 a.m.",
    "CS103":"10:00 a.m.",
    "NT110":"11:00 a.m.",
    "CM241":"1:00 p.m."}

courseNumber = input ("Please enter a course number to get course details: ")

while courseNumber.upper() != "N":

    if courseNumber.upper() in courseTime:

        print ("Course Number:",courseNumber.upper())
        print ("Room:",courseRoom[courseNumber.upper()])
        print ("Instructor:",courseInstructor[courseNumber.upper()])
        print ("Meeting Time:",courseTime[courseNumber.upper()])

    else:
        print("Course not found.")

    courseNumber = input("Enter the course number to search again or enter 'n' to exit: ")



