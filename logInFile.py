from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException



             #opens up ogame
# wait = WebDriverWait(browser, 10)


def logIn():

    logInLoop = True
    while logInLoop == True:
        try:
            global browser
            browser = webdriver.Chrome(
                r'C:\Users\leosc\Downloads\chromedriver')  # set which
            # browser to use
            browser.get('https://de.ogame.gameforge.com/')
            loopAdClose = True
            while loopAdClose == True:
                try:
                    try:
                        # time.sleep(4)
                    # print ('trying')
                        if browser.find_element_by_xpath("//a[@href= 'javascript:;']"):
                            browser.find_element_by_xpath("//a[@href= 'javascript:;']").click()
                    except:
                        break
                except Exception as e:
                    print (str(e))
                    continue
            browser.find_element_by_id('ui-id-1').click()

            browser.switch_to.default_content()
            logIn_write_name = browser.find_element_by_id('usernameLogin')
            time.sleep(2) #otherwise it clicks AGB

            logIn_write_name.send_keys('leo.schwab@gmx.net')
            logIn_write_pwd = browser.find_element_by_id('passwordLogin')
            logIn_write_pwd.send_keys('ls--1989')
            accptAGBbutton = browser.find_element_by_id('accept_btn')
            accptAGBbutton.click()

            time.sleep(2) #otherwise it clicks AGB

            logInButton = browser.find_element_by_id('loginSubmit')
            logInButton.click()

            time.sleep(5) #otherwise it clicks AGB
            #
            # logInToUni = browser.find_element_by_xpath("//*[contains(text(),"
            #                                            "'Zuletzt')]")
            # logInToUni.click()
            time.sleep(2) #otherwise it clicks AGB


            logInToUni = browser.find_element_by_xpath("//span[contains(text(), 'Spielen')]")
            logInToUni.click()
            time.sleep(5)

            linklist = browser.find_elements_by_xpath("//span[contains(text(), 'Spielen')]")
            uniList = ['Europa', 'Galatea', 'Dorado', 'Fenrir']

            # for uni in uniList:
            #     linklist = browser.find_elements_by_xpath('//span[contains(text(), ''\'' + uni + '\')]')
            for element in uniList:
                print(element)
                a = browser.find_element_by_xpath('//*[contains(text(),\'' + element +'\')]//parent::div//following-sibling::div//*[contains('
                                                              'text(),'
                                                              '\'Spielen\')]')
                time.sleep(1)
                print(a)
                handles = browser.window_handles
                time.sleep(3)

                for tab in handles:
                    time.sleep(3)
                    print(2)
                    browser.switch_to.window(tab)
                    time.sleep(3)

                    if browser.current_url == \
                            'https://lobby.ogame.gameforge.com/de_DE/accounts':
                        print(3)
                        print(element)

                        browser.find_element_by_xpath('//*[contains(text(),\'' + element +'\')]//parent::div//following-sibling::div//*[contains('
                                                              'text(),'
                                                              '\'Spielen\')]').click()
                        print('//*[contains(text(),\'' + element + '\')]//parent::div//following-sibling::div//*['
                                                                   'contains('
                                                              'text(),'
                                                              '\'Spielen\')]')
                        # browser.find_element_by_xpath(
                        #     '//*[contains(text(),\'' + element +'\')]//*[contains(text(),\'Spielen\')]').click()
                        print(element)
                        break

            logInLoop = False
            # input()
            time.sleep(5) #otherwise it clicks AGB

        except Exception as e:
            print(str(e))
            browser.close()
            continue




# wait.until(EC.element_to_be_clickable(By.ID('ui-id-1')))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_id('usernameLogin').click()))
#
# wait.until(EC.element_to_be_selected(browser.send_keys('leo.schwab@gmx.net').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_id('passwordLogin').click()))
#
# wait.until(EC.element_to_be_clickable(browser.send_keys('ls--1989').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_id('accept_btn').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_id('loginSubmit').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_class_name('button-primary').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_id('loginSubmit').click()))
#
# wait.until(EC.element_to_be_clickable(browser.find_element_by_class_name('button-primary').click()))
#
# # wait.until(EC.element_to_be_clickable(browser.find_element_by_class_name('btn-primary').click()))
#
# wait.until(EC.presence_of_element_located(browser.find_element_by_id('loginSubmit').click()))

# //*[@id="MAX_7be539ee"]/div[1]/a

# if browser.find_element_by_class_name("openX_int_closeButton"):
#     browser.find_element_by_xpath("openX_int_closeButton").click()
# handles = browser.window_handles
# print (handles)


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.alert_is_present()
#     )
# except:
#     pass
# # browser.switch_to.alert
# if browser.find_element_by_xpath("//a[@href= 'javascript:;']"):
  #     browser.find_element_by_xpath("//a[contains(text(), 'x')]").click()