# 모듈

import py10_function as calc

calc.multiple(10,4)

# 수학 함수를 편하게 사용할 수 있도록 모아둔 모듈 
import math

result = math.pow(2,10)
print(result)

result = math.log2(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests
import requests

res = requests.get('https://www.naver.com') # naver 사이트를 접속하라
print(res.status_code)#200

print(res.content)