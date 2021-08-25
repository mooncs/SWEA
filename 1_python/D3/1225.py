
# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
# append, pop활용
for _ in range(10):
    tc = int(input())
    pwd = list(map(int, input().split()))
    flag = True
    while flag:
        for i in range(1, 6):
            # 제일 처음 수를 꺼내서 i만큼 감소
            p = pwd.pop(0) - i
            # 감소한 수가 0보다 작거나 같다면
            if p <= 0:
                # 0을 마지막에 추가하고, 반복문 탈출
                pwd.append(0)
                flag = False
                break
            else:
                # 감소한 수가 0보다 크다면, 감소한 수를 마지막에 추가
                pwd.append(p)
    print('#{} {}'.format(tc, ' '.join(map(str, pwd))))
                
################################################################################# 
# # circular queue활용
# # 암호 생성 함수
# def makepwd():
#     # 0부터 시작
#     front = 0
#     flag = True
#     while flag:
#         # 1~5를 조건이 만족할 때까지 계속해서 감소
#         for i in range(1, 6):
#             # 제일 처음 수를 꺼내서 i만큼 감소
#             p = pwd[front] - i
#             # 감소한 수가 0보다 작거나 같다면
#             if p <= 0:
#                 # 그 수는 0으로 만들고
#                 pwd[front] = 0
#                 # 시작 지점을 다음 지점으로 바꾸고, 반복문 탈출
#                 front = (front+1) % len(pwd)
#                 flag = False
#                 break
#             else:
#                 # 감소한 수가 0보다 크다면, 현재 값 갱신하고 시작 지점을 다음 지점으로 갱신
#                 pwd[front] = p
#                 front = (front+1) % len(pwd)
#     return front

 
# for _ in range(10):
#     tc = int(input())
#     pwd = list(map(int, input().split()))

#     front = makepwd()
#     for i in range(front):
#         pwd.append(pwd[i])
    

#     print('#{}'.format(tc), end=' ')
#     for p in pwd[front:]:
#         print(p, end=' ')
#     print()


################################################################################# 
# 굳이 rear는 불필요해서...rear제거  
# # circular queue활용
# # 암호 생성 함수
# def makepwd():
#     # 시작은 0, 끝지점은 7
#     front = 0
#     rear = 7
#     flag = True
#     while flag:
#         # 1~5를 조건이 만족할 때까지 계속해서 감소
#         for i in range(1, 6):
#             # 제일 처음 수를 꺼내서
#             p = pwd[front]
#             # 그 수가 0보다 작거나 같다면
#             if p <= 0:
#                 # 시작지점과 끝지점을 한 칸씩 뒤로
#                 front = (front+1) % len(pwd)
#                 rear = (rear+1) % len(pwd)
#                 flag = False
#                 break
#             else:
#                 # 꺼낸 수가 0보다 크다면 i만큼 감소
#                 p -= i
#                 # 감소한 수가 0보다 작거나 같다면
#                 if p <= 0:
#                     # 그 수는 0으로 만들고
#                     pwd[front] = 0
#                     front = (front+1) % len(pwd)
#                     rear = (rear+1) % len(pwd)
#                     flag = False
#                     break
#                 else:
#                     # 감소한 수가 0보다 크다면 front의 수를 갱신하고 front이동
#                     pwd[front] = p
#                     front = (front+1) % len(pwd)
#                     rear = (rear+1) % len(pwd)
#     return front

 
# for _ in range(10):
#     tc = int(input())
#     pwd = list(map(int, input().split()))

#     front = makepwd()
#     for i in range(front):
#         pwd.append(pwd[i])
    

#     print('#{}'.format(tc), end=' ')
#     for p in pwd[front:]:
#         print(p, end=' ')
#     print()