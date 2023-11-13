def roots(a, b, c):
    root = b**2-4*a*c
    if root > 0:
        root1 = (-b + (b**2-4*a*c)**2)/(2*a)
        root2 = (-b - (b**2-4*a*c)**2)/(2*a)
        print(f"thera are Two real roots: {root1} and {root2}")
    elif root == 0:
        root = -b / (2*a)
        print(f"there is One real root: {root}")
    else:
        print("No real roots")
a = int(input("Enter the  a: "))
b = int(input("Enter the  b: "))
c = int(input("Enter the  c: "))
roots(a, b, c)
