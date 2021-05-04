import json

class Student:

#Append_Method
    def writingFile(self,rno, name, city, state, classs, math, english, hindi, science, computer, social_Science,
                    obtain_marks, percentage, status):
        content = {
            "roll_no": rno,
            "name": name,
            "city": city,
            "state": state,
            "Class": classs,
            "Math": math,
            "English": english,
            "Hindi": hindi,
            "Science": science,
            "Computer": computer,
            "Social_Science": social_Science,
            "Obtain_Marks": obtain_marks,
            "Total_percentage": percentage,
            "Status": status
        }
        def write_json(data, filename='student2.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        with open('student2.json') as json_file:
            data = json.load(json_file)
            temp = data['content']
            y = content
            temp.append(y)
            write_json(data)

# Reading_Method..
    def readFile(self, rno):
        x = open('student2.json').read()
        json_object = json.loads(x)
        z = 0
        for i in json_object["content"]:
            if (i["roll_no"] == rno):
                print(i)
                z=1
        if z==0:
            print("Roll number does not Exists...")

    # Deleting_File

    def deleteFile(self):
        R_no = 0
        R_no = input("Enter Roll no to Delete Data")
        obj = json.load(open('student2.json'))
        for i in range(len(obj["content"])):
            if obj["content"][i]["roll_no"] == R_no:
                obj["content"].pop(i)
                print("Data Deleted at Roll no " + R_no)
                break
        open("student2.json", "w").write(
            json.dumps(obj, indent=4)
        )

#Update_data
    def showopt(self):
        print("Select Options to Edit Data")
        print("Select 1 For Name")
        print("Select 2 For City")
        print("Select 3 For State")
        print("Select 4 For Class")
        print("Select 5 For Math")
        print("Select 6 For English")
        print("Select 7 For Hindi")
        print("Select 8 For Science")
        print("Select 9 For Computer")
        print("Select 10 For Social Science")

    def editFile(self):
        stss=Student()
        stss.showopt()
        ychoice=input("Enter your Choice?")

        if int(ychoice)==1:
            print("1")
            stss.updatedata("name")
        elif int(ychoice)==2:
            print("2")
            stss.updatedata("city")
        elif int(ychoice) == 3:
            print("3")
            stss.updatedata("state")
        elif int(ychoice) == 4:
            print("4")
            stss.updatedata("Class")
        elif int(ychoice) == 5:
            print("5")
            stss.updatedata("Math")
        elif int(ychoice) == 6:
            print("6")
            stss.updatedata("English")
        elif int(ychoice) == 7:
            print("7")
            stss.updatedata("Hindi")
        elif int(ychoice) == 8:
            print("8")
            stss.updatedata("Science")
        elif int(ychoice) == 9:
            print("9")
            stss.updatedata("Computer")
        elif int(ychoice) == 10:
            print("10")
            stss.updatedata("Social_Science")
        elif int(ychoice) == 11:
            print("11")
        else:
            print("Invalid Choice..\n Please Try Again..")

    def updatedata(self,child):
        self.rno = 0
        rno=input("Enter Roll no.")
        newdata=input("Input new Data for "+child)
        a_file = open("student2.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        z = 0
        for i in json_object["content"]:
            if (i["roll_no"] == rno):
                z=1
                i[child] = newdata
                a_file = open("student2.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
                print("Data Update "+ child+"="+newdata)
                break
        if z==0:
            print("Roll number does not Exists...")

#Creating_Object
str = Student()

print("""Enter choice:
       1. For Writing..
       2. For Reading..
       3. For Deleting..
       4. For Editing..
   """)
x = input("Enter Input...")

if int(x) == 1:
    rn = input("Enter Roll number")
    Name = input("enter Name")
    city = input("enter city")
    state = input("enter state")
    classs = input("enter class")
    math = input("enter math")
    english = input("enter english")
    hindi = input("enter hindi")
    Science = input("enter science")
    computer = input("enter computer")
    social_Science = input("enter ssc")
    obt_marks = input("Enter Obtain Marks")
    percentage = input("Enter Percentage")
    Status = input("Status")
    print("Loading...")
    print("Data Added Successfully....")
    str.writingFile(rn, Name, city, state, classs, math, english, hindi, Science, computer, social_Science,obt_marks,percentage,
                    Status)

elif int(x) == 2:
    obj = Student()
    rn = input("Enter Student roll number..")
    obj.readFile(rn)

elif int(x) == 3:
    str.deleteFile()

elif int(x) == 4:
    str.editFile()

else:
    print("Invalid Choice..\n Please Try Again..")