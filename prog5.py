##prog5.py
##Sayed Yoseph Sadat
##
##2/26/17

##Question 1
def sumOfOdds(integer):
    """ Function takes one argument, an integer greater than or equal to 1,
        Returns the result of adding the odd integers between 1 and the value of the given argument"""
    result = 0
    counter = 1
    for int in integer:
        if integer % 2 != 0:
            integer += 2
    return result
    
##Question 2
def countChar(character,string):
    """ Function takes two arguments, single character and arbitrary lenght
        Returns the number of times character appears in the string"""
    counter = 0 
    for char in string:
        if character == char:
            counter += 1
    return(counter)
##Question 3
def countDiffs(string1,string2):
    """ Function takes two arguments of the same length
        Function should compare the strings and count the number of times the strings have different characters"""
    counter = 0 
    for char in [string1,string2]:
        if string1[0:len(string1)] != string2[0:len(string2)]:
            counter += 1
    return(counter)
    
##Question 4
def avgSumOfSquares(in_list):
    """Function expects one list of numbers
        Function then computes the average of the sum of the squares of all the values entered and then returns the value """
    count = 0
    total = 0
    for value in in_list:
        value = value ** 2
        count = count + 1
        total = total + value
    if count == 0:
        return None
    return total/count
        
        
