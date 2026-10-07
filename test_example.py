from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_github_search():
    driver = webdriver.Chrome()
    driver.get("https://github.com/search")

    driver.find_element(By.CSS_SELECTOR, '[aria-label="Search GitHub"]').send_keys("qa-guruu", Keys.ENTER)

    results = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="results-list"]'))
    )

    assert 'QA.GURU' in results.text

    driver.quit()



