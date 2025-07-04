semiperim = lambda x,y,z: (x + y + z)/2
heron = lambda x,y,z: (semiperim(x,y,z) * (semiperim(x,y,z) - x) * (semiperim(x,y,z) - y) * (semiperim(x,y,z) - z))**0.5

def main():
    x = float(input("Enter the length of side x: "))
    y = float(input("Enter the length of side y: "))
    z = float(input("Enter the length of side z: "))
    
    if x + y > z and x + z > y and y + z > x:
        area = heron(x, y, z)
        print(f"The area of the triangle with sides {x}, {y}, and {z} is {area:.2f}")
    else:
        print("The lengths do not form a valid triangle.")

main()