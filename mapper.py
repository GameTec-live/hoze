with open("mapped", "a+") as f:
    i = 0
    cord = 0
    for i in range(1, 1000):
        f.write( str(i) + "," + str(cord) + ",0,-16,0,0,0,1,1,1,0,5,10,24,10,24,10,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0\n")
        i = i + 1
        cord = cord + 50