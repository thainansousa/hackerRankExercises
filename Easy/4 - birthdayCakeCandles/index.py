#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    rept = 0
    count = 0

    # Verify child more old
    for i in candles:
        if i > rept:
            rept = i
    
    # Sum how many times old child appear in the list
    for i in candles:
        if i == rept:
            count += 1
            
    return count