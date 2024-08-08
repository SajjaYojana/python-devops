a = 42   # This is an integer
print(a)

#Float
b = 23.54342
print(b)

# boolean
c = True
print(c)

# Strings
d = 'This is string1'
e = "This is string2"
f = """
This is string3 or multi string
"""
#Override the value of a variable
d = 'the weather is good'
print(d)

#list
test_list = ["hello", "world", "Python"]
print(test_list)

#Tuple
test_tuple = ("hello", "world", "Python")
print(test_tuple)

#Dict
test_dict = {'a' : 1 , 'b' :2}
print(test_dict)

#Set
test_set = {'a','b', "abc"}
print(test_set)

# type() function --> returns the data type of a variable
print(type(test_list))
print(type(print))

#operators
#1.add
a = 34
b = 24.654
c = a + b
print("sum = " ,c)
#substract
d = a - b 
print("sub = " ,d)
#Multiply
e = a * b
print("multiply=" ,e)
#division
f = 12
g = 3
h = f  / g
print("remainder= ",h)
#Modulo division
i = f % g
print(i)

#Addition
x = "42"
y = "43"
print(a + b) #concatenation

#Power
a=10
print(a**2)

#Comparision Operators
x=15
y=25
res=x>y
res1=x<y
res2=x!=y
print(res)
print(res1)
print(res2,a==b)