dictionary = {'Aditya': 85 , 'Shashank':82, 'Jia': 78,'Lokesh': 15, 'Siddhant': 59, 'Vijet': 42}
m = input("Enter the student's name: ")
if m in dictionary:
    print(m,"'s marks:", dictionary[m])
else:
    print("Student not found")


