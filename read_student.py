with open("data1/student.txt","r") as file:
    for line in file:
        print(line)    

with open("data1/student.txt","r") as file:
    for line in file:
        print(line.strip())          