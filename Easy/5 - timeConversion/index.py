#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    shift = s[8:10]
    
    hour = int(s[0:2])
    minute = int(s[3:5])
    
    if s[0:2] == '12' and shift == 'AM':
        return f'00{s[2:8]}'
    elif s[0:2] == '12' and shift == 'PM':
        return f'{hour}{s[2:8]}'
    elif shift == 'PM':
        return f'{hour + 12}{s[2:8]}'
    elif hour < 10:
        return f'0{hour}{s[2:8]}'
    else:
        return f'{hour}{s[2:8]}'