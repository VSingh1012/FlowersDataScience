
#TODO Add more functions to make code more concise and user-friendly


def stop(): 
    import sys
    sys.exit()

def get_len(list): 
    print(len(list))

def makeBufferLine(): 
    print("*************")
     

def getListVals(list): 
    print(list)
    
def meanFunc(list):
    sumOfNumbers = 0
    for val in list: 
        sumOfNumbers += val
    avg = sumOfNumbers / len(list)
    print(avg)


def convertToCm(meters, feet): 
    print(str(meters) + " m = " + str(meters * 100.00) + " cm")
    print(str(feet) + " ft = " + str(feet * 30.48) + " cm")



