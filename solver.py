# Rotor Values
rotors = [
    [[3, 0, 6, 0, 10, 0, 7, 0, 15, 0, 8, 0]],
    [[12, 0, 4, 0, 7, 15, 0, 0, 14, 0, 9, 0,],
     [6, 17, 7, 3, 0, 6, 0, 11, 11, 6, 11, 0,]],
    [[16, 0, 9, 0, 5, 0, 10, 0, 8, 0, 22, 0],
     [14, 1, 12, 0, 21, 6, 15, 4, 9, 18, 11, 26],
     [5, 0, 7, 8, 9, 13, 9, 7, 13, 21, 17, 4]],
    [[6, 0, 10, 0, 10, 0, 1, 0, 9, 0, 12, 0],
     [9, 0, 17, 19, 3, 12, 3, 26, 6, 0, 2, 13],
     [14, 12, 3, 8, 9, 0, 9, 20, 12, 3, 6, 0],
     [11, 0, 8, 0, 16, 2, 7, 0, 9, 0, 7, 14]],
    [[7, 16, 8, 7, 8, 8, 3, 4, 12, 2, 5, 10],
     [14, 21, 21, 9, 9, 4, 4, 6, 6, 3, 3, 14],
     [11, 12, 13, 14, 15, 4, 5, 6, 7, 8, 9, 10],
     [14, 11, 14, 11, 14, 11, 11, 14, 11, 14, 11, 14]]
]

# If you want to change the starting offset, do it here
offset = [0,0,0,0]
cells = [0, 0, 0, 0, 0]

# This function will go through each column and check if the sum in each is 42.
def check():
    column = 0
    while column < 12:
        for i in range(4):
            cellfound = False
            layer = i
            additional = 0
            while cellfound is False:
                cells[i] = rotors[i + additional][additional][(column - offset[i + additional]) % 12]
              
                if cells[i] != 0:
                    cellfound = True
                else: 
                    if layer + additional == 3:
                        cells[i] = rotors[4][additional][(column) % 12]
                        cellfound = True
                    else:
                        additional = additional + 1
        column = column + 1
        if sum(cells) != 42:
            if column > 4:
                print("FAIL: " + str(column))
            return False
        elif column == 11:
            print(offset)
            return True
                    
# Increments the offset 
def increment():
    offset[0] += 1
    if offset[0] == 12:
        offset[0] = 0
        offset[1] = offset[1] + 1
    if offset[1] == 12:
        offset[1] = 0
        offset[2] = offset[2] + 1
    if offset[2] == 12:
        offset[2] = 0
        offset[3] = offset[3] + 1
        


# Run through
solutionfound = False
while solutionfound is False:
    a = check()
    if (offset[3] == 14):
        # Something is wrong with the code lol
        print("uhoh")
        exit()
    if a is True:
        solutionfound = True
    else:
        increment()