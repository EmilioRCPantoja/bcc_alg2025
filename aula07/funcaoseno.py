from math import sin, radians, degrees, ceil
for i in range(360):
    i = radians(i)
    seno=sin(i)*360
    delta = ceil(seno)
    delta = (degrees(delta))
    delta = ceil(delta/ 330)
    print((delta+60)*" "+"*")
