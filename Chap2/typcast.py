a = "21.2" #here a is string
b = float(a) #output is still a but type shld become float

t = type(b)
print(t) #string to float conv

c = 12.5 #c is float
d = str(c) #op is still true but shld be string not float

t = type(d)
print(t) #float to string conv

v = True #c is bool
i = str(c) #op is still true but shld be string not bool

t = type(i)
print(t) #bool to string conv