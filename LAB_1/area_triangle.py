import math
def tri_area(x, y, z):
    s = (x + y + z) / 2
    a = math.sqrt(s * (s - x) * (s - y) * (s - z))
    return a

def get_side():
    print("Enter sides of triangle:")
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))
    return a, b, c
area = tri_area(20, 30, 40)
print("Area of triangle with sides 20, 30, 40 =", area)
a1, b1, c1 = get_side()
print("Sides of triangle 1 =", a1, b1, c1)
a2, b2, c2 = get_side()
print("Sides of triangle 2 =", a2, b2, c2)
area1 = tri_area(a1, b1, c1)
area2 = tri_area(a2, b2, c2)
print("Area of triangle 1 =", area1)
print("Area of triangle 2 =", area2)
tot_area = area1 + area2
print("Total area of the 2 triangles =", tot_area)
contri1 = (area1 / tot_area) * 100
contri2 = (area2 / tot_area) * 100
print("Contribution of triangle 1 =", contri1, "%")
print("Contribution of triangle 2 =", contri2, "%")
