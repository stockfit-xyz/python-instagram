# 인스타그램 자동로그인
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# 올바른 방식으로 ChromeDriver 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://instagram.com')

# 요소가 나타날 때까지 최대 10초 대기
wait = WebDriverWait(driver, 10)

# 내 걸 알이서 찾아오라고 시키기
# <input type="text" name="username" placeholder="전화번호, 사용자 이름 또는 이메일" required="" class="x1lliihq x6ikm8r x10wlt62 xlyipyv xuxw1ft">
input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
print("input 요소 찾음:", input_element)

# 2초 대기
time.sleep(2)

# 입력 필드에 텍스트 입력
input_element.clear()  # 기존 텍스트가 있다면 지우기
input_element.send_keys("my_username_sample")  # 여기에 실제 사용자 이름을 입력하세요
print("입력된 텍스트:", input_element.get_attribute('value'))  # 입력된 텍스트 확인

# 비밀번호 입력 필드 찾기
# <input type="password" name="password" placeholder="비밀번호" required="" class="x1lliihq x6ikm8r x10wlt62 xlyipyv xuxw1ft">
password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
print("비밀번호 요소 찾음:", password_element)

# 2초 대기
time.sleep(2)

# 비밀번호 입력
password_element.clear()
password_element.send_keys("my_password_sample")  # 여기에 실제 비밀번호를 입력하세요
print("입력된 비밀번호:", password_element.get_attribute('value'))

# 2초 대기
time.sleep(2)

# 로그인 버튼 찾기
# <button type="submit" class="x1lliihq x6ikm8r x10wlt62 xlyipyv xuxw1ft">로그인</button>
login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
print("로그인 버튼 찾음:", login_button)

# 로그인 버튼 클릭
login_button.click()
print("로그인 시도 완료")

# 엔터키 입력하여 로그인 시도하는 방법
# password_element.send_keys(Keys.RETURN)
# print("로그인 시도 완료")

# 프로그램이 바로 종료되지 않도록 대기
time.sleep(10)  # 10초 동안 브라우저 유지


#--------------------------------
# """
# [app3.py 실행 원리 설명]

# 1. 기본 설정
#    - selenium, webdriver-manager 등 필요한 모듈 import
#    - ChromeDriver 자동 설치 및 초기화
#    - 인스타그램 웹사이트 접속

# 2. 사용자 이름 입력 과정
#    - CSS 선택자로 사용자 이름 입력 필드 찾기
#    - clear()로 기존 텍스트 제거
#    - send_keys()로 새 텍스트 입력
#    - get_attribute('value')로 입력된 텍스트 확인
#    - time.sleep()으로 2초 대기

# 3. 비밀번호 입력 과정
#    - CSS 선택자로 비밀번호 입력 필드 찾기
#    - clear()로 기존 텍스트 제거
#    - send_keys()로 새 텍스트 입력
#    - get_attribute('value')로 입력된 텍스트 확인
#    - time.sleep()으로 2초 대기

# 4. 로그인 시도
#    - CSS 선택자로 로그인 버튼 찾기
#    - click()으로 버튼 클릭
#    - 대체 방법: Keys.RETURN으로 엔터키 입력

# 5. 대기 시간 관리
#    - WebDriverWait: 요소가 나타날 때까지 최대 10초 대기
#    - time.sleep(): 각 단계 사이에 2초씩 대기
#    - 마지막 10초 대기로 결과 확인 시간 확보

# 6. 요소 찾기 방식
#    - By.CSS_SELECTOR: CSS 선택자로 요소 찾기
#    - wait.until(): 요소가 나타날 때까지 대기
#    - EC.presence_of_element_located: 요소 존재 확인
# """



