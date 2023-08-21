#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimumValue = arr[0]
    maximumValue = arr[0]
    
    
    sumAllValues = 0
    
    sumMinValues = 0
    sumMaxValues = 0
    
    # Find minimum value of the array
    for idx, i in enumerate(arr):
        if arr[idx] <= minimumValue:
            minimumValue = i
            
        # Sum all values of the array
        sumAllValues += i
        
    # Find maximum value of the array      
    for idx, i in enumerate(arr):
        if arr[idx] >= maximumValue:
            maximumValue = i
    
    # Calculate sum of the minimum values           
    for n in arr:
        sumMinValues += n
        if sumMinValues < sumAllValues:
            sumMinValues = sumMinValues
        else:
            sumMinValues = sumMinValues - maximumValue
            
    # Calculate sum of the maximum values        
    for n in arr:
        sumMaxValues += n
        
        if sumMaxValues < sumAllValues:
            sumMaxValues = sumMaxValues
        else:
            sumMaxValues = sumMaxValues - minimumValue
            
    # Print result
    print(f'{sumMinValues} {sumMaxValues}')
