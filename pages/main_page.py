from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
import time


# Locators
TEXT_IS_HERE = (By.XPATH, "//p[@class='font_9']")
URL_FLD = (By.XPATH, "//input[@inputmode='search']")
SRCH_BTN = (By.XPATH, "//button[@class='button search__btn button--color-blue button--v-default button--size-lg']")
SCRT_SCR = (By.XPATH, "(//span[@class='security-level__score'])[2]")
CRTCL_RSK = (By.XPATH, "(//div[@class='severity__count'])[1]")
MDM_RSK = (By.XPATH, "(//div[@class='severity__count'])[2]")
ELVT_RSK = (By.XPATH, "(//div[@class='severity__count'])[3]")
ISSR_DN = (By.XPATH, "//pre[@class='pre-text']")
ADDRESS_1_IS_HERE = (By.XPATH, "//span[contains(text(), '640 Ellicott Street,')]")
ADDRESS_2_IS_HERE = (By.XPATH, "//span[contains(text(), 'Buffalo, NY 14203')]")
EMAIL = (By.XPATH, "//span[contains(text(), 'hello@heyquelle.com')]")
QUELLE_TXT = (By.XPATH, "(//span[@class='color_25'])[1]")
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

class MainPage(Page):

    # 001 Verify text "© 2021 Quelle. All Rights Reserved" is here
    def vrfy_txt_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = txt
        sleep(1.5)
        actual_text = wait.until(EC.presence_of_element_located((TEXT_IS_HERE))).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 002 Vulnerability test
    # Login https://spyse.com/
    def lgn_spyse(self, spyse):
        self.driver.get(spyse)

    # Input https://www.heyquelle.com/ to search field
    def inpt_our_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(URL_FLD)).clear()
        wait.until(EC.presence_of_element_located(URL_FLD)).send_keys(url)

    # Click on Search button
    def clck_srch_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(SRCH_BTN)).click()

    # Find security score, critical risk, medium risk, elevated risk, issuer DN
    def fnd_all_data(self):
        wait = WebDriverWait(self.driver, 10)
        security_score = wait.until(EC.visibility_of_element_located(SCRT_SCR)).text.lower()
        critical_risk = wait.until(EC.visibility_of_element_located(CRTCL_RSK)).text.lower()
        medium_risk = wait.until(EC.visibility_of_element_located(MDM_RSK)).text.lower()
        elevated_risk = wait.until(EC.visibility_of_element_located(ELVT_RSK)).text.lower()
        issuer_dn = wait.until(EC.visibility_of_element_located(ISSR_DN)).text.lower()
        print(
            f'Security score: "{security_score}";\nCritical risk: "{critical_risk}";\nMedium risk: "{medium_risk}"\n'
            f'Elevated risk: "{elevated_risk}";\nIssuer DN: "{issuer_dn}"')

    # Make a screenshot of the whole page
    def mk_scrnsht(self):
        ob = Screenshot_Clipping.Screenshot()
        url = self.driver.current_url
        today = time.strftime(f'%Y_%m_%d')
        now = time.strftime(f'%H_%M_%S')
        file_name = 'vulnerability_' + today + '_' + now + '.jpg'
        img_url = ob.full_Screenshot(self.driver,
                                     save_path=r'C:\Everything\IT\Testing\Automation_08_09_2019\heyquelle\screen_shots',
                                     image_name=file_name)
        print(img_url)

    # End of the above code

    # 003 Verify address, email and logo are here
    # Verify address "640 Ellicott Street" is here
    def vrfy_addrss_1_here(self, addrss_1):
        wait = WebDriverWait(self.driver, 10)
        expected_text = addrss_1
        actual_text = wait.until(EC.visibility_of_element_located(ADDRESS_1_IS_HERE)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # Verify address "Buffalo, NY 14203" is here
    def vrfy_addrss_2_here(self, addrss_2):
        wait = WebDriverWait(self.driver, 10)
        expected_text = addrss_2
        actual_text = wait.until(EC.visibility_of_element_located(ADDRESS_2_IS_HERE)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # Verify email "hello@heyquelle.com" is here
    def vrfy_email_here(self, mail):
        wait = WebDriverWait(self.driver, 10)
        expected_text = 'hello@heyquelle.com'
        actual_text = wait.until(EC.visibility_of_element_located(EMAIL)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # Verify logo "Quelle is the place that connects specialty contract recruiters directly to companies." is here
    def vrfy_logo_here(self, logo):
        wait = WebDriverWait(self.driver, 10)
        expected_text = logo
        sleep(4)
        actual_text = wait.until(EC.visibility_of_element_located(QUELLE_TXT)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 004 Go as a Recruiter and verify all works according the steps
    def recruiter_steps(self):
        # 2. Click on Recruiters button
        self.driver.find_element(*RECRUITERS_BTN).click()

        # 3. Verify "Recruiters" is here
        expected_text = 'Recruiters'
        wait = WebDriverWait(self.driver, 10)
        sleep(4)
        actual_text = wait.until(EC.visibility_of_element_located(RECRUITERS_TXT)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # 4. Click on Start button
        self.driver.find_element(*START_RCRTS).click()

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
        self.driver.find_element(*OK_BTN_AFTR_NM).click()

        # 8. Verify "Nice to meet you, First and last name." is here
        expected_text = "Nice to meet you, " + name + "."
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
        self.driver.find_element(*OK_BTN_AFTR_EMAIL).click()

        # 11. Verify "What hourly job rates are you willing to consider?" is here
        expected_text = "What hourly job rates are you willing to consider?"
        print(expected_text)
        sleep(4)
        actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_OK_BTN_AFTR_EMAIL)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # 12. Click on 50 - 75 range button and Ok button
        self.driver.find_element(*CLK_50_75_RNG).click()
        self.driver.find_element(*OK_BTN_AFTR_CLK_50_75_RNG).click()

        # 13. Click on 40 hours range button and Ok button
        sleep(4)
        self.driver.find_element(*CLK_40_HRS_RNG).click()
        self.driver.find_element(*OK_BTN_AFTR_CLK_40_HRS_RNG).click()

        # 14. Enter Phone number to proper field
        # ph_no = str("(" + password[::4] + ")" + password[3:6:] + "-" + password[4:8:]).strip()
        # ph_no = str(password[::4] + password[3:6:] + password[4:8:]).strip()
        sleep(4)
        wait.until(EC.presence_of_element_located(PHN_NMB_FLD)).clear()
        sleep(4)
        wait.until(EC.presence_of_element_located(PHN_NMB_FLD)).send_keys('(201) 555-0123')  # (ph_no)

        # 15. Click on Ok button after phone was sent
        self.driver.find_element(*OK_BTN_AFTR_PHN_SNT).click()

        # 16. Verify "Let us know a little bit more about the experience you have with certain types of recruiting." is here
        expected_text = "Let us know a little bit more about the experience you have with certain types of recruiting."
        print(expected_text)
        sleep(4)
        actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_PHN_SNT)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # 17. Click on Continue button
        self.driver.find_element(*CNTNUE_BTN).click()

        # 18. Verify "What type of recruiting have you done?This question is required." is here
        expected_text = "What type of recruiting have you done?"
        print(expected_text)
        sleep(4)
        actual_text = wait.until(EC.visibility_of_element_located(TXT_AFTR_CNTNUE_BTN)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # 19. Click on Technical Recruiting button
        self.driver.find_element(*TCNL_RCRT_BTN).click()

        # 20. Click on Ok button after Technical Recruiting button
        # Activate ActionChains
        sleep(2)
        target = wait.until(EC.element_to_be_clickable(OK_BTN_AFTR_TCNL_RCRT))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        # Here i got a blocker-OK_BTN_AFTR_TCNL_RCRT-is not clickable-need resolve it with the developer

    # End of the above code







