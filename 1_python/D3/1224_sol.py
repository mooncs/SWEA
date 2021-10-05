# # 1
# T = int(input())
 
# for t in range(1, T + 1):
#     nums, cnt = input().split() # num: 숫자, cnt: 교환 횟수
#     nums = list(nums)
#     cnt = int(cnt)
#     org_cnt = cnt
 
#     for i in range(len(nums) - 1):
#         max_idx = i
#         for j in range(len(nums) - 1, i, -1):
#             if nums[j] > nums[max_idx]:
#                 max_idx = j
#         if i != max_idx:
#             nums[i], nums[max_idx] = nums[max_idx], nums[i]
#             cnt -= 1
#         if cnt == 0:
#             break
 
#     duplicated_nums = 0
#     if org_cnt > len(nums):
#         org_cnt = len(nums)
#     for i in range(org_cnt - 1):
#         if nums[i] == nums[i + 1]:
#             duplicated_nums += 1
 
#     for i in range(len(nums) - duplicated_nums - 1, len(nums) - 1):
#         for j in range(i, len(nums)):
#             if nums[i] < nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
 
#     if cnt % 2 and len(nums) == len(set(nums)):
#         nums[-1], nums[-2] = nums[-2], nums[-1]
 
#     print('#{}'.format(t), ''.join(nums))


# # 2
# T = int(input())
 
# for tc in range(1, T+1):
#     N, C = map(int, input().split())
#     S = C
#     sN = str(N)
#     N_list = []
#     for i in sN:
#         N_list.append(int(i))
#     maxN_list = sorted(N_list)
#     p = len(N_list)-1
#     rN_list = N_list[::-1]
#     crN_list = rN_list[:]
#     while S != 0:
#         if rN_list == maxN_list:
#             break
#         maxN = 0
#         for i in range(len(N_list)):
#             if maxN < crN_list[i]:
#                 maxN = crN_list[i]
#         mp = crN_list.index(maxN)
#         rN_list[p], rN_list[mp] = rN_list[mp], rN_list[p]
#         crN_list[p], crN_list[mp] = crN_list[mp], crN_list[p]
#         crN_list[p] = 0
#         if p != mp:
#             S -= 1
#         p -= 1
#     if S % 2 == 1:
#         rN_list[0], rN_list[1] = rN_list[1], rN_list[0]
#     if C >= 2 and rN_list[0] != rN_list[1]:
#         if rN_list[-1] == rN_list[-2]:
#             rN_list[0], rN_list[1] = rN_list[1], rN_list[0]
#     print("#{}".format(tc), end=" ")
#     for i in rN_list[::-1]:
#         print(i, end="")
#     print()

# # 3 수정중....
# # cnt : 바꾼 횟수
# def change(cnt):
#     global ans
#     if cnt == K:
#         ans = max(ans, int(''.join(money)))
    
#     for i in range(len(money)-1):
#         for j in range(i+1, len(money)):
#             money[i], money[j] = money[j], money[i]
#             change(cnt+1)
#             money[i], money[j] = money[j], money[i]
            
# T = int(input())
# for tc in range(1, T+1):
#     money, K = input().split()

#     visited = []

#     money = list(money)
#     K = int(K)

#     ans = 0

#     change(0)

#     print('#{} {}'.format(tc, ans))