# --------------------------------
# 셀레니움 사용처
# 1. 단순 반복 웹 업무를 자동화하고 싶을 때
# 2. 구조가 어려운 사이트를 크롤링 하고 싶을 때

# * 변경사항
    # 1. 셀레니움 설치시 pip install selenium==4.11.2 이걸로 설치합시다 
    # 2. 크롬드라이버 115버전부터는 다운로드 후 압축풀면 이상한 파일이 많이 생기는데
# 그거 전부 파이썬 파일 옆에 놓으면 됩니다.

    # 3. 처음 셋팅하는 코드 작성시
    # driver = webdriver.Chrome('chromedriver.exe') 말고 
    # driver = webdriver.Chrome() 사용합시다. 

# 파이썬을 이용하시면
# 인스타그램에 자동으로 로그인해서 원하는 페이지로 이동한 후 
# 이미지를 싸그리 수집하거나 자동으로 댓글, 좋아요를 남기는 봇을 만들 수 있습니다. 
# 인스타 팔로워수 늘리려고 "와 정말 좋은 정보네요~" 이렇게 무성의한 댓글쓰는 시간을 줄일 수 있겠네요. 
# 근데 우리는 그보다 유용한 이미지 수집을 해보도록 합시다.
# 딥러닝용 개 고양이 사진 수집할 때 이만한 곳이 없습니다. 

#--------------------------------
# 셀레니움 세팅

# 1. chromedriver를 구글에 검색해 내 os에 맞는 파일을 다운받습니다.

# 진행 중에 에러가 뜨거나 안되면 내 크롬 버전과 동일한 버전을 다운받으십시오. 
# 크롬버전 확인하려면 크롬 브라우저 주소창에 chrome://version 쳐보시면 됩니다. 
# 다운받아서 압축풀면 파일이 좀 많이 나오는데 내 파이썬 파일과 같은 공간에 넣어두시면 됩니다.


# 2. 셀레니움을 설치합니다. 

# pip install selenium==4.11.2
# 터미널에 입력하십시오. 

 

 

# 3. 다음 코드를 입력하면 시작할 준비가 끝입니다. 

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys 
# import time

# driver = webdriver.Chrome()
# 파이썬 파일에 입력하시길 바랍니다. 

# 크롬드라이버 115버전, selenium 4.11버전 이후 부터는 chromedriver.exe 라고 경로 입력 안해도 됩니다. 


# --------------------------------
# 셀레니움은 웹 브라우저를 자동으로 제어하는 라이브러리입니다.

# 원래 웹개발할 때 로그인 기능 잘 되는지 글발행 잘 되는지 테스트해보는 작업이 필요합니다. 
# 테스트할 때마다 직접 입력하기 귀찮아서 자동화하려고 나온 라이브러리가 셀레니움입니다.
# 하지만 사람들이 데이터수집에 활용하기 시작했습니다. 

# - 기존 requests + bs4 만으로 수집하기 어려웠던 이상한 구조의 사이트들,
# - ajax라는게 많이 들어간 사이트들
# - 로그인이 필요한 사이트들을 수집할 때 유용합니다.

# 셀레니움 주요 사용법 몇개 

# 원하는 URL 접속 & 이동 

# driver.get('https://instagram.com')
 
# 원하는 요소 찾기

# driver.find_element_by_css_selector('.class명')
# driver.find_element_by_css_selector('#id명')
# driver.find_element_by_css_selector('태그명[속성이름="속성명"]')

# css_selector 뭐시기가 안되면 이런 것도 가능합니다. 

# driver.find_element(By.CSS_SELECTOR,'.class명')
# driver.find_element(By.CSS_SELECTOR,'#id명')
 
# 같은 class명이 매우 여러개 있을 경우 그 중 X번째 등장하는 요소를 찾고 싶은 경우 

# driver.find_elements_by_css_selector('.class명')[X]
# driver.find_elements(By.CSS_SELECTOR, '.class명')[X] #위 문법이 안될 경우
 
# 원하는 요소 안에 있는 글자 가져오기 

# driver.find_element_by_css_selector('.class명').text
# driver.find_element(By.CSS_SELECTOR, '.class명').text #위 문법이 안될 경우
 

# 명령 끝나고나서 브라우저 자동으로 꺼지는거 방지하려면

# import time
# time.sleep(1000000) #코드 맨 마지막에 추