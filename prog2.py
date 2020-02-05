##prog2.py
##Sayed Yoseph Sadat
##
##1/29/17

## Question 1
def pq(i,s,c,pn,pa,d,n):
    """ i = importance(1-10)
        s = number of hours of sleep
        c = shots of espresso or other stimulants
        pn = hours of preparation needed to excel
        pa = hours you actually spent preparing
        d = difficulty of subject matter(1-10)
        n = level of nervousness(1-10)"""
    result = (( 8 * pa * ( s + c)))/ (3 * pn * ( d + n + i))
    return result
## Question 2
def inchesToMeters(inches):
    """ Takes number in inches
        Converts to Meters
        Returns the length in Meters"""
    conversion_factor = .0254 
    result = inches * conversion_factor
    return result

## Question 3
def poundsToKgs(pounds):
    """ Takes weight in pounds
        Converts that number to kilograms
        Returns the weight in kilograms"""
    conversion_factor = .453592
    result = pounds * conversion_factor
    return result
##Question 4
def bmi(height_inches, weight_pounds):
    """ Takes height in inches/ weight in pounds
        Converts those numbers to meters/ kilograms
        Return as body mass index"""
    weight_conversion_factor = .453592
    height_conversion_factor = .0254
    weight = weight_pounds * weight_conversion_factor
    height = height_inches * height_conversion_factor
    result = weight / (height * height)
    return result
