import classes as c
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def defBuildMod():

    totProductionMSE = 10 * (str(c.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                              '//*[@id="overview"]/div[11]/div['
                                                                              '3]/div/div/table/tbody/tr['
                                                                              '3]/td/span'))).text) + 1,
                             5 * str(c.wait.until(
                                 EC.presence_of_element_located((By.XPATH,
                                                                 '//*[@id="overview"]/div[13]/div['
                                                                 '3]/div/div/table/tbody/tr['
                                                                 '3]/td/span'))).text) + 3 * str(c.wait.until(
                                 EC.presence_of_element_located((By.XPATH,
                                                                 '//*[@id="overview"]/div[14]/div['
                                                                 '3]/div/div/table/tbody/tr['
                                                                 '3]/td/span'))).text))
    # 75 Raketenwerfer : 150L eichtenLaser: 8 Gauskanonen: 1 Plasmawerfer + kleine und große Schildkuppel

    numRaksToBuild = round(totProductionMSE / 135000)

    if c.btnRak.LVL() < numRaksToBuild:

        c.btnRak.sparte.click()

        c.btnRak.build(numRaksToBuild)

    else:
        pass

def logInAccount(email, pwd):

    logInLoop = True
    while logInLoop == True:
        try:
            c.driver.get('https://de.ogame.gameforge.com/')

            if c.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href= 'javascript:;']"))):
                c.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href= 'javascript:;']"))).click()

            else:
                pass

            c.driver.find_element_by_id('ui-id-1').click()

            c.driver.switch_to.default_content()
            logIn_write_name = c.driver.find_element_by_id('usernameLogin')
            c.time.sleep(2)

            logIn_write_name.send_keys(email)
            logIn_write_pwd = c.driver.find_element_by_id('passwordLogin')
            logIn_write_pwd.send_keys(pwd)
            accptAGBbutton = c.driver.find_element_by_id('accept_btn')
            accptAGBbutton.click()
            c.time.sleep(2)

            logInButton = c.driver.find_element_by_id('loginSubmit')
            logInButton.click()
            c.time.sleep(2)

            logInToUni = c.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Spielen')]")))
            logInToUni.click()
            c.time.sleep(2)

            uniList = ['Dorado', 'Galatea', 'Europa', 'Fenrir']

            for element in uniList:
                a = c.wait.until(EC.presence_of_element_located((By.XPATH,
                    '//*[contains(text(),\'' + element + '\')]//parent::div//following-sibling::div//*[contains('
                                                         'text(),'
                                                         '\'Spielen\')]')))
                handles = c.driver.window_handles
                c.time.sleep(2)

                for tab in handles:
                    c.driver.switch_to.window(tab)
                    c.time.sleep(2)

                    if c.driver.current_url == \
                            'https://lobby.ogame.gameforge.com/de_DE/accounts':

                        c.wait.until(EC.presence_of_element_located((By.XPATH,
                            '//*[contains(text(),\'' + element + '\')]//parent::div//following-sibling::div//*[contains('
                                                                 'text(),'
                                                                 '\'Spielen\')]'))).click()
                        break

            logInLoop = False
            c.time.sleep(2)  # otherwise it clicks AGB

            allTabs = c.driver.window_handles

            for tab in allTabs:  # ***
                c.driver.switch_to.window(tab)
                if c.driver.current_url == 'https://lobby.ogame.gameforge.com/de_DE/accounts':
                    c.driver.close()
                    break

        except:
            c.driver.close()
            continue


def buildMinesCycle():


    # totProductionMSE = 10*(str(c.wait.until(EC.presence_of_element_located((By.XPATH,
    #                                              '//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[4]/td[3]/span/text()'))).text) + 1,5*str(c.wait.until(
    #     EC.presence_of_element_located((By.XPATH,
    #                                              '//*[@id="overview"]/div[13]/div[3]/div/div/table/tbody/tr['
    #                                              '3]/td/span'))).text) + 3*str(c.wait.until(
    #     EC.presence_of_element_located((By.XPATH,
    #                                              '//*[@id="overview"]/div[14]/div[3]/div/div/table/tbody/tr['
    #                                              '3]/td/span'))).text))


    while True:


        c.time.sleep(10)
        newTabs = c.driver.window_handles
        for tab in newTabs:
            c.driver.switch_to.window(tab)

            # defBuildMod()

            c.time.sleep(1)
            c.metalMine.sparte().click()
            c.time.sleep(1)

            try:
               if c.driver.find_element_by_xpath("//span[@name='zeit']"):
                    print('Busy!')
                    continue
            except:
                pass

            defodActivator = c.metalMine.LVL() + c.crystMine.LVL() + c.deutMine.LVL()



            if defodActivator == 39:
                defMod = True
                print('DEF BUILD MODUS ACTIVATED!')

            elif c.checkIfOvermarked():
                c.build(c.checkIfOvermarked().tank)


            elif c.resPower.amount() < 0:
                c.build(c.powerPlant)

            elif c.compare(c.crystMine, c.metalMine) > -2 and c.resPower.amount() > 0:
                c.build(c.metalMine)
            elif c.compare(c.crystMine, c.metalMine) < -2 and c.resPower.amount() > 0:
                c.build(c.crystMine)


            elif c.compare(c.deutMine, c.crystMine) < -2 and c.resPower.amount() > 0:
                c.build(c.deutMine)


            else:
                c.build((c.metalMine))





