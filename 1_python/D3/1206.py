# # 1
# # 총 10개의 테스트 케이스
# for tc in range(1, 11):
#     # 총 건물의 수
#     building = int(input())
#     # 건물들의 층 수
#     stories = list(map(int, input().split()))
#     # 조망권 확보세대를 셀 변수 설정
#     views = 0
#     # 제일 처음 2개와 제일 끝 2개는 0층
#     for i in range(2, building-1):
#         # 바로 양 옆 건물들과 비교
#         if stories[i] > stories[i-1] and stories[i] > stories[i+1]:
#             dif1 = stories[i]-stories[i-1] if stories[i]-stories[i-1] < stories[i]-stories[i+1] else stories[i]-stories[i+1]
#             # 두 칸 넘어의 건물들과 비교
#             if stories[i] > stories[i-2] and stories[i] > stories[i+2]:
#                 dif2 = stories[i]-stories[i-2] if stories[i]-stories[i-2] < stories[i]-stories[i+2] else stories[i]-stories[i+2]
#                 # 건물들과의 층수 차이 중 가장 작은 수를 조망권 확보 세대로 더해준다.
#                 view = dif1 if dif1 <= dif2 else dif2
#                 views += view

#     print('#{} {}'.format(tc, views))


# # 1-2
# for tc in range(1, 11):
#     # 총 건물의 수
#     building = int(input())
#     # 건물들의 층 수
#     stories = list(map(int, input().split()))
#     # 조망권 확보세대를 셀 변수 설정
#     views = 0
#     # 제일 처음 2개와 제일 끝 2개는 0층
#     for i in range(2, building-1):
#         if stories[i] > stories[i-1] and stories[i] > stories[i+1] and stories[i] > stories[i-2] and stories[i] > stories[i+2]:
#             dif1 = stories[i]-stories[i-1] if stories[i]-stories[i-1] < stories[i]-stories[i+1] else stories[i]-stories[i+1]
#             dif2 = stories[i]-stories[i-2] if stories[i]-stories[i-2] < stories[i]-stories[i+2] else stories[i]-stories[i+2]
#             views += dif1 if dif1 <= dif2 else dif2
    
#     print('#{} {}'.format(tc, views))


# 2
# 조망권 체크 함수 만들기
def views(building, story):
    # 최종 반환할 변수 정의
    view = 0
    # 체크한 건물의 갯수를 담을 변수 정의
    checked = 2
    # 2~building-2까지의 데이터 비교
    while checked < building-2:
        # 가장 높은 건물의 높이를 담을 변수 정의
        highest = 0
        # 주변 4개의 건물 중에서 가장 높은 건물 구하기
        for i in [checked-2, checked-1, checked+1, checked+2]:
            if story[i]>highest:
                highest = story[i]
        
        # 가장 높은 건물의 높이보다 현재의 건물의 높이가 더 높다면, 두 건물의 높이 차를 조망권 세대로 추가하기
        if story[checked] > highest:
            view += story[checked]-highest
            # 현재의 건물이 가장 높기 때문에, 뒤의 2개의 건물은 체크할 필요가 없어진다.
            checked += 3
        # 현재의 건물이 가장 높지 않다면 다음 건물을 확인해본다.
        else:
            checked += 1
    
    return view

for ts in range(1, 11):
    build = int(input())
    datas = list( map(int, input().split() ) )
    print( '#{} {}'.format( ts, views(build, datas) ) )