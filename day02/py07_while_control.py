# for문과 동일

# 첫번재 예시
loop = 10
while loop > 0 : #loop 변수값이 0 보다 큰 동안 계속 
    # loop >= 0 은 출력값이 0까지 출력
    print(loop, end='\t')
    loop = loop -1

print()

# 두번째 예시
# 위의 while과 같은 출력
for i in range(10,-1,-1):
    print(i, end='\t')

print()
    
#세번째 예시
#무한반복
num = 0
while True:
    print('Hello',num)
    num = num + 1 
