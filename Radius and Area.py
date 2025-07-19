def circle():
    r=int(input("Enter radius of circle:"))
    print("Area of circle is" , 3.14*r*r)
    
def square(a):
    print("Area of Square is :" ,a*a)
    
def tringle():
    b=int(input("Enter base:"))
    h=int(input("Enter height of triangle:"))
    return 0.5*b*h
def rect(a,b):
    return a*b

while (True):
    print("CIRCLE")
    print("SQUARE")
    print("TRINGALE")
    print("RECTANGLE")
    print("EXIT")
    
    ch=int(input("Enter your choice...."))
    match ch:
        case 1:
            circle()
        case 2:
            a=int(input("Enter side of square"))
            square(a)
        case 3:
            res=tringle()
            print("Area of triangle:",res)
        case 4:
            a=int(input("Enter length of rec:"))
            b=int(input("Enter breadth of rec:"))
            res=rect(a,b)
            print("Area of rectangle is ",res)
        case 5: exit(0)
        case _:print("Invalid Option")
