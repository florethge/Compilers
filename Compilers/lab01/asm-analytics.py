import re

def searchFunctions(c, functions, address):
    logFile = open('log', "r")
    for line in logFile:
        funct =re.findall("^_[a-z].*\:$", line)
        if len(funct) != 0:
            functions.append(funct)
            addr = (logFile.next()).split(":")
            address.append(addr[0])
            fa = zip(functions, address)
            c += 1
    print("You have %s functions:" %(c))
    return fa

def addressesFormat():
    nAddress= (searchFunctions(0, functions = [], address = []))
    for n in nAddress:
        print ("function: %s located at: %s" %(n[0], n[1]))

def operations():
    logFile = open('log', "r")
    countW={}
    aux=[]
    for x in logFile:
        line=x[15:]
        instruction=line.split()
        for element in instruction:
            if len(element)>=4 and len(element)<=8 and re.findall("^[a-z][a-z]", element) and element != "section" and element != "format":
                aux.append(element)
    for inst in aux:
        if inst in countW:
            countW[inst]=countW[inst]+1
        else:
            countW[inst]=1

    print("You have %s types of instructions in this object file:" %(len(countW)))
    for x,y in countW.items():
        print("%s   : Executed: %s" %(x, y))
    logFile.close()

def main():
    addressesFormat()
    operations()

main()