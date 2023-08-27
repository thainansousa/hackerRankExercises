#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    applesLandAtHouse = 0
    orangesLandAtHouse = 0
    
    # Counter apples positions
    
    for apple in apples:
        appleLandPosition = a + apple
        if appleLandPosition >= s and appleLandPosition <= t:
            applesLandAtHouse += 1
          
    # Counter oranges positions
    
    for orange in oranges:
        orangeLandPosition = b + orange
        if orangeLandPosition >= s and orangeLandPosition <= t:
            orangesLandAtHouse += 1
    
    # Print value of the apples
    print(applesLandAtHouse)
    
    # Print value of the oranges
    print(orangesLandAtHouse)