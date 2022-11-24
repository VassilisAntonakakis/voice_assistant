import weatherReport

def strReconstruct(partsList, index):
    tempTerm = ""
    while(len(partsList) > index):
        if partsList[index] == "-" or partsList[index] == "+":
            tempTerm = " " + tempTerm + partsList[index]
        else: tempTerm = tempTerm + partsList[index] + " ";
        index = index + 1
    
    tempTerm = tempTerm.strip()
    return tempTerm

def commandParser(command):

    if "exact request" in command:
        tokenList = command.split()
        tempCommand = tokenList[0] + " " + tokenList[1]
        tokenList[0] = tempCommand
        tempTerm = strReconstruct(tokenList, 2)
        tokenList[1] = tempTerm
    elif "request" in command:
        tokenList = command.split(" ",1)
    
        if "exclude" in tokenList[1]:
            tempTokenList = tokenList[1].split(" ")

            for index in range(len(tempTokenList)-1):
                if tempTokenList[index] == "exclude":
                    tempTokenList[index] = "-"
            tokenList[1] = strReconstruct(tempTokenList, 0)
        
        if "include" in tokenList[1]:
            tempTokenList = tokenList[1].split(" ")

            for index in range(len(tempTokenList)-1):
                if tempTokenList[index] == "include":
                    tempTokenList[index] = "+"
            tokenList[1] = strReconstruct(tempTokenList, 0)
        return tokenList
    elif "weather" in command:
        weatherReport.getWeather(command)


#commandTokenizer("get weather")