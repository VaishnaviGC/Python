#marks of 6 students entered by the user and displayed in a sorted manner
marks = []

s1 = int(input("Enter s1 marks:"))
marks.append(s1)
s2 = int(input("Enter s2 marks:"))
marks.append(s2)
s3 = int(input("Enter s3 marks:"))
marks.append(s3)
s4 = int(input("Enter s4 marks:"))
marks.append(s4)
s5 = int(input("Enter s5 marks:"))
marks.append(s5)
s6 = int(input("Enter s6 marks:"))
marks.append(s6)

marks.sort()
print(marks)