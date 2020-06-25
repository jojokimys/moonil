import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

# 네이버 검색 url
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# 검색어 받아와서 searchWord에 저장
searchWord = input('검색어를 입력하세요 : ')

# 한글 검색 자동 변환
url = baseUrl + quote_plus(searchWord)

# 검색어 오픈해서 BeautifulSoup 라이브러리로 파싱
html = urlopen(url)
soup = bs(html, "html.parser")
# 클래스네임에 이미지가 들어간것들만 추출
img = soup.find_all(class_='_img')

# 검색어로 시작되는 폴더가 없으면 생성
if not os.path.exists('./'+searchWord):
    os.mkdir(searchWord)

# 추출된 태그내용으로 이미지 추출 시작
n = 1
for i in img:
    # 이미지의 url 주소 가져오기
    imgUrl = i['data-source']
    print(imgUrl)
    with urlopen(imgUrl) as f:
        # 폴더에 저장
        with open('./'+searchWord+'/' + searchWord + str(n)+'.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

print('다운로드 완료')
