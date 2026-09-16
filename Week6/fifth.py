file = open("Marks.data", "w")
n = int(input("Enter Number of Students: "))

for i in range(n):
    roll = input("Enter Roll No. : ")
    name = input("Enter Name : ")
    marks = input("Enter Marks : ")
    file.write(roll + " " + name + " " + marks + "\n")

file.close()

print("Student details saved in Marks.data")