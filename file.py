import json
import os

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
        for i in json_object["content"]:
            if (i["roll_no"] == rno):
                print(i)
                break
            else:
                print("Roll number does not Exists...")
                break
#Creating_File
    def createFile(self):
        x = open("file.txt","w")
        print("File Create Successfully...")

#Deleting_File
    def deleteFile(self):
        os.remove("file.txt")


#Creating_Object
str = Student()

print("""Enter choice:
       1. For Writing..
       2. For Reading..
       3. For Creating..
       4. For Deleting
   """)
x = input("Enter Input")

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
    obtain_marks = input("enter obtain marks")
    total_percentage = input("enter total")
    status = input("Enter status")
    print("Loading...")
    print("Data Added Successfully....")

    str.writingFile(rn, Name, city, state, classs, math, english, hindi, Science, computer, social_Science,
                    obtain_marks, total_percentage, status)


elif int(x) == 2:
    obj = Student()
    rn = input("Enter Student roll number..")
    obj.readFile(rn)

elif int(x) == 3:
    str.createFile()
    print("create file..")

elif int(x) == 4:
    str.deleteFile()
    print("deleting file...")

else:
    print("Invalid Choice..\n Please Try Again..")