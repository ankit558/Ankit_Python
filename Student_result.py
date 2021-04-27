import json
x = open('student.json').read()

json_object = json.loads(x)
roll_no=input("Enter Your Roll No.")
k = json_object["content"]

if not (k.get(roll_no) is None):
    y = json_object["content"][roll_no]
    name = y["name"]
    state = y["state"]
    city = y["city"]
    Class = y["Class"]
    Math = y["Math"]
    English = y["English"]
    Hindi = y["Hindi"]
    Science = y["Science"]
    Social_Science = y["Social_Science"]
    Computer = y["Computer"]
    Obtain_Marks = y["Obtain_Marks"]
    Total_percentage = y["Total_percentage"]
    Status = y["Status"]

    print(
        "Name= " + name + "\n" + "State= " + state + "\n" + "City= " + city + "\n" + "Class= " + Class + "\n" + "Math= " + Math + "\n" + "English= " + English + "\n" + "Hindi =" + Hindi + "\n" + "Science= " + Science + "\n" + "Computer= " + Computer + "\n" + "Social Science= " + Social_Science + "\n" + "Obtain_marks= " + Obtain_Marks + "\n" + "Total_marks= 100" + "\n" + "Total_percentage= " + Total_percentage + "\n" + "Status= " + Status)
else:
     print("Roll no Does not Exist"+ "\n"+" Try Again!!")
