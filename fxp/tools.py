import math as mh
from colorama import Fore, Style, init
init(autoreset=True)
# Flag que indica para que lado satura el resultado
def sat_over_signed(Value : int,nbf : int , max : int, min : int, show : int = 0):
    """
    Esta funcion analiza si el numero en la representacion inicial
    puede ser representado correctamente en la representacion 
    final, esto es importante para evitar valores erroreneos de 
    salida debido al overflow. En este caso, se detecta el overflow
    y se aplica saturacion, ya sea positiva o negativa
    """
    Value_tmp = Value*2**(-nbf)
    # print(Value_tmp,max,min)
    if Value_tmp > max:
        flag = 1
        if show == 1 :
            print(Fore.YELLOW + "[WARM]" + Style.RESET_ALL,f"Se produce overflow positivo {max}")
        Value = max
    elif Value_tmp < min :
        flag = -1
        if show == 1 :
            print(f"#   [WARM]    Se produce overflow negativo {min}")
            print(Fore.YELLOW + "[WARM]" + Style.RESET_ALL, f"Se produce overflow negativo {min}")
        Value_tmp = min
    else :
        flag = 0
        if show == 1 :
            print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, "No hay overflow")
    return Value_tmp, flag

def sat_over_usigned(Value: int, max: int, show: int = 0):
    """
    Controla el overflow para números sin signo.
    Saturación: [0, max]
    """
    if Value > max:
        flag = 1
        if show:
            print(Fore.YELLOW + "[WARM]" + Style.RESET_ALL,f"Se produce overflow positivo {max}")
        Value = max
    elif Value < 0:
        flag = -1
        if show:
            print(Fore.YELLOW + "[WARM]" + Style.RESET_ALL,f"Underflow (valor negativo en unsigned), se fuerza a 0")
        Value = 0
    else:
        flag = 0
        if show:
            print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,f" No hay overflow")
    return Value, flag

# Representa todos los datos de informacion de partida
def show_init(Value : int ,NB_input : int, NBF_input : int, Mode : int):    
    """
    Visualiza de forma ordenada los valores de entrada del numero a convertir
    """        
    print(f"=================================================================")
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Informacion de Partida")  
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Representacion S({NB_input},{NBF_input})")
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Rango entero equivalente {-2**(NB_input-1)} a {2**(NB_input-1)-1}")
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL, f"Rango REAL equivalente {-2**(NB_input-NBF_input-1)} a {2**(NB_input-NBF_input-1)-2**(-NBF_input)}")

    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,f"Valor Inicial en entero equivalente {Value}")
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,f"Valor REAL  equivalente {Value*(2**-NBF_input)}")
    print(f"=================================================================")
    if Mode == 0:
        print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,f"Aplica Truncado")
    else :
        print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,f"Aplica Redondeo   ")
    print(f"=================================================================")

# Representa todos los datos de informacion de salida
def show_done():           
    pass

def convert_rp_signed(Val_q : int , NBF_input : int ,NBF_out : int, Mod):
    """
    Convierte un valor fijo signado de NBF_input a NBF_out.
    Mod = 0 → truncado
    Mod = 1 → redondeo aritmético con signo
    """
    # print(f"[convert_rp_signed] {Val_q} {2**(NBF_out)}")
    Val_tmp = Val_q*2**(NBF_out)
    # print(f"[convert_rp_signed] {Val_tmp}, MOD {Mod}")
    if Mod == 0:
        return int(Val_tmp)               #  Esta operacion realiza solo el truncado.
    else:                                 #  Valua el tipo de numero signado + o -
        if Val_tmp >=0 :                     
            return int(Val_tmp +0.5)
        else:
            return int(Val_tmp -0.5)

def convert_rp_usigned(Val_q : int , NBF_input : int ,NBF_out : int, Mod):
    """
    Convierte un valor fijo sin signo de NBF_input a NBF_out.
    Mod = 0 → truncado
    Mod = 1 → redondeo aritmético con signo
    """
    Val_q = 2*(-NBF_input)*2**(NBF_out)
    diff = Val_q - int(Val_q)             #  Diferencia positiva 
    if Mod == 0:
        return int(Val_q)                 #  Esta operacion realiza solo el truncado.
    else:                                 #  Valua el tipo de numero signado + o -
        if diff >=0.5 :                     
            return mh.ceil(Val_q)
        else:
            return mh.floor(Val_q)
        

def dec2hex(value, nbits):
    """
    Convierte un número entero (positivo o negativo)
    a su representación hexadecimal de nbits bits (complemento a 2).
    """
    mask = (1 << nbits) - 1             # Aplicar máscara para mantener solo nbits
    val_masked = value & mask

    # Calcular la cantidad de dígitos hex necesarios
    n_hex_digits = (nbits + 3) // 4     # redondea hacia arriba cada 4 bits

    # Formatear a hexadecimal con ceros a la izquierda
    return format(val_masked, f'0{n_hex_digits}X')


def dec2bin(value, nbits):
    """
    Convierte un decimal (positivo o negativo)
    a binario con nbits bits en complemento a 2,
    separando cada 4 bits con un '_'.
    """
    mask = (1 << nbits) - 1
    val_masked = value & mask
    bin_str = format(val_masked, f'0{nbits}b')

    # Insertar guiones bajos cada 4 bits (de derecha a izquierda)
    groups = [bin_str[max(i - 4, 0):i] for i in range(len(bin_str), 0, -4)]
    return '_'.join(reversed(groups))

