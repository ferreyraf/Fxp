import fxp.core as fxp
import random as rd
# import inspect # para mostrar lineas en el codigo
import fxp.debug as p

NB_INT1   =   16
NBF_INT1  =   15
NB_INT2   =   16
NBF_INT2  =   15

NB_OUT    =   10
NBF_OUT   =    7

Val_a     =   -25159 #rd.randrange(0,2**(NB_INT1-1),1)
Val_b     =   25159  #rd.randrange(0,2**(NB_INT2-1),1)

NB_INT    =   [NB_INT1,NB_INT2]
NBF_INT   =   [NBF_INT1,NBF_INT2]
Val = [Val_a,Val_b]
 
for ii in range(2):
    X = fxp.int2fxp(Val[ii],1,NB_INT[ii],NBF_INT[ii],NB_OUT,NBF_OUT,1,show=1,formate='BIN')