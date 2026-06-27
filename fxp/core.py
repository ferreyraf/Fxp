import fxp.tools as tls
from colorama import Fore, Style, init
init(autoreset=True)


def int2fxp(
        Value   : int ,      #  Valor de entrada
        Signed  : int ,      #  Signed = 0 -> Numero no signado , Signed = 1 -> Numero signado
        NB_in   : int ,      #  Cantidad de numeros enteros de la representacion inicial
        NBF_in  : int ,      #  Cantidad de numeros fraccionarios de la representacion inicial
        NB_out  : int ,      #  Cantidad de numeros enteros de la representacion final
        NBF_out : int ,      #  Cantidad de numeros fraccionarios de la representacion final
        Mod     : int = 0,   #  Modo al cual se desea trabajar la parte fraccionaria, Mod = 0 -> Truncado ||    Mod = 1 -> Redondeo
        show    : int = 1,   #  show = 0 -> no muestra toda la informacion de las operaciones. show = 1 -> Muestra toda la info 
        formate : str = "DEC"#  Formato de salida del numero, DECIMAL,BINARIO,HEXADECIMAL.
    ):

    """
    Convierte un valor en entero equivalente de una representacion a otra teniendo en cuenta lo siguiente
        Value     #  Valor de entrada
        Signed    #  Signed = 0 -> Numero no signado , Signed = 1 -> Numero signado
        NB_in     #  Cantidad de numeros enteros de la representacion inicial
        NBF_in    #  Cantidad de numeros fraccionarios de la representacion inicial
        NB_out    #  Cantidad de numeros enteros de la representacion final
        NBF_out   #  Cantidad de numeros fraccionarios de la representacion final
        Mod       #  Modo al cual se desea trabajar la parte fraccionaria, Mod = 0 -> Truncado ||    Mod = 1 -> Redondeo
        show      #  show = 0 -> no muestra toda la informacion de las operaciones. show = 1 -> Muestra toda la inf
    """

    if (not Signed) and (Value < 0):
        print(Fore.RED + "[ERROR]" + Style.RESET_ALL,f"Valor negativo en número sin signo")
        return
    if (show):
        tls.show_init(Value,NB_in,NBF_in,Mod)

    if (Signed):
        max_pos         =   2*(NB_out-NBF_out)-2*(-NBF_out)
        max_neg         =   -2**(NB_out-NBF_out)

        Result, flag    =   tls.sat_over_signed(Value, NBF_in, max_pos, max_neg, show)          #  Ejecuta Saturacion y detecta Overflow, segun corresponda
        Value_o         =   tls.convert_rp_signed(Result,NBF_in,NBF_out,Mod)         #  Ejecuta Redondeo o Saturacion, segun corresponda
    else:
        max_pos = 2**(NB_out)-1                                                  #  Rango representable sin signo 0 - max_pos
        Result, flag = tls.sat_over_usigned(Value, max_pos, show)
        Value_o = tls.convert_rp_usigned(Result, NBF_in, NBF_out, Mod) 
    if show:
        Value_o_tmp = Value_o
        
        if formate == "DEC" :
            print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Valor convertido final formato DEC: {Value_o}")
        elif formate == "BIN":
            Value_o = tls.dec2bin(Value_o_tmp,NB_out)
            print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Valor convertido final formato BIN: {Value_o}")
        elif formate == 'HEX':
            Value_o = tls.dec2hex(Value_o_tmp,NB_out)
            print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Valor convertido final formato HEX: {Value_o}")
    