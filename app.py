from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def setup_driver():
    chrome_options = Options()
    # 필요한 경우 옵션 추가
    # chrome_options.add_argument('--headless')  # 헤드리스 모드
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    
    # ChromeDriver 자동 설치 및 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

if __name__ == "__main__":
    driver = setup_driver()
    # 테스트: 구글 홈페이지 열기
    driver.get("https://www.google.com")
    print("페이지 제목:", driver.title)
    driver.quit()  # 브라우저 종료
