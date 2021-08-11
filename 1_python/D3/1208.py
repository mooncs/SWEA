# 1208. [S/W 문제해결 기본] 1일차 - Flatten
for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    # 1~100까지의 높이를 나타내는 리스트, index와 맞추기 위해 0부터 시작
    heights = [0]*101
    # 제일 높은 박스 max_box, 제일 낮은 박스 min_box
    max_box = 1
    min_box = 100
    # 해당 높이의 횟수 만큼 더해주고, min/max_box 갱신
    for box in boxes:
        heights[box] += 1
        if box > max_box:
            max_box = box
        if box < min_box:
            min_box = box

    # dump 횟수만큼 실행
    while dump:
        heights[max_box] -= 1
        heights[max_box-1] += 1
        heights[min_box] -= 1
        heights[min_box+1] += 1
        
        # 최대 높이, 최소 높이의 카운트가 0이 되면 한 칸씩 옮겨두기
        if heights[max_box] == 0:
            max_box -= 1
        if heights[min_box] == 0:
            min_box += 1

        dump -= 1

    print('#{} {}'.format(tc, max_box-min_box))



# # 2
# def MyMinMax(nums):
#     min_num = nums[0]
#     max_num = nums[0]
#     for num in nums:
#         if num > max_num:
#             max_num = num
#         elif num < min_num:
#             min_num = num
#     return min_num, max_num
 
# for tc in range(1, 11):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#     min_level, max_level = MyMinMax(boxes)
#     level_cnt = [0] * (max_level - min_level + 1)
 
#     for box in boxes:
#         level_cnt[box - min_level] += 1
 
#     max_level -= min_level
#     min_level = 0
 
#     min_level_cnt = level_cnt[min_level]
#     max_level_cnt = level_cnt[max_level]
 
#     while N >= 0:
 
#         if min_level_cnt > max_level_cnt:
#             N -= max_level_cnt
#             min_level_cnt -= max_level_cnt
#             level_cnt[min_level + 1] += max_level_cnt
#             max_level -= 1
#             max_level_cnt += level_cnt[max_level]
 
#         elif max_level_cnt > min_level_cnt:
#             N -= min_level_cnt
#             max_level_cnt -= min_level_cnt
#             level_cnt[max_level - 1] += min_level_cnt
#             min_level += 1
#             min_level_cnt += level_cnt[min_level]
 
#         else:
#             N -= min_level_cnt
#             min_level += 1
#             max_level -= 1
#             min_level_cnt += level_cnt[min_level]
#             max_level_cnt += level_cnt[max_level]
 
#     print('#{} {}'.format(tc, max_level - min_level + 1))
