import classes as c
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback


def logInAccount(email, pwd):
    logInLoop = True

    while logInLoop == True:
        try:
            c.driver.get('https://de.ogame.gameforge.com/')
            try:
                if c.wait.until(
                        EC.presence_of_element_located((By.XPATH, "//a[@href= 'javascript:;']"))):
                    c.wait.until(EC.presence_of_element_located(
                            (By.XPATH, "//a[@href= 'javascript:;']"))).click()

            except:
                pass

            c.wait.until(
                    EC.presence_of_element_located((By.ID,'ui-id-1'))).click()

            c.driver.switch_to.default_content()
            c.wait.until(
                    EC.presence_of_element_located((By.ID,'usernameLogin'))).send_keys(email)
            # c.time.sleep(2)

            c.wait.until(
                    EC.presence_of_element_located((By.ID,'passwordLogin'))).send_keys(pwd)
            # c.time.sleep(2)
            try:
                c.wait.until(
                        EC.presence_of_element_located((By.ID,'accept_btn'))).click()
            except:
                pass
            c.time.sleep(0.5)

            c.wait.until(
                    EC.presence_of_element_located((By.ID,'loginSubmit'))).click()
            c.time.sleep(0.5)
            c.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Spielen')]"))).click()

            uniList = ['Galatea' , 'Europa', 'Fenrir', 'Dorado']

            for element in uniList:
                c.time.sleep(0.5)
                c.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                 '//*[contains(text(),'
																 '\'' + element + '\')]//parent::div//following'
																 '-sibling::div//*[contains(text(), ''\'Spielen\')]')))

                handles = c.driver.window_handles

                for tab in handles:

                    c.driver.switch_to.window(tab)
                    c.time.sleep(0.5)

                    if c.driver.current_url == \
                            'https://lobby.ogame.gameforge.com/de_DE/accounts':
                        c.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     '//*[contains(text(),'
																	 '\'' + element +
																	 '\')]//parent::div//following'
																	 '-sibling::div//*[contains('
                                                                                                          'text(),'
                                                                                                          '\'Spielen\')]'))).click()
                        c.time.sleep(1)

                        break

            logInLoop = False

            allTabs = c.driver.window_handles

            for tab in allTabs:
                c.time.sleep(1)
                c.driver.switch_to.window(tab)
                if c.driver.current_url == 'https://lobby.ogame.gameforge.com/de_DE/accounts':
                    c.driver.close()
                    break
        except:
            continue


def buildMinesCycle():
    while True:

        c.time.sleep(15)

        newTabs = c.driver.window_handles
        for tab in newTabs:
            c.driver.switch_to.window(tab)

            c.metalMine.sparte().click()

            try:
                if c.driver.find_element_by_xpath("//span[@name='zeit']"):
                    print('Busy!')
                    continue
            except:
                pass

            try:
                c.time.sleep(1)
                c.btnnumKolo.sparte().click()
                c.time.sleep(1)
                if c.btnnumKolo.LVL() < 8:
                    c.btnnumKolo.build()
            except Exception:
                traceback.print_exc()
                pass

            c.metalMine.sparte().click()

            try:
              c.defBuildMod()

            except:
                pass




            c.metalMine.sparte().click()
            #
            # defodActivator = c.metalMine.LVL() + c.crystMine.LVL() + c.deutMine.LVL()
            #
            # if defodActivator == 39:
            #     defMod = True
            #     print('DEF BUILD MODUS ACTIVATED!')
            #     print('0')

            if c.checkIfOvermarked():
                 c.checkIfOvermarked().tank.build()

            elif c.resPower.amount() < 0:
                print('2')
                c.powerPlant.build()

            elif c.compare(c.crystMine, c.metalMine) > -2 and c.resPower.amount() > 0:
                print('3')
                c.metalMine.build()
            elif c.compare(c.crystMine, c.metalMine) < -2 and c.resPower.amount() > 0:
                print('4')
                c.crystMine.build()


            elif c.compare(c.deutMine, c.crystMine) < -2 and c.resPower.amount() > 0:
                print('5')
                c.deutMine.build()

            else:
                print('6')
                c.metalMine.build()
