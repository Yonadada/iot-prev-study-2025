# iot-prev-study-2025
2025 iot 개발자과정 선행 학습

## 1일차
- 기본 과정 설명 및 개발환경 설정, Python 기본 학습

### 과정소개

### 개발환경 설치(IDE)

#### 깃허브 사용법
- remote repository 생성
- 깃허브 테스크탑 local repository로 클론
- local에서 작성 후 commit
- remote로 푸시(**Push**)
- 다른 사용자가 리모트에 있는 최신 내용을 풀(`Push`)
* 파일에 내용이 없다면 (**Commit&Push**)를 했을 때 해당 파일은 git에 올라가지 않는다




### Markdown 학습

#### What is the Markdown?
- Markdown은 Webpage에 리포팅을 하기 위한 마크업 언어
    *주요사용처( 위키피디아, 나무위키, 깃허브, 주피터노트북 등...)
    *문법이 간단하고 쉽게 배울 수 있다.
    *표준이 없는 것이 단점

1. 번호목록 
    1. 첫번째 목록
    2. 두번째 목록
        1. 두번째 하위 목록 1
        2. 두번째 하위 목록 2 
        - 일반 목록 
            

#### 기본 문법(제목 5)
- 링크 사용법
[네이버](https://www.naver.com)

- 이미지 사용법
![귀여운곰돌이이](https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/cnoC/image/0FLb5BJ8prwjPqpPVzqxfpfRpuU)

- HTML 이미지 방법(이미지 크기 조정)
<img src="https://ssl.pstatic.net/melona/libs/1522/1522020/aa5b48b7e7f7e1e6d44c_20250109174152630.jpg" width="300">


##### addInfo(제목 6)
- 추가사항입니다.

### Python 학습 

#### Python?
- 귀도 반 로썸이 1990년경에 개발한 초간단 인터프리터 프로그래밍 언어이다.

##### 파이썬 특징
- 컴파일러 언어(exe 실행 파일이 생성되는 언어)가 아닌 .py 파일로 바로 실행 할 수 있는 
인터프리터 언어

- 객체지향언어(Object Oriented Programming)
- 사용자에게 쉬운 언어(진입 장벽이 낮음)
- 프로그래머가 아닌 과학자들도 쉽게 프로그램 계발에 참여
- https://www.tiobe.com/tiobe-index/ 에서 2020년 이후 1위 고수
- 빅데이터분석, 인공지능, 웹개발 등 다양한 분야 활용

##### 파이썬 설치
- Install Now 설치하면 안된다! Customize installation으로 설치
- Add Python.ext to path는 체크
- install python #.## for all users 체크
- customize install location 에서 슬래시 부터 경로 복사
- dev 밑에 Lang 파일 새로 만들어서 경로 Lang\Python31법


## 2일차
- 파이썬 문법

### 문법학습 순서
1. 변수
    - 파이썬에서는 입력 수 크기의 제약이 없다
2. 데이터 타입 
3. 입출력 - 파일 입출력 포함
    - 한국어만 (ANSI/EUC-KR/`CP949`) 와 국제통용(UTF - 8) 인코딩 주의!
4. 연산자: + , -, *, /, //, %, **
5. 흐름제어
    1. if 문
        - 단일 if, if - else, if - elif - else
    2. for 문 - 프로그래밍 꽃
    3. while 문 - for문과 동일
6. 함수
7. 객체지향, 클래스 
8. 모듈, 패키지
9. 예외처리 
10. 디버깅 


## 3일차
1. 주소록 프로그램 만들기
2. 예외(Exception -> Error)
    - 오류 => 문법 상의 에러
    - 예외 => 실행 중 발생하는 에러
    
3. 디버깅(Debugging)
    - F5 : 디버깅 시작 
    - F10 : 한 줄 실행
    - F11 : 함수, 클래스 등 내부구조 안으로 진입
    - F9 : 브레이크 포인트 토글 
    - Shift + F5 : 종료


4. 디버깅 순서
    1. 예외가 발생할 것 같은 코드 위치 그 이전에 F9로 BP(break point)를 토글
    2. F5 디버깅 시작 
    3. 필요시 F10, F11을 번갈아 사용하면서 한 줄씩 코드 체크

