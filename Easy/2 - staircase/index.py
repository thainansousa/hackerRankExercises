#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    i = 1
    while n > 0:
        print(f"{' ' * (n - 1)}{'#' * i}")
        n -= 1
        i += 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
