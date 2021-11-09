#def2
#sahil


char_input=input("Enter a character: ")

array_D = [[1,1,1," "," "],
           [1," "," ",1," "],
           [1," "," "," ",1],
           [1," "," "," ",1],
           [1," "," "," ",1],
           [1," "," ",1," "],
           [1,1,1," "," "]]

#[" "]==" "; off LED
#[1]==1; on LED

array_E = [[1,1,1,1,1], 
          [1," "," "," "," ",], 
          [1," "," "," "," ",], 
          [1,1,1,1,1,], 
          [1," "," "," "," ",], 
          [1," "," "," "," ",], 
          [1,1,1,1,1,]]

#[" "]==" "; off LED
#[1]==1; on LED

array_F = [[1,1,1,1,1],
           [1," "," "," "," ",],
           [1," "," "," "," ",],
           [1,1,1,1,1,],
           [1," "," "," "," ",],
           [1," "," "," "," ",],
           [1," "," "," "," ",]]

#[" "]==" "; off LED
#[1]==1; on LED

array_2 = [[" ",1,1,1," "],
           [1," "," "," ",1],
           [" "," "," ",1," "],
           [" "," ",1," "," "],
           [" ",1," "," "," "],
           [1," "," "," "," "],
           [1,1,1,1,1]]

#[" "]==" "; off LED
#[1]==1; on LED

array_continue = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]
                    


#[" "]==" "; off LED
#[1]==1; on LED

for i in range(7):
    for j in range(5):
        if char_input == "D":
            print(array_D[i][j], end=" ")
        elif char_input == "E":
            print(array_E[i][j], end=" ")
        elif char_input == "F":
            print(array_F[i][j], end=" ")
        elif char_input == "2":
            print(array_2[i][j], end=" ")
        else:
            print(array_continue[i][j], end=" ")
    print()

#by- sahilahmed