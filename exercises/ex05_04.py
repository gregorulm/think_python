def is_triangle(a, b, c):
    if a > b + c or b > a + b or c > a + b:
        return "Not a triangle."
    else:
        return "Triangle."

def triangle_input():
    a = int(raw_input("Enter length of side a: "))
    b = int(raw_input("Enter length of side b: "))
    c = int(raw_input("Enter length of side c: "))
    print is_triangle(a, b, c)

#print is_triangle(1,2,3) # degenerate triangle
triangle_input()
