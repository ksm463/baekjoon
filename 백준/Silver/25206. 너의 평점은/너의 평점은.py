credit = 0
total = 0

grade_to_point = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        point = grade_to_point[c]
        credit += b
        total += b * point

print('%.6f' % (total / credit))