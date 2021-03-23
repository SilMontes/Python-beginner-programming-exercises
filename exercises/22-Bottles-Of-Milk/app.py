def number_of_bottles():
    for i in range(99,0,-1):
        if i!=0 and i!=1:
            print(str(i)+" bottles of milk on the wall, "+str(i)+" bottles of milk. Take one down and pass it around, "+str(i-1)+" bottles of milk on the wall.")
        else:
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\nNo more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")


number_of_bottles()    