from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(r'C:\Users\leosc\Downloads\chromedriver')

wait = WebDriverWait(driver, 5)


def build(item, value=None):
    try:
        item.sparte().click()
        time.sleep(1)
        item.toolTip().click()
        time.sleep(1)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//input["
                                                             "@class='amount_input']"))).send_keys(value)
        except:
            pass
        time.sleep(1)
        item.ausbauButton().click()
    except:
        pass

def compare(item1, *args):
    a = item1.LVL()
    for argu in args:
        a -= argu.LVL()
        return a

def checkIfOvermarked():

    for res in [resMet, resCrys, resDeut]:
        try:
            if res.overmarked():
                return res

        except Exception as e:
            pass



class Build:

    def __init__(self, ref):

        self.toolTip = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@ref=\''+str(ref)+'\']'))))
        self.LVL = lambda: int(wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@ref=\''+str(
            ref)+'\']/span/span')))).text)
        #self.techTree = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@id="href" '
                                                                                      # 'contains('
                                                                                      # '\'https://s158-de.ogame.gameforge.com/game/index.php?page=techtree&tab=2&techID=113\')]')))).click().wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@id="href" '
                                                                                      # 'contains(text(), '
                                                                                      #                                                                                                                                                             'Technik\')))).click().
        self.ausbauButton = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(text(),\'Ausbauen\')]'))))

class Versorgung(Build):

    def __init__(self, ref):
        super().__init__(ref)
        self.sparte = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(text(),'
                                                                                    '\'Versorgung\')]'))))

class Anlagen(Build):

    def __init__(self, ref):
        super().__init__(ref)
        self.sparte = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@class=\'textlabel\' and contains(text(),\'Anlagen\')]'))))

class Forschung(Build):

    def __init__(self, ref):
        super().__init__(ref)
        self.sparte = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@class=\'textlabel\' and contains(text(),\'Forschung\')]'))))
        self.ausbauButton = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(text(),\'Erforschen\')]'))))

class Schiffswerft(Build):

    def __init__(self, ref):
        super().__init__(ref)
        self.sparte = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@class=\'textlabel\' and contains(text(),\'Schiffswerft\')]'))))
        self.ausbauButton = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(text(), '
                                                                                          '\'Bauen\')]'))))

class Verteidigung(Build):

    def __init__(self, ref):
        super().__init__(ref)
        self.sparte = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@class=\'textlabel\' and contains(text(),\'Verteidigung\')]'))))
        self.ausbauButton = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//*[contains(text(),'
                                                                                          '\'Bauen\')]'))))

class Resources():

    def __init__(self, resource, tank):
        self.overmarked = lambda: wait.until(EC.presence_of_element_located((By.XPATH, ('//span[@id=\''+resource+'\' and @class=\'overmark\']'))))
        self.amount = lambda: int(wait.until(EC.presence_of_element_located((By.XPATH, ('//span['                                                                                       '@id=\''+resource+'\']')))).text)
        self.tank = tank





metalMine = Versorgung(1)
crystMine = Versorgung(2)
deutMine = Versorgung(3)
powerPlant = Versorgung(4)
metalTank = Versorgung(22)
crystTank = Versorgung(23)
deutTank = Versorgung(24)
roboFab = Anlagen(14)
schWerft = Anlagen(21)
forschLab = Anlagen(31)
eTech = Forschung(113)
laserTech = Forschung(120)
ioTech = Forschung(121)
hyperTech = Forschung(114)
plasmaTech = Forschung(122)
verbrTech = Forschung(115)
impTech = Forschung(117)
hyperAntTech = Forschung(118)
spioTech = Forschung(106)
compTech = Forschung(108)
astroTech = Forschung(124)
intergalFTech = Forschung(123)
graviTech = Forschung(199)
weapTech = Forschung(109)
shieldTech = Forschung(110)
panzTech = Forschung(111)
numLJ = Schiffswerft(204)
numSJ = Schiffswerft(205)
btnnumXer = Schiffswerft(206)
btnnumSS = Schiffswerft(207)
btnnumKT = Schiffswerft(202)
btnnumGT = Schiffswerft(203)
btnnumKolo = Schiffswerft(208)
btnnumSXer = Schiffswerft(215)
btnnumBB = Schiffswerft(211)
btnnumZer = Schiffswerft(213)
btnnumDstar = Schiffswerft(214)
btnnumRec = Schiffswerft(209)
btnnumSpio = Schiffswerft(210)
btnnumSol = Schiffswerft(212)
btnRak = Verteidigung(401)
btnLLas = Verteidigung(402)
btnSLas = Verteidigung(403)
btnGaus = Verteidigung(404)
btnIoG = Verteidigung(405)
btnPlasma = Verteidigung(406)
btnKlKuppel = Verteidigung(407)
btnGrKuppel = Verteidigung(408)
btnabfangRak = Verteidigung(502)
btnInerplaRak = Verteidigung(503)
resMet = Resources('resources_metal', metalTank)
resCrys = Resources('resources_crystal', crystTank)
resDeut = Resources('resources_deuterium', deutTank)
resPower = Resources('resources_energy', None)