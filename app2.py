from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 올바른 방식으로 ChromeDriver 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://instagram.com')

# 요소가 나타날 때까지 최대 10초 대기
wait = WebDriverWait(driver, 10) # 최신 문법

# ID로 요소 찾기 (최신 문법)
root_element = wait.until(EC.presence_of_element_located((By.ID, 'react-root')))
print("react-root 요소 찾음:", root_element)

# input 요소 찾기
# <input type="text" name="username" placeholder="전화번호, 사용자 이름 또는 이메일" required="" class="x1lliihq x6ikm8r x10wlt62 xlyipyv xuxw1ft">

# 과거 문법
# time.sleep(2)
# e = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').text
# 이것도 과거 문법임

# 요소가 나타날 때까지 최대 10초 대기
input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
print("input 요소 찾음:", input_element)

# """
# [app2.py 실행 원리 설명]

# 1. 기본 설정
#    - selenium, webdriver-manager 등 필요한 모듈 import
#    - ChromeDriver 자동 설치 및 초기화
#    - 인스타그램 웹사이트 접속

# 2. 요소 찾기 방식
#    - WebDriverWait: 요소가 나타날 때까지 최대 10초 대기
#    - EC.presence_of_element_located: 요소가 실제로 존재하는지 확인
#    - By.ID: ID로 요소 찾기 (react-root)
#    - By.CSS_SELECTOR: CSS 선택자로 요소 찾기 (input[name="username"])

# 3. 과거 문법과의 차이
#    - 과거: time.sleep()으로 고정 시간 대기
#    - 과거: find_element_by_* 메서드 사용
#    - 현재: WebDriverWait로 동적 대기
#    - 현재: find_element(By.*, ...) 형식 사용

# 4. 요소 확인
#    - 찾은 요소의 정보를 print로 출력
#    - 요소가 제대로 찾아졌는지 확인 가능
# """

