def thirty_convert(num, factor):
    num2  = num[4:]
    num1  = num[0:3]
    num32 = int ( num2 ) / factor
    if num32 == 0:
       return num1
    elif num32 == 1:
       return int ( num1 ) + int ( num32 )
    else:
       return int ( num1 ) + num32


def thirty_dec_convert(num, factor):
    num2  = num[4:]
    num1  = num[0:3]
    if num2 == '':
       num32 = factor
    else:
       num32 = int ( num2 ) * factor / 100
    num   = str ( num1 ) + '-' + str ( int(num32) )
    return num

print ( thirty_convert     ( '100-16', 32 ) )
print ( thirty_dec_convert ( '101', 32 ) )
