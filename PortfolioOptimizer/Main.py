
from numpy import square
import math

def main():
    stockdict = stockDictionary()
    
    
    for stock in stockdict:
        print(stockdict[stock])


    if len(stockdict) == 2:

        weightX = 0.5
        weightY = 0.5

        portfolioVar = ((square(weightX))*variance(stockdict["stock1"]))+\
        ((square(weightY))*variance(stockdict["stock2"]))+\
        (2*weightX*weightY*covariance(stockdict["stock1"],stockdict["stock2"]))
        
    
    elif len(stockdict) == 3:

        weightX = 0.34
        weightY = 0.33
        weightZ = 0.33

        portfolioVar = ((square(weightX))*variance(stockdict["stock1"]))+\
        ((square(weightY))*variance(stockdict["stock2"]))+\
        (square(weightZ)*variance(stockdict["stock3"]))+\
        (2*weightX*weightY*covariance(stockdict["stock1"],stockdict["stock2"]))+\
        (2*weightX*weightZ*covariance(stockdict["stock1"],stockdict["stock3"]))+\
        (2*weightZ*weightY*covariance(stockdict["stock3"],stockdict["stock2"]))
    
    elif len(stockdict) == 4:
        weightX = 0.25
        weightY = 0.25
        weightZ = 0.25
        weightX1 = 0.25

        portfolioVar = ((square(weightX))*variance(stockdict["stock1"]))+\
        ((square(weightY))*variance(stockdict["stock2"]))+\
        (square(weightZ)*variance(stockdict["stock3"]))+\
        (square(weightX1)*variance(stockdict["stock4"]))+\
        (2*weightX*weightY*covariance(stockdict["stock1"],stockdict["stock2"]))+\
        (2*weightX*weightZ*covariance(stockdict["stock1"],stockdict["stock3"]))+\
        (2*weightZ*weightY*covariance(stockdict["stock3"],stockdict["stock2"]))+\
        (2*weightX1*weightX*covariance(stockdict["stock4"],stockdict["stock1"]))+\
        (2*weightX1*weightY*covariance(stockdict["stock4"],stockdict["stock2"]))+\
        (2*weightX1*weightZ*covariance(stockdict["stock4"],stockdict["stock3"]))
    
    elif len(stockdict) == 5:
        weightX = 0.2
        weightY = 0.2
        weightZ = 0.2
        weightX1 = 0.2
        weightY1 = 0.2

        portfolioVar = ((square(weightX))*variance(stockdict["stock1"]))+\
        ((square(weightY))*variance(stockdict["stock2"]))+\
        (square(weightZ)*variance(stockdict["stock3"]))+\
        (square(weightX1)*variance(stockdict["stock4"]))+\
        (square(weightY1)*variance(stockdict["stock5"]))+\
        (2*weightX*weightY*covariance(stockdict["stock1"],stockdict["stock2"]))+\
        (2*weightX*weightZ*covariance(stockdict["stock1"],stockdict["stock3"]))+\
        (2*weightZ*weightY*covariance(stockdict["stock3"],stockdict["stock2"]))+\
        (2*weightX1*weightX*covariance(stockdict["stock4"],stockdict["stock1"]))+\
        (2*weightX1*weightY*covariance(stockdict["stock4"],stockdict["stock2"]))+\
        (2*weightX1*weightZ*covariance(stockdict["stock4"],stockdict["stock3"]))+\
        (2*weightY1*weightX*covariance(stockdict["stock5"],stockdict["stock1"]))+\
        (2*weightY1*weightY*covariance(stockdict["stock5"],stockdict["stock2"]))+\
        (2*weightY1*weightZ*covariance(stockdict["stock5"],stockdict["stock3"]))+\
        (2*weightY1*weightX1*covariance(stockdict["stock5"],stockdict["stock4"]))


    print((portfolioVar))

def stockDictionary (): #Its taking input right now, it will pull data from Yahoo finance later
    dictionary = {}
    add = ""
    stock = 1

    while add != "n":
        dictionary["stock"+str(stock)]=list(input("Please enter the stock returns: "))
        stock += 1
        add = input ("Press any key to add another stock, press 'n' to stop: ")
    
    return dictionary

def stdev (stockReturns):
    return math.sqrt(variance(stockReturns))

def variance (stockReturns): #stockReturns needs to be a list here
   
    empty = 0
    numerator = 0
    accumulatorX = 0

    for x in stockReturns:
        accumulatorX += float(x)
    
    mean = accumulatorX/(len(stockReturns))
    
    for y in stockReturns:
        numerator += square(float(y)-mean)
    
    final = numerator/(len(stockReturns)-1)

    return final

# The final value is returned to the function
def covariance (stockX,stockY): #stockX and stockY are to be list inputs
    
    if len(stockX) == len(stockY):
        empty = 0
        accumulatorX = 0
        accumulatorY = 0
        numerator = 0
        
        for x in stockX:
            accumulatorX += float(x)
        
        for y in stockY:
            accumulatorY += float(y)
        
        meanX = accumulatorX/(float(len(stockX)))
        meanY = accumulatorY/float(len(stockY))

        while empty <= max(float(len(stockX)),float(len(stockY)))-1:
            numerator += (float(stockX[empty])-meanX)*(float(stockY[empty])-meanY)
            empty += 1
        
        final = numerator/(len(stockX)-1)

        return final


    else:
        print("The length of both lists need to be equal for co-variance")
        
    

    
main()

