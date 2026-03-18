#string slicing
name = "vaishnavi"
nameslice = name[0:5]  #start from index 0 and end at index 5 excluding 5
print(nameslice) #op = vaish
char = name[1]
print(char) #element at index1 appears

#-------------------------------------------------------------

#negative slicing
name = "vaishnavi"
print(name[0:5])
print(name[-4:-1]) #nav is the output start from backward and count from -1
print(name[:5]) #starting empty so 0 is considered
print(name[-4:]) #ending empty so is considered -1

#skip in slice
name = "0123456789"
print(name[1:7:3]) #1st 1:7 and again skip 3 3 in tht so 14 is op
print(name[1:8:2])