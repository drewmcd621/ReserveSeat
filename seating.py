import re


def toStr(seatMap):
    str = ""
    for row in seatMap:
        str += "".join(row) + "\n"

    return str


def build(rows, cols, reserved):
    row = ['0'] * cols
    map = list()
    for i in range(0, rows):
        map.append(list(row))

    for seat in reserved:
        rexp = r"R(?P<row>\d+)C(?P<col>\d+)"
        m = re.match(rexp, seat)
        row = int(m.group('row')) - 1
        col = int(m.group('col')) - 1
        map[row][col] = 'S'

    return map



def reserve(map, n):

    #Check if the user is reserving more than 10 seats
    if(n>10):
        print "Please reserve 10 seats or less"
        return map
    #Get clmns
    clmns = len(map[0])

    #Turn
    mapStr = toStr(map)

    #Get the best seat column
    bestSeat = clmns/2.0

    #Setup regular expression, if only 1 ticket needs reserved just look for a 0
    if (n==1):
        regex = r"0"
    else:
        regex = r"0(?=" + "0"*(n-1) + ")"

    #Used to record the best seat and it's score
    bestScore = None
    bestR = None
    bestC = None

    #Loop through matches found by te regular expression
    for match in re.finditer(regex, mapStr):
        index = match.start()

        #Find the row and column
        row = int(index / (clmns+1))
        col = (index % (clmns+1))
        #Calculate the score
	mid = col + (n-1)/2.0 #get middle seat
        score = row + abs(mid - bestSeat)

        #Determine if this is the best seat so far
        if(bestScore is not None):
            if(score < bestScore):
                bestScore = score
                bestR = row
                bestC = col
        else:
            bestScore = score
            bestR = row
            bestC = col


    if bestR == None:
        print "Not Avaliable"
        return map

    for i in range(bestC, bestC + n):
        map[bestR][i] = 'R'

    #Generate reserve string
    reservation = "R" + str(bestR + 1) + "C" + str(bestC + 1)
    if n > 1:
        reservation +=  " - R" + str(bestR + 1) + "C" + str(bestC + n)

    print reservation

    return map
