#별찍기

## 문자열에 사용할 수 있는 연산자는 + , * 

## for문을 사용해서 콘솔에 아래와 같이 나오도록 구현하세요
        

a = 5
for i in range(5):
    print(' ' * ((a-1) - i), end='')
    print('*' * (i+1))


# b = 10 
# for i in range(10):
#     for j in range(10):

#     print(' ' * ((b-1) -i), end='')

#     print('*' * (i+1))