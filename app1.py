from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 올바른 방식으로 ChromeDriver 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://instagram.com')

# 웹페이지에 보이는 글자 수집법
# 1. 원하는 글자 분석
# 2. 원하는 글자 찾아오라고 시키기


# <p class="x5n08af x1f6kntn xcxhlts x1jqylkn x1fqp7bg x13ibhcj x2b8uid">계정이 없으신가요? <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd" href="/accounts/emailsignup/" role="link" tabindex="0"><span class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x173jzuc x10wh9bi x1wdrske x8viiok x18hxmgj" style="line-height: 18px;">가입하기</span></a></p>

# time.sleep(2)
# e = driver.find_element(By.CSS_SELECTOR, 'p.x5n08af.x1f6kntn.xcxhlts.x1jqylkn.x1fqp7bg.x13ibhcj.x2b8uid')
# 이것도 과거 문법임


# 요소가 나타날 때까지 최대 10초 대기
wait = WebDriverWait(driver, 10) # 최신 문법
e = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.x5n08af.x1f6kntn.xcxhlts.x1jqylkn.x1fqp7bg.x13ibhcj.x2b8uid')))
# e = driver.find_element_by_css_selector('p.x5n08af.x1f6kntn.xcxhlts.x1jqylkn.x1fqp7bg.x13ibhcj.x2b8uid') 이거는 과거 문법임.
print(e.text) # 계정이 없으신가요? 가입하기 만 뜬다.

