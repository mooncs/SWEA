for tc in range(10):
    input()
    N = 100
    words_list = [list(input()) for _ in range(N)]
    flag = False
    # 가로의 경우
    width_length = 100
    while width_length > 0 and not flag:
        for i in range(N):
            for j in range(N - width_length + 1):
                for l in range(width_length // 2):
                    if words_list[i][j + l] != words_list[i][j + (width_length - l) - 1]:
                        break
                else:
                    flag = True
                    break  # 회문은 하나밖에 없다고 했으므로
            if flag:
                break
        width_length -= 1
 
    flag = False
    # 세로의 경우
    height_length = 100
    while height_length > 0 and not flag:
        for i in range(N):
            for j in range(N - height_length + 1):
                for l in range(height_length // 2):
                    if words_list[j + l][i] != words_list[j + (height_length - l) - 1][i]:
                        break
 
                else:
                    flag = True
                    break  # 회문은 하나밖에 없다고 했으므로
            if flag:
                break
        height_length -= 1
 
    if height_length > width_length:
        print("#{} {}".format(tc+1, height_length+1))
    else:
        print("#{} {}".format(tc + 1, width_length + 1))



# ???
# def solution(matrix):
#     def get_length_of_longest_palindrome(s):
#         s = '#' + '#'.join(s) + '#'
#         N = len(s)
#         lps_cnt = [0] * N
 
#         r = p = 0
#         for idx in range(N):
#             if idx <= r:
#                 mirror_idx = 2 * p - idx
#                 if lps_cnt[mirror_idx] > r - idx:
#                     lps_cnt[idx] = r - idx
#                 else:
#                     lps_cnt[idx] = lps_cnt[mirror_idx]
 
#             while idx - lps_cnt[idx] - 1 >= 0 and idx + lps_cnt[idx] + 1 < N \
#                     and s[idx - lps_cnt[idx] - 1] == s[idx + lps_cnt[idx] + 1]:
#                 lps_cnt[idx] += 1
 
#             # 회문의 우측 끝이 갱신되었다면, 현재 idx 가 최장 회문의 중심
#             if r < idx + lps_cnt[idx]:
#                 r = idx + lps_cnt[idx]
#                 p = idx
 
#         return max(lps_cnt)
 
#     maximum = 0
#     for row in matrix:
#         lps_cnt = get_length_of_longest_palindrome(row)
#         if lps_cnt > maximum:
#             maximum = lps_cnt
 
#     for y in range(100):
#         for x in range(100):
#             if x > y:
#                 matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
 
#     for col in matrix:
#         lps_cnt = get_length_of_longest_palindrome(col)
#         if lps_cnt > maximum:
#             maximum = lps_cnt
 
#     return maximum
 
# T = 10
 
# for _ in range(T):
#     tc = int(input())
#     matrix = [list(input()) for _ in range(100)]
#     print(f'#{tc} {solution(matrix)}')
