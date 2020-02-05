##prog4.py
##Sayed Yoseph Sadat
##
##2/13/17

##Question 1

def sumOfOdds(integer):
    """ Takes an integer greater than or equal to 1 as an argument
        Returns the result of adding the odd integers between 1 and the value of the given argument"""
    result = 0
    counter = 1
    while counter <= integer:
        if counter % 2 != 0:
            result = result + counter
            counter += counter + 1
    return result

##Question 2

def productOfPowersOf2(exp1,exp2):
    """Takes two arguments, both being non-negative integers,
        Compute and return the product of all powers of from 2exp1 to 2exp2"""
    result = 1
    while(exp1 <= exp2):
          result *= 2 ** exp1 
          exp1 += 1
    return result 

##Question 3

def printAsterisks(number):
    """ Expects one argument as a non-negative integer
        Prints a row of asterisks"""
    total = 0
    while (total < number):
        total += 1
        print('*', end="")

##Question 4

def printTriangle(integer):
    """ Expects a non negaive integer
        Prints a right triangle, where both height and weight are given by value"""
    total = 0
    while (total < number):
        total += 1
        print('*', /n"")


##Question 5
def allButMax():
    """Function expects no argumnets, but gets input from user
        Ask user to enter series of number greater than or equal to zero
        Function the prints the sum and returns the sum"""
        
    total = 0
    final = 0
    tmax = max
    
    while True:
        r = input("Enter the next number: ")
        if r == "end":
            break
        r = int(r)
        total = int(r) + total
    final = total - tmax
    print("The sum of all values except for the maximum value is: " + str(total)



##Question 6
def avgSumOfSquares():
    """Expects no arguments and instead gets input from the user
        Asks user to enter a series of numbers one at a time and to type end when done
        Fucntions computes the average of the sum
        Then Prints the average of the sum of the squares and returns the average"""
    total = 0
    counter = 0
    while True: 
        n = input("Enter next number: ")
        if n == "end":
            break
        n = int(n)
        counter += 1
        total = n**2 + total
    final = total / counter
    print("The average of the sum if the squares is: " + str(final))




          def countDiffs(string1,string2):
    """This function takes two strings as an arguement and reads them letter
        letter and returns the number of characters that differ"""
    counter=0
    for letter in range(0,len(string1)):
        if(sting1[letter]!= sting[letter]):
            counter = count + 1
    return counter 
        
