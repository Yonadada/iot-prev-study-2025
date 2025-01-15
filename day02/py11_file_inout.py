# 파일 입.출력 

# 쓰기
# a 는 (추가), r (읽기), w (쓰기)
#open() 파일을 만들어주는 함수 

f = open('./day02/textfile.txt', mode='w', encoding='utf-8')
#아무것도 안함
f.write('저는 호주사람입니다\n')
f.write('성별은 안 알랴줌\n')
f.close()

print('Success New textfile')


## 읽기
f = open('./day02/textfile.txt', mode='r', encoding='utf-8')

while True :
    line = f.readline() #한줄 씩 읽고 
    if not line: break  # 읽을 줄이 없으면 반복문 탈출

    print(line)

f.close()