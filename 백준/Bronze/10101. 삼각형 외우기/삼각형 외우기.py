a_angle = int(input())
b_angle = int(input())
c_angle = int(input())

total_angle = a_angle + b_angle + c_angle

if a_angle == b_angle == c_angle == 60:
    print("Equilateral")
elif total_angle == 180 and (a_angle == b_angle or b_angle == c_angle or a_angle == c_angle):
    print("Isosceles")
elif total_angle == 180 and (a_angle != b_angle and a_angle!= c_angle and b_angle != c_angle):
    print("Scalene")
elif total_angle != 180:
    print("Error")