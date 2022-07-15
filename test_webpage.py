from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    driver.get('http://www.google.com')
    assert driver.title == "Google"
    driver.quit()
    
def test_fb():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()