from seating import build, reserve, toStr
import time


start = time.time()

seatMap = build(3, 11, ["R1C4","R1C6","R2C3","R2C7","R3C9","R3C10"])

seatMap = reserve(seatMap, 3)

seatMap = reserve(seatMap, 4)

seatMap = reserve(seatMap, 6)

seatMap = reserve(seatMap, 5)

seatMap = reserve(seatMap, 2)

seatMap = reserve(seatMap, 10)

print toStr(seatMap)

print("--- %s seconds ---" % (time.time() - start))
