def print_matrix(li):
    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] != 0 and li[i][j] != ' ':
                print("*",end = " ")
            else:
                print(" ",end = " ")
        print("")
        
    print("")
#end of program