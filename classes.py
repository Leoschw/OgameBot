from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, traceback, re

driver = webdriver.Chrome(r'C:\Users\leosc\Downloads\chromedriver')


wait = WebDriverWait(driver, 7)

tryy = {}
listBuildables = []

def checkIfOvermarked():
    for res in [resMet, resCrys, resDeut]:
        try:
            if res.overmarked():
                return res

        except Exception as e:
            print(e)
            pass


def compare(item, *args):
    a = item.LVL()
    for argu in args:
        a -= argu.LVL()
        return a


class Buildables():

    def __repr__(self):
        return self.sparte, self.toolTip

    def __init__(self, name, ref, sparte, techTree, ausbauButton='Ausbauen', *args, **kwargs):

        self.name = name
        self.ref = ref
        self.toolTip = lambda: wait.until(
                EC.presence_of_element_located((By.XPATH, ('//*[@ref=\'{}\']').format(ref))))
        self.LVL = lambda: int(
                wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@ref=\'' + str(
                        ref) + '\']/span/span')))).text)
        self.techTree = techTree
        self.ausbauButton = lambda: wait.until(
                EC.presence_of_element_located((By.XPATH,
                                                ('//*[contains(text(),\'{}\')]').format(
                                                        ausbauButton))))
        self.sparte = lambda: wait.until(
                EC.presence_of_element_located(
                        (By.XPATH, ('//*[contains(text(),\'{}\')]').format(sparte))))
        tryy[name] = self


    def findTech(self):


        # self.toolTip().click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located(
                        (By.XPATH, ('//*[@class=\'techtree_img\']')))).click()
        time.sleep(2)

        wait.until(EC.presence_of_element_located(
                        (By.XPATH, ('//*[contains(text(),\'Technik\')]')))).click()

        # wait.until(EC.presence_of_element_located((By.XPATH, (
        #             '//*[@id="technology"]/div/h3[contains(text(),\'{}\')]').format(
        #                 self.techTree)))).click()
        needToBuild = wait.until(EC.presence_of_element_located((By.XPATH, (
            '//*[@id="technology"]//*[contains(@class,\'{}\')]//ancestor::tr//*[@class= \'overmark\']').format(self.ref)))).get_attribute('innerHTML')
        print(needToBuild)
        buildIt = re.findall(r'\w+', needToBuild, re.MULTILINE)
        print(buildIt)
        return tryy[buildIt[0]]

    def build(self, value=None):

        try:
            time.sleep(1)

            self.sparte().click()
            time.sleep(1)
            self.toolTip().click()
            time.sleep(1)
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(@class,\'cost\') and contains(@class,\'overmark\')]')))):
                    return

            except Exception:
                traceback.print_exc()
                pass
            try:
                wait.until(
                        EC.presence_of_element_located((By.XPATH, (
                            '//*[@class=\'build-it_disabled\']'))))
                Buildables.findTech(self).build()
            except Exception:
                traceback.print_exc()
                pass
            time.sleep(1)

            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//input["
                                                                     "@class='amount_input']"))).send_keys(
                        value)
            except:
                pass

            time.sleep(1)

            self.ausbauButton().click()
        except:
            pass





def defBuildMod():
    # schWerft.sparte().click()
    # if roboFab.LVL() < 2:
    #     roboFab.build()
    # elif schWerft.LVL() < 1:
    #     schWerft.build()
    # else:
    #     pass
    metalMine.sparte().click()
    driver.find_element_by_xpath('//*[contains(text(), \'Versorgungseinstellungen\')]').click()
    totProductionMSE = 10 * ((float(((wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                 '//*['
                                                                                 '@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[17]/td[2]/span')))).text)) + 2 * float(
            ((wait.until(EC.presence_of_element_located((By.XPATH,
                                                         '//*[@id="inhalt"]/div['
                                                         '2]/div['
                                                         '2]/form/table/tbody/tr['
                                                         '17]/td['
                                                         '3]/span')))).text)) + 3 * float(
            ((wait.until(EC.presence_of_element_located((By.XPATH,
                                                         '//*[@id="inhalt"]/div['
                                                         '2]/div['
                                                         '2]/form/table/tbody/tr['
                                                         '17]/td['
                                                         '4]/span'))))).text)) / 24)

    btnRak.sparte().click()

    try:
        shipCountRak = float(
                wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@ref=\'401\' and @id="shipcount"]'))).text)

        shipCountLl = float(
                wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@ref=\'402\' and @id="shipcount"]'))).text)

    # 75 Raketenwerfer : 150 Leichten Laser : 8 Gauskanonen : 1 Plasmawerfer
    # + kleine und große Schildkuppel

    except:
        shipCountRak = 0
        shipCountLl = 0
        pass

    numRaksToBuild = 75 * (round(totProductionMSE / 135.000))
    numLlToBuild = 150 * (round(totProductionMSE / 135.000))
    print(totProductionMSE, shipCountLl, shipCountRak, btnRak.LVL())
    print(numRaksToBuild, numLlToBuild)

    if btnRak.LVL() + shipCountRak < numRaksToBuild:

        btnRak.build((numRaksToBuild-btnRak.LVL()-shipCountRak))

    elif btnLLas.LVL() + shipCountLl < numLlToBuild:

        btnLLas.build(numLlToBuild-btnLLas.LVL()-shipCountLl)

    else:
        print('Enough Def')
        pass


class Resources():

    def __init__(self, resource, tank):
        self.overmarked = lambda: wait.until(EC.presence_of_element_located(
                (By.XPATH, ('//span[@id=\'' + resource + '\' and @class=\'overmark\']'))))
        self.amount = lambda: int(wait.until(EC.presence_of_element_located((By.XPATH, (
                '//span['
                '@id=\'' + resource + '\']')))).text)
        self.tank = tank


metalMine = Buildables('Metallmine', 1, 'Versorgung', 'Konstruktion')
crystMine = Buildables('Kristallmine', 2, 'Versorgung', 'Konstruktion')
deutMine = Buildables('Deuterium-Synthetisierer', 3, 'Versorgung', 'Konstruktion')
powerPlant = Buildables('Solarkraftwerk', 4, 'Versorgung', 'Konstruktion')
metalTank = Buildables('Metallspeicher', 22, 'Versorgung', 'Konstruktion')
crystTank = Buildables('Kristallspeicher', 23, 'Versorgung', 'Konstruktion')
deutTank = Buildables('Deuteriumtank', 24, 'Versorgung', 'Konstruktion')
roboFab = Buildables('Roboterfabrik', 14, 'Anlagen', 'Konstruktion')
schWerft = Buildables('Raumschiffswerft', 21, 'Anlagen', 'Konstruktion')
forschLab = Buildables('Forschungslabor', 31, 'Anlagen', 'Konstruktion')
eTech = Buildables('Energietechnik', 113, 'Forschung', 'Forschung', ausbauButton='Erforschen')
laserTech = Buildables('Lasertechnik', 120, 'Forschung', 'Forschung', ausbauButton='Erforschen')
ioTech = Buildables('Ionentechnik', 121, 'Forschung', 'Forschung', ausbauButton='Erforschen')
hyperTech = Buildables('Hyperraumtechnik', 114, 'Forschung', 'Forschung', ausbauButton='Erforschen')
plasmaTech = Buildables('Plasmatechnik', 122, 'Forschung', 'Forschung', ausbauButton='Erforschen')
verbrTech = Buildables('Verbrennungstriebwerk', 115, 'Forschung', 'Forschung',
                       ausbauButton='Erforschen')
impTech = Buildables('Impulstriebwerk', 117, 'Forschung', 'Forschung', ausbauButton='Erforschen')
hyperAntTech = Buildables('Hyperraumantrieb', 118, 'Forschung', 'Forschung',
                          ausbauButton='Erforschen')
spioTech = Buildables('Spionagetechnik', 106, 'Forschung', 'Forschung', ausbauButton='Erforschen')
compTech = Buildables('Computertechnik', 108, 'Forschung', 'Forschung', ausbauButton='Erforschen')
astroTech = Buildables('Astrophysik', 124, 'Forschung', 'Forschung', ausbauButton='Erforschen')
intergalFTech = Buildables('Intergalaktisches Forschungsnetzwerk', 123, 'Forschung', 'Forschung',
                           ausbauButton='Erforschen')
graviTech = Buildables('Gravitationforschung', 199, 'Forschung', 'Forschung',
                       ausbauButton='Erforschen')
weapTech = Buildables('Waffentechnik', 109, 'Forschung', 'Forschung', ausbauButton='Erforschen')
shieldTech = Buildables('Schildtechnik', 110, 'Forschung', 'Forschung', ausbauButton='Erforschen')
panzTech = Buildables('Raumschiffpanzerung', 111, 'Forschung', 'Forschung',
                      ausbauButton='Erforschen')
numLJ = Buildables('Platzhalter', 204, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
numSJ = Buildables('Platzhalter', 205, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumXer = Buildables('Platzhalter', 206, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumSS = Buildables('Platzhalter', 207, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumKT = Buildables('Platzhalter', 202, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumGT = Buildables('Platzhalter', 203, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumKolo = Buildables('Platzhalter', 208, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumSXer = Buildables('Platzhalter', 215, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumBB = Buildables('Platzhalter', 211, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumZer = Buildables('Platzhalter', 213, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumDstar = Buildables('Platzhalter', 214, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumRec = Buildables('Platzhalter', 209, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumSpio = Buildables('Platzhalter', 210, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnnumSol = Buildables('Platzhalter', 212, 'Schiffswerft', 'Schiffe', ausbauButton='In Bauliste')
btnRak = Buildables('Raketenwerfer', 401, 'Verteidigung', 'Verteidigung', ausbauButton='Bauen')
btnLLas = Buildables('Leichtes Lasergeschütz', 402, 'Verteidigung', 'Verteidigung',
                     ausbauButton='Bauen')
btnSLas = Buildables('Schweres Lasergeschütz', 403, 'Verteidigung', 'Verteidigung',
                     ausbauButton='Bauen')
btnGaus = Buildables('Gausskanone', 404, 'Verteidigung', 'Verteidigung', ausbauButton='Bauen')
btnIoG = Buildables('Ionengeschütz', 405, 'Verteidigung', 'Verteidigung', ausbauButton='Bauen')
btnPlasma = Buildables('Plasmawerfer', 406, 'Verteidigung', 'Verteidigung', ausbauButton='Bauen')
btnKlKuppel = Buildables('Kleine Schildkuppel', 407, 'Verteidigung', 'Verteidigung',
                         ausbauButton='Bauen')
btnGrKuppel = Buildables('Grosse Schildkuppel', 408, 'Verteidigung', 'Verteidigung',
                         ausbauButton='Bauen')
btnabfangRak = Buildables('Abfangrakete', 502, 'Verteidigung', 'Verteidigung', ausbauButton='Bauen')
btnInerplaRak = Buildables('Interplanetarrakete', 503, 'Verteidigung', 'Verteidigung',
                           ausbauButton='Bauen')

resMet = Resources('resources_metal', metalTank)
resCrys = Resources('resources_crystal', crystTank)
resDeut = Resources('resources_deuterium', deutTank)
resPower = Resources('resources_energy', None)
