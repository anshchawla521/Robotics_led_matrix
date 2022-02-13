def print_matrix(li):
    for i in range(7):
        for j in range(5):
            if li[i][j] == 0:
                print(" ",end = " ")
            else:
                print("*",end = " ")
        print("")
        
    print("")
#end of program