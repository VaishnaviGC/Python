#tuples are inmutable

a = (1,245,76,865,4321,"vaish",False,245,245)
print(type(a))

#tuples methods
no=a.count(245)
no = a.index(1)
print(no)

#chcek if an element is present r not
li = (1,2,3,4,1,2,4,5,6,7,77,6,5,4,8,8,99,234)
print(99 in li)