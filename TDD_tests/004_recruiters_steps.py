from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()

# Locators
RECRUITERS_BTN = (By.XPATH, "(//p[@class='ccDUc'])[1]")
RECRUITERS_TXT = (By.XPATH, "//h1[@class='text__TextWrapper-sc-1t2ribu-0 djHivM']")
START_RCRTS = (By.XPATH, "//button[@data-qa='start-button']")
HLLO_WHT_NM_HERE = (By.XPATH, "(//label[@data-qa='block-title deep-purple-block-title'])[1]")
FRS_LST_NMS = (By.XPATH, "//input[@autocomplete='name']")
OK_BTN_AFTR_NM = (By.XPATH, "//button[@data-qa='ok-button-visible deep-purple-ok-button-visible']")
TXT_AFTR_OK_BTN_AFTR_NM = (By.XPATH, "(//div[@class='text__TextWrapper-sc-1t2ribu-0 jGvYXS'])[2]")
EMAIL_FLD = (By.XPATH, "//input[@autocomplete='email']")
OK_BTN_AFTR_EMAIL = (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
TXT_AFTR_OK_BTN_AFTR_EMAIL = (By.XPATH, "(//div[@class='text__TextWrapper-sc-1t2ribu-0 jGvYXS'])[2]")
CLK_50_75_RNG = (By.XPATH, "(//div[@class='text__TextWrapper-sc-1t2ribu-0 jMCaoH'])[2]")
OK_BTN_AFTR_CLK_50_75_RNG = (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
CLK_40_HRS_RNG = (By.XPATH, "//img[@alt='40-hours']") # (By.XPATH, "(//div[@class='checkbox-list__Wrapper-werx6u-0 dFNQDt'])[7]")
OK_BTN_AFTR_CLK_40_HRS_RNG = (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
PHN_NMB_FLD = (By.NAME, "tel") # (By.ID, "phone_number-4c4df34b-e569-4043-a3b2-60c5575f5361-So9yCgfvnzEAIc3j")
OK_BTN_AFTR_PHN_SNT = (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
TXT_AFTR_PHN_SNT = (By.XPATH, "(//p[@data-qa='block-description'])[2]")
CNTNUE_BTN = (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
TXT_AFTR_CNTNUE_BTN = (By.XPATH, "(//span[@data-qa='block-title deep-purple-block-title'])[2]")
TCNL_RCRT_BTN = (By.XPATH, "(//div[@class='text__TextWrapper-sc-1t2ribu-0 jMCaoH'])[1]")
OK_BTN_AFTR_TCNL_RCRT = (By.XPATH, "(//button[@class='button__ButtonWrapper-sc-1g3rldj-0 hNhLaJ'])[2]")# (By.XPATH, "(//div[@class='submit__Root-sc-1ra8r4w-0 kYgMyf'])[2]") # (By.XPATH, "(//span[@class='button__FlexWrapper-sc-1g3rldj-1 dcBBsI'])[2]")  # (By.XPATH, "(//button[@data-qa='ok-button-visible deep-purple-ok-button-visible'])[2]")
SFWR_QA = (By.XPATH, "(//div[@class='checkbox-choice__ChoiceContent-m4g23g-1 erBFfO'])[13]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.heyquelle.com/' )

# 2. Click on Recruiters button
driver.find_element(*RECRUITERS_BTN).click()

# 3. Verify "Recruiters" is here
expected_text = 'Recruiters'
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(RECRUITERS_TXT)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 4. Click on Start button
driver.find_element(*START_RCRTS).click()

# 5. Verify "Hello, what's your name?" is here
expected_text = "Hello, what's your name?"
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(HLLO_WHT_NM_HERE)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 6. Enter the First and last name to proper field
password = str(randint(1000000000, 9999999999))
name = 'name' + " " + password
last_name = name + "_" + password
email = (password + '@sample.com')
print(f'\nName: {name}, \nlast name: {last_name},\nemail: {email} \nand password: {password}')

wait.until(EC.presence_of_element_located(FRS_LST_NMS)).clear()
wait.until(EC.presence_of_element_located(FRS_LST_NMS)).send_keys(name)

# 7. Click on Ok button after First and last name were sent
driver.find_element(*OK_BTN_AFTR_NM).click()

# 8. Verify "Nice to meet you, First and last name." is here
expected_text = "Nice to meet you, " + name +"."
print(expected_text)
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_OK_BTN_AFTR_NM)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 9. Enter the Email to proper field
wait.until(EC.presence_of_element_located(EMAIL_FLD)).clear()
wait.until(EC.presence_of_element_located(EMAIL_FLD)).send_keys(email)

# 10. Click on Ok button after email was sent
driver.find_element(*OK_BTN_AFTR_EMAIL).click()

# 11. Verify "What hourly job rates are you willing to consider?" is here
expected_text = "What hourly job rates are you willing to consider?"
print(expected_text)
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_OK_BTN_AFTR_EMAIL)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 12. Click on 50 - 75 range button and Ok button
driver.find_element(*CLK_50_75_RNG).click()
driver.find_element(*OK_BTN_AFTR_CLK_50_75_RNG).click()

# 13. Click on 40 hours range button and Ok button
sleep(4)
driver.find_element(*CLK_40_HRS_RNG).click()
driver.find_element(*OK_BTN_AFTR_CLK_40_HRS_RNG).click()

# 14. Enter Phone number to proper field
# ph_no = str("(" + password[::4] + ")" + password[3:6:] + "-" + password[4:8:]).strip()
# ph_no = str(password[::4] + password[3:6:] + password[4:8:]).strip()
sleep(4)
wait.until(EC.presence_of_element_located(PHN_NMB_FLD)).clear()
sleep(4)
wait.until(EC.presence_of_element_located(PHN_NMB_FLD)).send_keys('(201) 555-0123')

# 15. Click on Ok button after phone was sent
driver.find_element(*OK_BTN_AFTR_PHN_SNT).click()

# 16. Verify "Let us know a little bit more about the experience you have with certain types of recruiting." is here
expected_text = "Let us know a little bit more about the experience you have with certain types of recruiting."
print(expected_text)
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_PHN_SNT)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 17. Click on Continue button
driver.find_element(*CNTNUE_BTN).click()

# 18. Verify "What type of recruiting have you done?This question is required." is here
expected_text = "What type of recruiting have you done?"
print(expected_text)
sleep(4)
actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_CNTNUE_BTN)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 19. Click on Technical Recruiting button
driver.find_element(*TCNL_RCRT_BTN).click()

# 20. Click on Ok button after Technical Recruiting button
# Activate ActionChains
sleep(2)
target = wait.until(EC.element_to_be_clickable(OK_BTN_AFTR_TCNL_RCRT))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()
sleep(1.5)
# Here I got a blocker-OK_BTN_AFTR_TCNL_RCRT-is not clickable-need resolve it with the developer

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()