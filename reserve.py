import re

def findBest(map, n):
    print map
    #Find the number of seats in a row
    clmns = re.search(r"\n",map).start()

    #Get the best seat column
    bestC = clmns/2.0

    #Setup regular expression, if only 1 ticket needs reserved just look for a 0
    if (n==1):
        regex = r"0"
    else:
        regex = r"0(?=" + "0"*(n-1) + ")"

    #Used to record the best seat and it's score
    bestDist = None
    bestS = None

    #Loop through matches found by te regular expression
    for match in re.finditer(regex, map):
        index = match.start()
        #Find the row and column
        row = int(index / (clmns+1))
        col = index % (clmns+1)
        #Calculate the score
        score = row + abs(col - bestC)

        #Determine if this is the best seat so far
        if(bestS):
            if(score < bestDist):
                bestDist = score
                bestS = index
        else:
            bestDist = score
            bestS = index

    #Return the first seat in the best match
    return bestS

def holdSeat(map, seat):
    rexp = r"R(?P<row>\d+)C(?P<col>\d+)"


def build(rows, cols, reserved):
    row = "0" * cols + "\n"
    map = row * rows



print findBest("00010100000\n00100010000\n00000000110",3)
