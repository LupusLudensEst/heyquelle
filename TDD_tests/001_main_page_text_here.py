from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
TEXT_IS_HERE = (By.XPATH, "//p[@class='font_9']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.heyquelle.com/' )

# 2. Verify text "© 2021 Quelle. All Rights Reserved." is here
expected_text = '© 2021 Quelle. All Rights Reserved.'
actual_text = wait.until(EC.visibility_of_element_located(TEXT_IS_HERE)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
