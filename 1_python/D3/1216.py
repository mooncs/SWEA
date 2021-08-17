# 1216. [S/W 문제해결 기본] 3일차 - 회문2
def palindrome_row(arr):
    longest = 1
    for i in range(100):
        for j in range(100):
            for k in range(99, j, -1):
                length = k-j+1
                for l in range(length//2):
                    if arr[i][j+l] != arr[i][k-l]:
                        break
                else:
                    if longest < length:
                        longest = length
    return longest

def palindrome_col(arr):
    longest = 1
    for i in range(100):
        for j in range(100):
            for k in range(99, j, -1):
                length = k-j+1
                for l in range(length//2):
                    if arr[j+l][i] != arr[k-l][i]:
                        break
                else:
                    if longest < length:
                        longest = length
    return longest

for _ in range(10):
    tc = int(input())

    arr = [list(input()) for _ in range(100)]

    max_row = palindrome_row(arr)
    max_col = palindrome_col(arr)

    if max_row > max_col:
        print('#{} {}'.format(tc, max_row))
    else:
        print('#{} {}'.format(tc, max_col))

