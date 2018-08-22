# эта программа позволяет посчитать площадь треугольника или круга в зависимости от вбиваемых пользователем данных
print ("Hello, user. It is time to calculate, lover")
option = input("Enter C for Circle or T for Triangle: ")
if option == "C":
    radius = float(input("Input the radius: "))
    area = 3.14159 * radius ** 2
    print ("Area: %f" % area)
elif option == "T":
    base = float(input("Input the base: "))
    height = float(input("Input the height: "))
    area = 0.5 * base * height
    print ("Area: %f" % area)
else:
    print ("Invalid shape")

print ("This programm is awesome")