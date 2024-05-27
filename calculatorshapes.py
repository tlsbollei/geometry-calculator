import time
import math

#function where you calculate area and cim. of a square, option number 1
def calculate_square():
    squareside = float(input("Enter the length of the side: "))
    squarearea = squareside * squareside 
    squarecircumference = 4 * squareside
#the area of the square and circumference are  calculated before the input (decision)
    time.sleep(1)
    squaredecision = input("Do you want to calculate the area or the circumference of the square? : ").strip().lower()
    if squaredecision == "area":
        print("The area of the square is: ", squarearea)
    else:
        print("The circumference of the square is: ", squarecircumference)

#function where you calculate area and cim. of a rectangle, option number 2
def calculate_rectangle():
    rectanglesidea = float(input("Enter the length of the rectangle (the longer side): "))
    time.sleep(1)
    rectanglesideb = float(input("Enter the width of the rectangle (the shorter side): "))
    rectanglearea = rectanglesidea * rectanglesideb 
    rectanglecircumference = 2 * (rectanglesidea + rectanglesideb)
#again, the area of the rectangle and its circumference are calculated before the decision
    time.sleep(1)
    rectangledecision = input("Do you want to calculate the area or the circumference of the rectangle? : ").strip().lower()
    if rectangledecision == "area":
        print("The area of the rectangle is: ", rectanglearea)
    else: 
        print("The circumference of the rectangle is: ", rectanglecircumference)
#function where you calculate area, circumference and unknown third side using pythagoras theorem, option number 3
def calculate_triangle():
    trianglesidea = input("Enter the length of the first side, a. If not known, write unknown: ").strip().lower()
    trianglesideb = input("Enter the length of the second side, b. If not known, write unknown: ").strip().lower()
    trianglesidec = input("Enter the length of the third side, c. If not known, write unknown: ").strip().lower()

    time.sleep(1)
    triangleareaorcircumference = input("Do you wish to calculate the area , the circumference of the triangle or the length of the third, unknown side? :  ").strip().lower()
    #start of triangle calculation and three subcategories - first one is right under, area
    if triangleareaorcircumference == "area":
        vyska = float(input("Please, enter the height respective to a side of the triangle  :  "))
        #asking for the heigth because its mandatory for us to know that in order to calculate the area, I plan on implementing a version and a function where the respective heigth will be calculated if the correct measurements are given
        time.sleep(1)

        vyskarespective = input("Please, enter the side for which the height you just entered is respective to. (a/b/c)  :  ").strip().lower()

        #formula for the calculation of the area of a triangle = 1/2 * a * height respective to side a 
        #here, the variable "vyska" the value of which you have entered, is the length of the height respective to side a 
        #vyskarespective specifies what side the "vyska" variable is respective to, which is in the first case "a"
        if vyskarespective == "a":
            trianglearea11 = float(vyska) / 2
            trianglearea22 = float(trianglearea11) * float(trianglesidea)
            print("The area of this triangle is :  ", trianglearea22)
            #float(vyska) / 2 is basically 1/2 (one half) times float(vyska), which is the height respective to the side
            #then, the result of the variable "trianglearea11" is multiplied by the variable trianglesidea, float is included in order to specify that we are counting with the number form of the variable, not the string form
            #simply following the formula to calculate the area of a tringle, same thing is repeating under
        elif vyskarespective == "b":
            trianglearea33 = float(vyska) / 2
            trianglearea44 = float(trianglearea33) * float(trianglesideb)
            print("The area of this triangle is :  ", trianglearea44)
        elif vyskarespective == "c":
            trianglearea55 = float(vyska) / 2
            trianglearea66 = float(trianglearea55) * float(trianglesidec)
            print("The area of this triangle is :  ", trianglearea66)
        else:
            print("Method not recognized.")
            #this means you have entered that the heigth you entered is not respective to neither of the three sides in a triangle, therefore incorrect

    #start of triangle calculation and three subcategories - second one is right under, circumference
    if trianglesidea == "unknown" and trianglesideb != "unknown" and trianglesidec != "unknown" and triangleareaorcircumference == "circumference":
        #comparision operator != is used in this context to distinguish between the ones that are unknown (what the user entered) and the ones that are known and have a numeric form (!=) = different from unknown
        #because of this, if something else than "unknown" or a number is inputted, the program fails, will fix soon
        c2 = float(trianglesidec) ** 2
        b2 = float(trianglesideb) ** 2
        a2 = c2 - b2
        a = math.sqrt(a2)
        trianglecircumference1 = float(trianglesideb) + float(trianglesidec) + a 
        #basic pythagoras theorem
        print("The circumference of the triangle is: ", trianglecircumference1)
    elif trianglesidea != "unknown" and trianglesideb == "unknown" and trianglesidec != "unknown" and triangleareaorcircumference == "circumference":
        c22 = float(trianglesidec) ** 2
        a22 = float(trianglesidea) ** 2
        b22 = c22 - a22
        b23 = math.sqrt(b22)
        trianglecircumference2 = float(trianglesidec) + float(trianglesidea) + b23
        #basic pythagoras theorem
        print("The circumference of the triangle is: ", trianglecircumference2)
    elif trianglesidea != "unknown" and trianglesideb != "unknown" and trianglesidec == "unknown" and triangleareaorcircumference == "circumference":
        a33 = float(trianglesidea) ** 2 
        b33 = float(trianglesideb) ** 2
        c33 = a33 + b33
        c34 = math.sqrt(c33)
        trianglecircumference3 = float(trianglesidea) + float(trianglesideb) + c34
        #basic pythagoras theorem
        print("The circumference of the triangle is: ", trianglecircumference3)
    elif trianglesidea != "unknown" and trianglesideb != "unknown" and trianglesidec != "unknown" and triangleareaorcircumference == "circumference":
        trianglecircumference4 = float(trianglesidea) + float(trianglesideb) + float(trianglesidec)
        #this is an exception - if the user entered all three credentials and wants to calculate circumference, then its just a simple arithmetic operation
        print("The circumference of the triangle is : ", trianglecircumference4)
    
    #start of triangle calculation and three subcategories - third one is right under, unknown
    #here simple pythagoras theorem is used in order to calculate the third side of the triangle if two sides 

    if trianglesidea == "unknown" and trianglesideb != "unknown" and trianglesidec != "unknown":
        tretiastrana1 = float(trianglesideb) ** 2
        tretiastrana2 = float(trianglesidec) ** 2
        tretiastrana3 = float(tretiastrana2) - float(tretiastrana1)
        tretiastrana4 = math.sqrt(tretiastrana3)
        print("The third side, a, is :   ", tretiastrana4)
       #in the calculation above, we know the length of the hypotenuse and opposite side and we need to calculate the adjacent side.
    elif trianglesidea != "unknown" and trianglesideb == "unknown" and trianglesidec != "unknown":
        stvrtastrana1 = float(trianglesidea) ** 2
        stvrtastrana2 = float(trianglesidec) ** 2
        stvrtastrana3 = float(stvrtastrana2) - float(stvrtastrana1)
        stvrtastrana4 = math.sqrt(stvrtastrana3)
        print("The third side, b, is  :  ", stvrtastrana4)
        #in the calculation above, we know the length of the adjacent and hypotenuse side and we need to calculate the opposite side.
    elif trianglesidea != "unknown" and trianglesideb != "unknown" and trianglesidec == "unknown":
        piatastrana1 = float(trianglesidea) ** 2
        piatastrana2 = float(trianglesideb) ** 2
        piatastrana3 = float(piatastrana1) + float(piatastrana2)
        piatastrana4 = math.sqrt(piatastrana3)
        print("The third side, c, is  :  ", piatastrana4)
        #in the calculation above, we know the length of the adjacent and opposite side and we need to calculate the hypotenuse.
    

    
#function where you calculate the area and circumference of a circle, results wont be 100% because I was calculating with hardcoded pi variable = 3.14 rather than math.pi constant. Thanks to this, you will get simpler numbers, but not neccesarily 100% accurate
def calculate_circle():
    pi = 3.14
    radius = float(input("What is the radius of the circle? : "))
    time.sleep(1)
    radiusnadruhu = radius ** 2
    circlearea = radiusnadruhu * pi

    time.sleep(1)
    circlecircumference = 2 * pi * radius
#calculated the circumference and area of the circle
    circledecision = input("Do you want to calculate the circumference or the area of the circle? : ").strip().lower()
    if circledecision == "area":
        print("The area of this circle is: ", circlearea)
    elif circledecision == "circumference":
        print("The circumference of this circle is: ", circlecircumference)
    else:
        print("Method not recognized.")
#Will soon add the option to calculate the radius from area and circumference, respectively.





#the function where you calculate the area and circumference of a triangle with all sides equal length
#not entirely finished, will add more functions in later versions
def calculate_equal_side_triangle():
    equalsidedecision = input("Do you wish to calculate the area, circumference or the side in the triangle?\nNOTE if you choose side, you are demanded to enter the area!!!\nNOTE if you choose area, you are demanded to enter the side!!!\nNOTE if you choose circumference, you are demanded to enter the side!!!   :  ")
    if equalsidedecision == "side":
        equalsidearea = float(input("Enter the area of the equilateral triangle  :   "))
        squarerootequilateral = math.sqrt(3)
        squarerootquilateral1 = float(squarerootequilateral) / 4 
        step1 = float(equalsidearea) / float(squarerootquilateral1)
        step2 = math.sqrt(step1)
        time.sleep(1)

        print("The side of this equilateral triangle is  :   ", step2)

    if equalsidedecision == "area":
        equalsideside = float(input("Enter the side of the equilateral triangle :  "))
        step3 = float(equalsideside) ** 2
        step4 = math.sqrt(3)
        step5 = float(step4) / 4
        equalsideareafinal = float(step5) * float(step3)
        time.sleep(1)
        print("The area of the equilateral triangle is :  ", equalsideareafinal)

    if equalsidedecision == "circumference":
        equalsideneedsideforcim = float(input("Enter the side of the equilateral triangle :  "))
        step6 = float(equalsideneedsideforcim) * 3
        print("The circumference of the equilateral triangle is :  ", step6)

        


    


#beggining  function
def play_game():
    print("Choose the shape from the following : \n1-Square \n2-Rectangle \n3-Triangle \n4-Circle \n5-Triangle with equal sides\n ... More to come!")
    shapechoice = input("I choose: ").strip()
    
    if shapechoice == "1":
        calculate_square()
    elif shapechoice == "2":
        calculate_rectangle()
    elif shapechoice == "3":
        calculate_triangle()
    elif shapechoice == "4":
        calculate_circle()
    elif shapechoice == "5":
        calculate_equal_side_triangle()
    else:
        print("Invalid choice. Please choose a valid shape.")

name = input("What is your name? : ")

time.sleep(1)

print("Welcome to the calculator of areas and circumferences of commonly used geometrical shapes,", name)

print("\n" + "-"*40 + "\n")

#give the option to restart

while True:
    play_game()
    again = input("Do you want to calculate more? (yes or no): ").strip().lower()
    print("\n\n")
    if again != "yes":
        break


input("Thank you for calculating. Press any key to exit.  ")
