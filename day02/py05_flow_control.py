# 흐름제어
# if, for, while 

## int(정수화), float(실수화), double(복소수화)
age = int(input('나이를 입력해주세요 > ')) # age 문자열이 입력 30 -> '30'
print(age)

## if 문이 시작된다는 것을 의미하는 마지막 단어는 콜론 :
if age < 19 :
    # if(흐름제어) 안으로 들어왔다는 의미
    # if 문이 참(True)이면 아래 출력 구문을 실행
    print(age,'안돼 ~ 돌아가~')
elif  age > 60 : 
    # 다른 조건이 필요할 때 (else if) -> 여러번 사용 가능 
    print('아저씨',age,'이면 술먹다 내일 죽을 수도 있어요. 자제하세요')

else :
    #if문이 거짓(False), 아래 출력 구문 실행
    print(age,'세 술 구매 가능하십니다~') 