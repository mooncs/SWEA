'''
2056. 연월일 달력

연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
 ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


[입력]
5
22220228
20150002
01010101
20140230
11111111


[출력]
#1 2222/02/28
#2 -1
#3 0101/01/01
#4 -1
#5 1111/11/11
'''
# n = int(input())
# for i in range(1, n+1):
#     date = input()
#     thirtyone = ['01', '03', '05', '07', '08', '10', '12']
#     thirty = ['04', '06', '09', '11']
#     if date[4:6] in thirtyone:
#         if int(date[6:]) < 32:
#             print(f'#{i} ' + date[:4] + '/' + date[4:6] + '/' + date[6:])
#         else:
#             print(f'#{i} -1' )
#     elif date[4:6] in thirty:
#         if int(date[6:]) < 31:
#             print(f'#{i} ' + date[:4] + '/' + date[4:6] + '/' + date[6:])
#         else:
#             print(f'#{i} -1' )
#     elif date[4:6] == '02':
#         if int(date[6:]) < 29:
#             print(f'#{i} ' + date[:4] + '/' + date[4:6] + '/' + date[6:])
#         else:
#             print(f'#{i} -1' )
#     else:
#         print(f'#{i} -1' )

n = int(input())
for i in range(1, n+1):
    date = input()

    y = date[:4]
    m = date[4:6]
    d = date[6:]
    md_match = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if int(m) > 12 or int(m) < 1:
        print(f'#{i} -1')

    else:
        if md_match[int(m)] < int(d) or int(d) < 1:
        # if md_match.get(int(m)) < int(d) or int(d) < 1:
            print(f'#{i} -1')
        else:
            print(f'#{i} ' + y + '/' + m + '/' + d)
