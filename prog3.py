##prog3.py
##Sayed Yoseph Sadat
##
##2/1/17

## Question 1
def max4( a,b,c,d ):
    """ Function expects four arguments
        All arguments must be numbers
        Returns the maximum of the four values """
    if a > b and a > c and a > d :
        print(a)
    elif b > a and b > c and b > d :
        print(b)
    elif c > b and c > a and c > d :
        print(c)
    elif d > b and d > c and d > a :
        print(d)
## Question 2
def grade(percentage):
    """ Function expects one argument
        Argument represents a number 0-100
        Returns number as a single character representing a letter grade"""
    if percentage >= 90:
        print(" A ")
    elif percentage >=80 and percentage < 90:
        print("B")
    elif percentage >= 70 and percentage < 80:
        print("C")
    elif percentage >= 60 and percentage < 70:
        print("D")
    elif percentage <= 59:
        print("F")

## Question 3
def days(month):
    """ Expects one argument
        Argument should be name of a month as a string(Use ' ')
        Returns the number of days in the month"""
    if month == 'September' or month == 'April' or month == 'June' or month == 'November':
        print("30")
    elif month == 'February':
        print("28")
    else:
        print("31")

## Question 4

def inchesToMeters(inches):
    """ Takes inches and converts to meters"""
    return(inches * .0254)
def poundsToKilograms(pounds):
    """Takes pounds and converts to kilograms"""
    return(pounds * .453592)
def bmi(height,weight):
    """Returns Body Mass Index"""
    return poundsToKilograms(w) / inchesToMeters(h)**2

def bodyMassIndex():
    name = input("Please enter your name: ")
    height = float(input("Please enter your height in inches: "))
    inchesToMeters (float(height))
    weight = float(input("Please enter your weight in pounds: "))
    poundsToKilograms (float(weight))
    bmi = poundsToKilograms(weight) / inchesToMeters(height)**2
    print(name + " has a body mass index of " + str(bmi) )
    if bmi < 18.5:
        print( name + " is underweight")
    elif bmi >= 18.5 and bmi < 25:
        print(name + " is normal weight")
    elif bmi >= 30:
        print( name + " is obese")

## Qyestion 5
def weekly_pay(wage,hours):
    if hours <= 40:
        return wage * hours
    elif hours > 40:
        return (hours - 40) * (1.5 * wage) + (wage * 40)

##Question 6

def taxes(s,income):

    if s =="s":
        if income <= 32000:
            taxes = (income * .10)
            return(taxes)
        else:
            taxes = (income - 32000) * .25 +  3200
            return(taxes)
    elif s == "m":
        if income <= 64000:
            taxes = (income * .10)
            return(taxes)
        else:
            taxes = (income - 64000) * .25 + 6400
            return(taxes)
    
    
        
