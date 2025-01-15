# 구구단
# 2단 만들기

for i in range(2,10):
    # print(i)
    for j in range(1,10):
        if j == 9: # break로 인해 j가 9를 곱할때 빠져나옴 
            break

        # print( i * j ) # 값만 출력
        print(i, 'x', j,'=', i*j, end='\t')

    print()