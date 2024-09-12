import math
eq = '4x^2+4x +    (-8) =  0'
eq = eq.replace(" ", '')


a_start_position = 0
a_end_position = eq.find("x^2")
a = eq[a_start_position:a_end_position]

a = a.replace("(", "")
a = a.replace(")", "")
a = a.replace("*", "")

b_start_position = eq.find("x^2+")+4
b_end_position = eq.find("x+")
b = eq[b_start_position:b_end_position]

b = b.replace("(", "")
b = b.replace(")", "")
b = b.replace("*", "")

c_start_position = eq.find("x+")+2
c_end_position = eq.find("=")
c = eq[c_start_position:c_end_position]

c = c.replace("(", "")
c = c.replace(")", "")
c = c.replace("*", "")
print(a, b, c)  

a = int(a)
b = int(b)
c = int(c)

d = b*b - 4*a*c
if d >= 0:
    print("d=",d)
    x1 = (-b + math.sqrt(d)) / 2*a
    x2 = (-b-math.sqrt(d)) / 2*a
    print("x1=", x1)
    print("x2=", x2)
else:
    print("немає розвязків")    


