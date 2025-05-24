import time
# 인스타그램 자동로그인
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import os

# 이미지 저장 폴더 생성
save_dir = 'instagram-images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"'{save_dir}' 폴더가 생성되었습니다.")  # 폴더 생성 안내

# 크롬 드라이버 초기화 (자동으로 드라이버 설치)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://instagram.com')  # 인스타그램 메인 페이지 접속

time.sleep(5)  # 메인 페이지 로딩 대기

# 로그인 입력창 찾기 및 로그인 정보 입력
# 사용자명 입력
e = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
e.send_keys("your_username_sample")
# 비밀번호 입력
e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
e.send_keys("your_password_sample")
# 엔터로 로그인 시도
e.send_keys(Keys.ENTER)

time.sleep(8)  # 로그인 후 페이지 로딩 대기

# 해시태그 검색 페이지로 이동
# (여기서는 '사과' 해시태그)
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
time.sleep(10)  # 해시태그 페이지 로딩 대기

# 첫 번째 게시물(이미지) 클릭
# 게시물 썸네일의 CSS 선택자 사용
driver.find_element(By.CSS_SELECTOR, 'div._aagw').click()
time.sleep(5)  # 게시물 팝업 로딩 대기

# 여러 장 저장 반복 (10장)
max_count = 10
for i in range(max_count):
    # 다양한 이미지 선택자 시도 (버전에 따라 다를 수 있음)
    selectors = [
        'img[style*="object-fit: cover"]',
        'img._aagt',
        'img[alt*="사과"]',
        'div._aagt img',
        'div[role="dialog"] img'
    ]
    img_url = None
    for selector in selectors:
        try:
            img_element = driver.find_element(By.CSS_SELECTOR, selector)
            img_url = img_element.get_attribute('src')
            if img_url:
                print(f"[{i+1}] 이미지 URL을 찾았습니다: {img_url}")
                break
        except:
            continue
    # 이미지 저장
    if img_url:
        response = requests.get(img_url)
        if response.status_code == 200:
            filename = f'instagram_image_{int(time.time())}_{i+1}.jpg'
            filepath = os.path.join(save_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f'[{i+1}] 이미지가 저장되었습니다: {filepath}')
        else:
            print(f'[{i+1}] 이미지 다운로드 실패')
    else:
        print(f'[{i+1}] 이미지 URL을 찾을 수 없습니다')
    # 다음 버튼 클릭 (여러 개 중 마지막 버튼이 실제 '다음'일 확률 높음)
    try:
        time.sleep(2)  # 버튼 활성화 대기
        next_btns = driver.find_elements(By.CSS_SELECTOR, 'button._abl-')
        if next_btns:
            next_btn = next_btns[-1]
            driver.execute_script('arguments[0].click();', next_btn)
            print(f'[{i+1}] 다음 게시물로 이동')
            time.sleep(3)  # 다음 게시물 로딩 대기
        else:
            print(f'[{i+1}] 다음 버튼을 찾을 수 없습니다.')
            break
    except Exception as e:
        print(f'[{i+1}] 다음 버튼을 찾을 수 없거나 더 이상 게시물이 없습니다: {e}')
        break

# 브라우저가 바로 닫히지 않도록 대기 (사용자 입력 대기)
input("프로그램을 종료하려면 Enter를 누르세요...")
driver.quit()  # 브라우저 종료