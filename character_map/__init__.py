# Making dict that compiles all lists of character maps

#importing 'A','B','C' and'1'
__all__ = ['map_of_letters']

from .map_1 import array_A ,array_B, array_C ,array_1

#importing importing 'D','E','F' and '2'

from .map_2 import array_D
from .map_2 import array_E
from .map_2 import array_F
from .map_2 import array_2

#importing 'G','H','I' and '3'

from .map_3 import array_g
from .map_3 import array_h
from .map_3 import array_i
from .map_3 import array_3

#importing 'J','K','L' and '3'

from .map_4 import array_J
from .map_4 import array_K
from .map_4 import array_L
from .map_4 import array_4

#importing 'M','N','O' and '4'

from .map_5 import array_m
from .map_5 import array_n
from .map_5 import array_o
from .map_5 import array_5

#importing 'P','Q','R' and '5'

from .map_6 import Array_p
from .map_6 import Array_q
from .map_6 import Array_r
from .map_6 import Array_6

#importing 'S','T','U' and '7'

from .map_7 import array_S
from .map_7 import array_T
from .map_7 import array_U
from .map_7 import array_7


#importing 'V','W','X' and '8'

from .map_8 import array_V
from .map_8 import array_W
from .map_8 import array_X
from .map_8 import array_8

#importing '!','y','z' and '9'

from .map_9 import Array_excm
from .map_9 import Array_y
from .map_9 import Array_z
from .map_9 import Array_9

#importing function print_matrix from functions.py
from .functions import print_matrix 

print("imported main package")


map_of_letters = {'A':array_A,'B':array_B,'C':array_C,'1':array_1,
                  'D':array_D,'E':array_E,'F':array_F,'2':array_2,
                  'G':array_g,'H':array_h,'I':array_i,'3':array_3,
                  'J':array_J,'K':array_K,'L':array_L,'4':array_4,
                  'M':array_m,'N':array_n,'O':array_o,'5':array_5,
                  'P':Array_p,'Q':Array_q,'R':Array_r,'6':Array_6,
                  'S':array_S,'T':array_T,'U':array_U,'7':array_7,
                  'V':array_V,'W':array_W,'X':array_X,'8':array_8,
                  'Y':Array_y,'Z':Array_z,'!':Array_excm ,'9':Array_9}


print("intialized character mapping")
if __name__ == '__main__':
      s = "hello"
      for letter in list(s.upper()):
            print_matrix(map_of_letters[letter])