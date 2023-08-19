#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    qtdPositiveValues = 0

    qtdNegativeValues = 0

    qtdZeroValues = 0

    for n in arr:

        if n > 0:
            qtdPositiveValues += 1

        elif n < 0:
            qtdNegativeValues += 1

        else:
            qtdZeroValues += 1

    print(f'{(qtdPositiveValues / len(arr)):.6f}')

    print(f'{(qtdNegativeValues / len(arr)):.6f}')

    print(f'{(qtdZeroValues / len(arr)):.6f}')