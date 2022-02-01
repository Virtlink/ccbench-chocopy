# ChocoPy library functions
def int_to_str(x: int) -> str:
    digits:[str] = None 
    result:str = ""

    # Set-up digit mapping
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Write sign if necessary
    if x < 0:
        result = "-"
        x = -x

    # Write digits using a recursive call
    if x >= 10:
        result = result + int_to_str(x // 10)
    result = result + digits[x % 10]
    return result

def int_to_str2(x: int, x2: int) -> str:
    digits:[str] = None 
    digits2:[str] = None 
    result:str = ""
    result2:str = ""

    # Set-up digit mapping
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Write sign if necessary
    if x < 0:
        result = "-"
        x = -x

    # Write digits using a recursive call
    if x >= 10:
        result = result + int_to_str(x // 10)
    result = result + digits[x % 10]
    return result

def int_to_str3(x: int, x2: int, x3: int) -> str:
    digits:[str] = None 
    digits2:[str] = None 
    digits3:[str] = None 
    result:str = ""
    result2:str = ""
    result3:str = ""

    # Set-up digit mapping
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Write sign if necessary
    if x < 0:
        result = "-"
        x = -x

    # Write digits using a recursive call
    if x >= 10:
        result = result + int_to_str(x // 10)
    result = result + digits[x % 10]
    return result
    
def int_to_str4(x: int, x2: int, x3: int, x4: int) -> str:
    digits:[str] = None 
    digits2:[str] = None 
    digits3:[str] = None 
    digits4:[str] = None 
    result:str = ""
    result2:str = ""
    result3:str = ""
    result4:str = ""

    # Set-up digit mapping
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Write sign if necessary
    if x < 0:
        result = "-"
        x = -x

    # Write digits using a recursive call
    if x >= 10:
        result = result + int_to_str(x // 10)
    result = result + digits[x % 10]
    return result

def int_to_str5(x: int, x2: int, x3: int, x4: int, x5: int) -> str:
    digits:[str] = None 
    digits2:[str] = None 
    digits3:[str] = None 
    digits4:[str] = None 
    digits5:[str] = None 
    result:str = ""
    result2:str = ""
    result3:str = ""
    result4:str = ""
    result5:str = ""

    # Set-up digit mapping
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Write sign if necessary
    if x < 0:
        result = "-"
        x = -x

    # Write digits using a recursive call
    if x >= 10:
        result = result + int_to_str(x // 10)
    result = result + digits[x % 10]
    return result

def str_to_int(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True

    # Parse digits
    for char in x:
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign


def str_to_int2(x: str, x2: str) -> int:
    result:int = 0
    result2:int = 0
    digit:int = 0
    digit2:int = 0
    char:str = ""
    char2:str = ""
    sign:int = 1
    sign2:int = 1
    first_char:bool = True
    first_char2:bool = True

    # Parse digits
    for char in x:
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign

def str_to_int3(x: str, x2: str, x3: str) -> int:
    result:int = 0
    result2:int = 0
    result3:int = 0
    digit:int = 0
    digit2:int = 0
    digit3:int = 0
    char:str = ""
    char2:str = ""
    char3:str = ""
    sign:int = 1
    sign2:int = 1
    sign3:int = 1
    first_char:bool = True
    first_char2:bool = True
    first_char3:bool = True

    # Parse digits
    for char in x:
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign

def str_to_int4(x: str, x2: str, x3: str, x4: str) -> int:
    result:int = 0
    result2:int = 0
    result3:int = 0
    result4:int = 0
    digit:int = 0
    digit2:int = 0
    digit3:int = 0
    digit4:int = 0
    char:str = ""
    char2:str = ""
    char3:str = ""
    char4:str = ""
    sign:int = 1
    sign2:int = 1
    sign3:int = 1
    sign4:int = 1
    first_char:bool = True
    first_char2:bool = True
    first_char3:bool = True
    first_char4:bool = True

    # Parse digits
    for char in x:
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign

def str_to_int5(x: str, x2: str, x3: str, x4: str, x5: str) -> int:
    result:int = 0
    result2:int = 0
    result3:int = 0
    result4:int = 0
    result5:int = 0
    digit:int = 0
    digit2:int = 0
    digit3:int = 0
    digit4:int = 0
    digit5:int = 0
    char:str = ""
    char2:str = ""
    char3:str = ""
    char4:str = ""
    char5:str = ""
    sign:int = 1
    sign2:int = 1
    sign3:int = $INT
    sign4:int = 1
    sign5:int = 1
    first_char:bool = True
    first_char2:bool = True
    first_char3:bool = True
    first_char4:bool = True
    first_char5:bool = True

    # Parse digits
    for char in x:
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign
        
# Input parameters
c:int = 42
c2:int = 42
c3:int = 42
c4:int = 42
c5:int = 42
n:int = 10
n2:int = 10
n3:int = 10
n4:int = 10
n5:int = 10

# Run [-nc, nc] with step size c
s:str = ""
s2:str = ""
s3:str = ""
s4:str = ""
s5:str = ""
i:int = 0
i2:int = 0
i3:int = 0
i4:int = 0
i5:int = 0
i = -n * c

# Crunch
while i <= n * c:
    s = int_to_str(i)
    print(s)
    i = str_to_int(s) + c

