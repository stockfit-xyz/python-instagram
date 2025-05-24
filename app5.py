import time
# 인스타그램 자동로그인
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os

# 이미지 저장 폴더 생성 (없으면 새로 만듦)
save_dir = 'instagram-images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"'{save_dir}' 폴더가 생성되었습니다.")  # 폴더 생성 안내

# 크롬 드라이버 초기화 (자동 설치)
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

# 해시태그 검색 페이지로 이동 (여기서는 '사과' 해시태그)
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')
time.sleep(10)  # 해시태그 페이지 로딩 대기

# 첫 번째 게시물(이미지) 클릭
# 게시물 썸네일의 CSS 선택자 사용
driver.find_element(By.CSS_SELECTOR, 'div._aagw').click()
time.sleep(5)  # 게시물 팝업 로딩 대기

img_urls_seen = set()  # 이미 저장한 이미지 URL 집합
count = 1  # 저장 이미지 번호
while True:
    # 현재 페이지의 모든 img 태그 중에서 아직 저장하지 않은 src를 찾음
    img_url = None
    for img in driver.find_elements(By.CSS_SELECTOR, 'img'):
        src = img.get_attribute('src')
        if src and src not in img_urls_seen and 'http' in src:
            img_url = src
            break
    # 새로운 이미지가 있으면 저장
    if img_url:
        img_urls_seen.add(img_url)  # 중복 방지용 집합에 추가
        filename = f'instagram_image_{int(time.time())}_{count}.jpg'
        filepath = os.path.join(save_dir, filename)
        try:
            urllib.request.urlretrieve(img_url, filepath)
            print(f'[{count}] 이미지가 저장되었습니다: {filepath}')
        except Exception as e:
            print(f'[{count}] 이미지 저장 실패: {e}')
        count += 1
    else:
        print(f'[{count}] 새로운 이미지 URL을 찾을 수 없습니다')
    # 다음 버튼 클릭 (SVG title, aria-label, 텍스트 등 다양한 방식으로 '다음' 버튼 판별)
    try:
        time.sleep(3)  # 버튼 활성화 및 팝업 전환 대기
        next_btns = driver.find_elements(By.CSS_SELECTOR, 'button._abl-')
        next_btn = None
        for btn in reversed(next_btns):
            try:
                # 1. SVG title이 '다음'인지 확인
                svg_titles = btn.find_elements(By.TAG_NAME, 'title')
                if svg_titles and any('다음' in t.get_attribute('textContent') for t in svg_titles):
                    next_btn = btn
                    break
                # 2. aria-label 속성 확인
                aria_label = btn.get_attribute('aria-label')
                if aria_label and '다음' in aria_label:
                    next_btn = btn
                    break
                # 3. 버튼 내부 텍스트 확인
                if '다음' in btn.text:
                    next_btn = btn
                    break
            except Exception as e:
                continue
        if next_btn:
            driver.execute_script('arguments[0].click();', next_btn)  # 실제 '다음' 버튼 클릭
            print(f'[{count}] 다음 게시물로 이동')
            # 새로운 이미지 src가 나올 때까지 대기 (최대 10초)
            WebDriverWait(driver, 10).until(
                lambda d: any(
                    img.get_attribute('src') not in img_urls_seen and 'http' in img.get_attribute('src')
                    for img in d.find_elements(By.CSS_SELECTOR, 'img')
                )
            )
            time.sleep(1)  # 이미지 로딩 안정화 대기
        else:
            print(f'[{count}] 다음 버튼을 찾을 수 없습니다. 종료합니다.')
            break
    except Exception as e:
        print(f'[{count}] 다음 버튼을 찾을 수 없거나 더 이상 게시물이 없습니다: {e}')
        break

# 브라우저가 바로 닫히지 않도록 대기 (사용자 입력 대기)
input("프로그램을 종료하려면 Enter를 누르세요...")
driver.quit()  # 브라우저 종료