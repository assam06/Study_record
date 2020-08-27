import requests

indeed_result = requests.get("https://kr.indeed.com/python%EC%A7%81-%EC%B7%A8%EC%97%85")
# 1. indeed의 url를 파이썬의 라이브러리 중 requests로 갖고옴
print(indeed_result.text) 
# 2. 그리고 html 추출