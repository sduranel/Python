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
    cstr1 = ''
    if num2 == '':
       num = str ( num1 ) + '-' + '00'
    else:
       if len(num2) == 2:
          num32 = int ( num2 ) * factor / 1000
       elif len(num2) == 3:
          num32 = int ( num2 ) * factor / 10000
       elif len(num2) == 4:
          num32 = int ( num2 ) * factor / 100000
       elif len(num2) == 5:
          num32 = int ( num2 ) * factor / 1000000
       elif len(num2) == 6:
          num32 = int ( num2 ) * factor / 10000000
       elif len(num2) == 7:
          num32 = int ( num2 ) * factor / 100000000
       elif len(num2) == 8:
          num32 = int ( num2 ) * factor / 1000000000
       elif len(num2) == 9:
          num32 = int ( num2 ) * factor / 10000000000
       else:
          num32 = int ( num2 ) * factor / 100


       cstr1 = str(num32)
       if num32 < 1 or num32 > 1:
          num   = str ( num1 ) + '-' + str(cstr1[0]) + str(cstr1[2])
       elif num32 == 1:
          num = str ( num1 )
       else:
          num = str ( num1 ) + '-' + str ( num32 )
        # num   = str ( num1 ) + '-' + str ( int(num32) )
    return num

print ( thirty_convert     ( '100-16', 32 ) )
print ( thirty_convert     ( '100-01', 32 ) )
print ( thirty_convert     ( '100-01', 256 ) )
print ( thirty_convert     ( '100-16', 64 ) )

print ( thirty_dec_convert ( '100.50', 32 ) )
print ( thirty_dec_convert ( '100.03125', 32 ) )
print ( thirty_dec_convert ( '100.00390625', 256 ) )
print ( thirty_dec_convert ( '100.25', 32 ) )
print ( thirty_dec_convert ( '100.25', 64 ) )
print ( thirty_dec_convert ( '100.25', 256 ) )
print ( thirty_dec_convert ( '101', 32 ) )
