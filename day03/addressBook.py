# addressBook.py - 주소록 프로그램 만들기

import contact 
import os # 운영체제에서 사용되는 기능들을 가지고 있는 모듈 


# 4. 연락처를 입력 받는 함수 생성
def set_address():
    try:
        name, phone, email, addr = input('정보입력(이름, 연락처, 이메일, 주소): ').split(',') 
        
    # print(name, phone, email, addr)
    #7. contact 객체 생성, 리턴
        address = contact.Contact(name, phone, email, addr)
        return address # Contact 객체 리턴
    except ValueError:
        print('데이터를 정확히 입력하세요 ')
        return None # 아무것도 아닌것




# 10. 연락처 출력 
def get_address(lst_contact): # run에 있는 lst_contact와 get_address의 lst_contact는 다르다
    for item in lst_contact:
        print(item)    


# 11. 연락처 삭제
# 12. 연락처 삭제 함수 변경, 삭제 여부 리턴
def del_address(last_contact, name):
    result = False #아무것도 삭제 안했음 

    for i, item in enumerate(last_contact): #enumerate -> 각 객체에 번호를 매겨주는 클래스
        if item.isNameExist(name):
            del last_contact[i] # del 메모리에서 영구 삭제 
            result = True # 지워졌음

    return result # 삭제여부 반환 



# 8. 콘솔화면 클리어 함수
def clear_console():
    command = 'clear' # LINUX, UNIX 클리어 명령어
    if os.name in ('nt', 'dos'): # 운영체제가 윈도우
        command = 'cls' # Windows 클리어 명령어

    os.system(command) #콘솔에 명령어 실행



# 14. 파일 DB 저장 함수
def save_contact (lst_contact):
    f = open('./day03/address_db.txt', mode='w',encoding='utf-8')

    for item in lst_contact:
        f.write(item.getName() + '/' )
        f.write(item.getPhone() + '/' )
        f.write(item.getEmail() + '/' )
        f.write(item.getAddr() + '\n' )

    f.close() # 파일을 열었으면 반드시!!!!! 닫아줘야함 -> 메모리를 차지하면 성능이 저하된다..


# 15. 파일DB 로드 함수 
def load_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='r',encoding='utf-8')
    
    while True:
        line = f.readline() # 홍여원/010/naver/부산 -=> 한줄 씩 읽어옴
        
        if not line:
            break # 줄에 아무글도 없으면 빠져나감 
        
        #25.01.16  15:52 
        # \n으로 오류발생, \n을 리스트 저장 전에 삭제해야한다.
        lines = line.replace('\n','').split('/') #lines는 4개의 문자열을 가지는 리스트가 된다
        # 예시
        # lines = ['홍여원','010',... ]
        # lines[0] == '홍여원'

        address = contact.Contact(name=lines[0], phone=lines[1], email=lines[2], addr=lines[3])
        lst_contact.append(address) 

    f.close()

# 5. 프로그램 실행 함수
def run(): 
    # 9. 주소 정보들을 담을 수 있는 변수(리스트)
    lst_contact = [] # 빈 리스트 생성
    load_contact(lst_contact)

    
    # set_address() # set_address() 함수를 실행시키도록 불러온다
    clear_console() #화면 클리어

    while True:
        sel_menu = get_menu()
    
        if sel_menu == 1: # 연락처 추가
            info = set_address()

            if info is None:
                pass
            else:
                lst_contact.append(info) # 9. 주소정보 담기
                print('추가되셨습니다~')
        
            input()

        elif sel_menu == 2: # 연락처 출력
            get_address(lst_contact)
            input()

        elif sel_menu == 3: # 연락처 삭제
            name = input('삭제할 이름 입력: ')
            res = del_address(lst_contact, name)

            if res == True:
                print('정상적으로 삭제 완료 되셨습니다!')
            else:
                print('삭제할 데이터가 없습니다')  
                
            input() # 단순 입력 대기 

        elif sel_menu == 4: # 종료
            save_contact(lst_contact)
            break # 프로그램 종료

        else:
            pass
        
        clear_console()


# 6. 메뉴구성
def get_menu():
    str_menu = (
        '주소록 프로그램 v1.0\n'
        '1. 연락처 추가\n'
        '2. 연락처 출력\n'
        '3. 연락처 삭제\n'
        '4. 종료\n'
    )
    print(str_menu)

    #예외처리 try - except - (finally) 키워드 사용
    try:
        menu_num = int(input('메뉴 입력: '))  # 숫자를 표현하는 문자열
    except Exception:
        print('예외발생!')
        menu_num = 0 # 메뉴와 관계없는 숫자

    return menu_num # 문자열을 정수형으로 형변환




    
# 1. 프로그램 시작 
if __name__ == '__main__':
    # pass , if, for, while 함수 등에서 오류를 없애는 방법
    # print('주소록 프로그램')

    #3.클래스 실행
    # first = contact.Contact('Yonova Hong', '010-4666-5666', 'y0123@gmail.com','Australia')
    # print(first)
    
    # 제일 처음 실행되는 함수 
    run() # run() 작성함으로써, 프로그램 실행될때 run 함수가 실행되도록 호출 /f12 키 눌리면 함수로 이동
        
print('프로그램 종료')

