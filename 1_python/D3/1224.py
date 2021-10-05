# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
# 10
# 123 1
# 2737 1
# 757148 1
# 78466 2
# 32888 2
# 777770 5
# 436659 2
# 431159 7
# 112233 3
# 456789 10
# def dfs(cnt, idx):
#     global answer
#     if cnt == 0:
#         result = int(''.join(nums))
#         if answer < result:
#             answer = result
#         return
    
#     for i in range(idx, n-1):
#         for j in range(i+1, n):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 dfs(cnt-1, i)
#                 nums[i], nums[j] = nums[j], nums[i]

# for tc in range(1, int(input())+1):
#     num, change = input().split()
#     nums = list(num)
#     change = int(change)
#     n = len(nums)
#     answer = 0
#     dfs(change, 0)
#     if answer == 0:
#         if change%2:
#             nums[-1], nums[-2] = nums[-2], nums[-1]
#             answer = ''.join(nums)
#         else:answer = ''.join(nums)
#     print('#{} {}'.format(tc, answer))


# # 10개의 테스트케이스 중 9개가 맞았습니다.
# def dfs(cnt, idx):
#     global answer
#     if cnt == 0:
#         result = int(''.join(nums))
#         if answer < result:
#             answer = result
#         return
    
#     for i in range(idx, n-1):
#         for j in range(i+1, n):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 dfs(cnt-1, i)
#                 nums[i], nums[j] = nums[j], nums[i]

# for tc in range(1, int(input())+1):
#     num, change = input().split()
#     nums = list(num)
#     change = int(change)
#     n = len(nums)
#     if n <= 2:
#         if change % 2:answer=''.join(nums[::-1])
#         else:answer=''.join(nums)
#     else:
#         answer = 0
#         dfs(change, 0)
#     print('#{} {}'.format(tc, answer))


# # 오답 : 10개의 테스트케이스 중 6개가 맞았습니다.
# # 중복수 처리 필요
# for tc in range(1, int(input())+1):
#     num, change = input().split()
#     nums = list(num)
#     change = int(change)
#     n = len(nums)
#     idx, cnt = 0, 0
#     while cnt<change:
#         if idx == n-1:
#             if (change-cnt)%2 == 0:
#                 nums[-1], nums[-2] = nums[-2], nums[-1]
#                 break
#             else:break
#         max_num = nums[idx]
#         for i in range(idx+1, n):
#             if nums[i] >= max_num:
#                 max_num = nums[i]
#                 max_idx = i
#         if nums.count(max_num) >= change-cnt:
#             pass
        
#         if nums[idx] == max_num:
#             idx += 1
#             continue
#         elif nums[idx] < max_num:
#             nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
#             idx += 1
#             cnt += 1
#     print('#{} {}'.format(tc, ''.join(nums)))

# # 오답 : 10개의 테스트케이스 중 7개가 맞았습니다.
# def dfs(cnt):
#     global answer
#     if cnt == 0:
#         result = int(''.join(nums))
#         if answer < result:
#             answer = result
#         return
    
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 chk = ''.join(nums)
#                 if not visited.get((chk, cnt-1)):
#                     visited[(chk, cnt-1)] = 1
#                     dfs(cnt-1)
#                 nums[i], nums[j] = nums[j], nums[i]

# for tc in range(1, int(input())+1):
#     num, change = input().split()
#     nums = list(num)
#     n = len(nums)
#     answer = 0
#     visited = {}
#     dfs(int(change))
#     print('#{} {}'.format(tc, answer))

# # 너무 오래 걸려...
# def dfs(cnt):
#     global answer
#     if cnt == 0:
#         result = int(''.join(nums))
#         if answer < result:
#             answer = result
#         return
    
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 dfs(cnt-1)
#                 nums[i], nums[j] = nums[j], nums[i]

# for tc in range(1, int(input())+1):
#     num, change = input().split()
#     nums = list(num)
#     max_ans = int(''.join(sorted(nums, reverse=True)))
#     n = len(nums)
#     answer = 0
#     dfs(int(change))
#     print('#{} {}'.format(tc, answer))