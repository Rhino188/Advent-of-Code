def moveup (y):
    return y - 3
def movedown (y):
    return y + 3
def moveleft (y):
    return y - 1
def moveright (y):
    return y + 1
repeat = 1
print("Enter Last number")
last_number = int (input())
while repeat == 1:
    print("Enter Instructions for password")
    instructions = str(input())
    for x in range(0,(len(instructions))):
        if instructions[x] == "U":
            if last_number >= 4 and last_number <= 9:
                last_number = moveup(last_number)
            else:
                continue
        elif instructions[x] == "D":
            if last_number >= 1 and last_number <= 6:
                last_number = movedown(last_number)
            else:
                continue
        elif instructions[x] == "L":
            if last_number != 1 and last_number != 4 and last_number != 7:
                last_number = moveleft(last_number)
            else:
                continue
        elif instructions[x] == "R":
            if last_number != 3 and last_number != 6 and last_number != 9:
                last_number = moveright(last_number)
            else:
                continue
        else:
            break
    print (last_number)