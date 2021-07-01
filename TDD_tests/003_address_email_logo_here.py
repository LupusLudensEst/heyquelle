from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
ADDRESS_1_IS_HERE = (By.XPATH, "//span[contains(text(), '640 Ellicott Street,')]")
ADDRESS_2_IS_HERE = (By.XPATH, "//span[contains(text(), 'Buffalo, NY 14203')]")
EMAIL = (By.XPATH, "//span[contains(text(), 'hello@heyquelle.com')]")
QUELLE_TXT = (By.XPATH, "(//span[@class='color_25'])[1]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.heyquelle.com/' )

# 2. Verify text "640 Ellicott Street" is here
expected_text = '640 Ellicott Street'
actual_text = wait.until(EC.visibility_of_element_located(ADDRESS_1_IS_HERE)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 3. Verify text "Buffalo, NY 14203" is here
expected_text = 'Buffalo, NY 14203'
actual_text = wait.until(EC.visibility_of_element_located(ADDRESS_2_IS_HERE)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 4. Verify email "hello@heyquelle.com" is here
expected_text = 'hello@heyquelle.com'
actual_text = wait.until(EC.visibility_of_element_located(EMAIL)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 5. Verify logo "Quelle is the place that connects specialty contract recruiters directly to companies." is here
expected_text = 'Quelle is the place that connects specialty contract recruiters directly to companies.'
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(QUELLE_TXT)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()