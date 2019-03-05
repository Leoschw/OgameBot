# # # @staticmethod
# # # def creaObj(dict):
# # #
# # #     for key_name in dict:
# # #         print('creating Obj')
# # #         key_name = WebElement(key_name,
# # #                               dict[key_name])
# # #         print('Obj created')
# #
# # # """
# # # DEIFITIONS WEBELEMENTS
# # # --------------------------------------------------------------------------------
# # # """
# # # """
# # # Übersicht
# # # --------------------------------------------------------------------------------
# # # """
# # # btnUbersicht = WebElement(('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Übersicht\')]'), level_num=None)
# # #
# # # """
# # # Versorgung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnVersorgung = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Versorgung\')]', level_num=None)
# # # levelMetalMn = WebElement('//*[@ref=\'1\']/span/span','//*[\'@ref=\'1\']')
# # # leveCrysMn = WebElement('//*[@ref=\'2\']/span/span', '//*[//*[@ref=\'3\']')
# # # levelPower = WebElement('//*[@ref=\'4\']/span/span', '//*[\'@ref=\'4\']')
# # # eRessource = WebElement('//*[@id=\'resources_energy\']', level_num=None)
# # # crysStoLVL = WebElement('//*[@ref=\'23\']', level_num=None)
# # # metStoLVL = WebElement('//*[@ref=\'22\']', level_num=None)
# # # deutStoLVL = WebElement('//*[@ref=\'24\']', level_num=None)
# # # btnDeutSto = WebElement('//*[@ref=\'3\']', level_num=None)
# # # btnMetSto = WebElement('//*[@ref=\'1\']', level_num=None)
# # # btnCrysSto = WebElement('//*[@ref=\'2\']', level_num=None)
# # # btnPower = WebElement('//*[@ref=\'4\']', level_num=None)
# # # crysOverm = WebElement('//[@id=\'resources_crystal\' and @class=\'overmark\']', level_num=None)
# # # metOverm = WebElement('//[@id=\'resources_metal\' and @class=\'overmark\']', level_num=None)
# # # deutOverm = WebElement('//[@id=\'resources_deuterium\' and @class=\'overmark\']', level_num=None)
# # #
# # #
# # # """
# # # Anlagen
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAnlagen = WebElement('//*[@class=\'textlabel\' and contains(text()\'Anlagen\')]')
# # # levelRobo = WebElement('//*[@ref=\'14\']/span/span')
# # # btnRobo = WebElement('//*[@ref=\'14\']')
# # # levelRaumschw = WebElement('//*[@ref=\'21\']/span/span')
# # # btnRaumschw = WebElement('//*[@ref=\'21\']')
# # # levelFLab = WebElement('//*[@ref=\'31\']/span/span')
# # # btnFLab = WebElement('//*[@ref=\'31\']')
# # #
# # #
# # # """
# # # Händler
# # # --------------------------------------------------------------------------------
# # # """
# # # btnHandler = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Händler\')]')
# # #
# # # """
# # # Forschung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnForschung = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Forschung\')]')
# # # eTech = WebElement('//*[@ref=\'113\']/span/span')
# # # btneTech = WebElement('//*[@ref=\'113\']')
# # # laserTech = WebElement('//*[@ref=\'120\']/span/span')
# # # btnlaserTech = WebElement('//*[@ref=\'120\']')
# # # ioTech = WebElement('//*[@ref=\'121\']/span/span')
# # # btnioTech = WebElement('//*[@ref=\'121\']')
# # # hyperTech = WebElement('//*[@ref=\'114\']/span/span')
# # # btnhyperTech = WebElement('//*[@ref=\'114\']')
# # # plasmaTech = WebElement('//*[@ref=\'122\']/span/span')
# # # btnplasmaTech = WebElement('//*[@ref=\'122\']')
# # # verbrTech = WebElement('//*[@ref=\'115\']/span/span')
# # # btnverbrTech = WebElement('//*[@ref=\'115\']')
# # # impTech = WebElement('//*[@ref=\'117\']/span/span')
# # # btnimpTech = WebElement('//*[@ref=\'117\']')
# # # hyperAntTech = WebElement('//*[@ref=\'118\']/span/span')
# # # btnhyperAntTech = WebElement('//*[@ref=\'118\']')
# # # spioTech = WebElement('//*[@ref=\'106\']/span/span')
# # # btnspioTech = WebElement('//*[@ref=\'106\']')
# # # compTech = WebElement('//*[@ref=\'108\']/span/span')
# # # btncompTech = WebElement('//*[@ref=\'108\']')
# # # astroTech = WebElement('//*[@ref=\'124\']/span/span')
# # # btnastroTech = WebElement('//*[@ref=\'124\']')
# # # intergalFTech = WebElement('//*[@ref=\'123\']/span/span')
# # # btnintergalFTech = WebElement('//*[@ref=\'123\']')
# # # graviTech = WebElement('//*[@ref=\'199\']/span/span')
# # # btngraviTech = WebElement('//*[@ref=\'199\']')
# # # weapTech = WebElement('//*[@ref=\'109\']/span/span')
# # # btnweapTech = WebElement('//*[@ref=\'109\']')
# # # shieldTech = WebElement('//*[@ref=\'110\']/span/span')
# # # btnshieldTech = WebElement('//*[@ref=\'110\']')
# # # panzTech = WebElement('//*[@ref=\'111\']/span/span')
# # # btnpanzTech = WebElement('//*[@ref=\'111\']')
# # #
# # #
# # #
# # # """
# # # Schiffswerft
# # # --------------------------------------------------------------------------------
# # # """
# # # btnSchiffswerft = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Schiffswerft\')]')
# # # numLJ = WebElement('//*[@ref=\'204\']/span/span')
# # # btnnumLJ = WebElement('//*[@ref=\'204\']')
# # # numSJ = WebElement('//*[@ref=\'205\']/span/span')
# # # btnnumSJ = WebElement('//*[@ref=\'205\']')
# # # numXer = WebElement('//*[@ref=\'206\']/span/span')
# # # btnnumXer = WebElement('//*[@ref=\'206\']')
# # # numSS = WebElement('//*[@ref=\'207\']/span/span')
# # # btnnumSS = WebElement('//*[@ref=\'207\']')
# # # numKT = WebElement('//*[@ref=\'202\']/span/span')
# # # btnnumKT = WebElement('//*[@ref=\'202\']')
# # # numGT = WebElement('//*[@ref=\'203\']/span/span')
# # # btnnumGT = WebElement('//*[@ref=\'203\']')
# # # numKolo = WebElement('//*[@ref=\'208\']/span/span')
# # # btnnumKolo = WebElement('//*[@ref=\'208\']')
# # # numSXer = WebElement('//*[@ref=\'215\']/span/span')
# # # btnnumSXer = WebElement('//*[@ref=\'215\']')
# # # numBB = WebElement('//*[@ref=\'211\']/span/span')
# # # btnnumBB = WebElement('//*[@ref=\'211\']')
# # # numZer = WebElement('//*[@ref=\'213\']/span/span')
# # # btnnumZer = WebElement('//*[@ref=\'213\']')
# # # numDstar = WebElement('//*[@ref=\'214\']/span/span')
# # # btnnumDstar = WebElement('//*[@ref=\'214\']')
# # # numRec = WebElement('//*[@ref=\'209\']/span/span')
# # # btnnumRec = WebElement('//*[@ref=\'209\']')
# # # numSpio = WebElement('//*[@ref=\'210\']/span/span')
# # # btnnumSpio = WebElement('//*[@ref=\'210\']')
# # # numSol = WebElement('//*[@ref=\'212\']/span/span')
# # # btnnumSol = WebElement('//*[@ref=\'212\']')
# # #
# # #
# # # """
# # # Verteidigung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnVerteidigung = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Verteidigung\')]')
# # # numRak = WebElement('//*[@ref=\'401\']/span/span')
# # # btnRak = WebElement('//*[@ref=\'401\']')
# # # numLLas = WebElement('//*[@ref=\'402\']/span/span')
# # # btnLLas = WebElement('//*[@ref=\'402\']')
# # # numSLas = WebElement('//*[@ref=\'403\']/span/span')
# # # btnSLas = WebElement('//*[@ref=\'403\']')
# # # numGaus = WebElement('//*[@ref=\'404\']/span/span')
# # # btnGaus = WebElement('//*[@ref=\'404\']')
# # # numIoG = WebElement('//*[@ref=\'405\']/span/span')
# # # btnIoG = WebElement('//*[@ref=\'405\']')
# # # numPlasma = WebElement('//*[@ref=\'406\']/span/span')
# # # btnPlasma = WebElement('//*[@ref=\'406\']')
# # # numKlKuppel = WebElement('//*[@ref=\'407\']/span/span')
# # # btnKlKuppel = WebElement('//*[@ref=\'407\']')
# # # numGrKuppel = WebElement('//*[@ref=\'408\']/span/span')
# # # btnGrKuppel = WebElement('//*[@ref=\'408\']')
# # # numabfangRak = WebElement('//*[@ref=\'502\']/span/span')
# # # btnabfangRak = WebElement('//*[@ref=\'502\']')
# # # numInerplaRak = WebElement('//*[@ref=\'503\']/span/span')
# # # btnInerplaRak = WebElement('//*[@ref=\'503\']')
# # #
# # #
# # # """
# # # Flotte
# # # --------------------------------------------------------------------------------
# # # """
# # # btnFlotte = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Flotte\')]')
# # #
# # #
# # # """
# # # Galaxie
# # # --------------------------------------------------------------------------------
# # # """
# # # btnGalaxie = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Galaxie\')]')
# # #
# # #
# # # """
# # # Allianz
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAllianz = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Allianz\')]')
# # #
# # #
# # # """
# # # Offizierkasino
# # # --------------------------------------------------------------------------------
# # # """
# # # btnOffizierkasino = WebElement('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Offizierkasino\')]')
# # #
# # #
# # # """
# # # Shop
# # # --------------------------------------------------------------------------------
# # # """
# # # btnShop = WebElement('//*[@class=\'textlabel\' and contains(text()\'Shop\')]')
# # #
# # #
# # # """
# # # Misc
# # # --------------------------------------------------------------------------------
# # # """
# # # busyBuilding = WebElement('//span[@name=\'zeit\']', level_num=None)
# # #
# # # btnBldBldng = WebElement('//*[@id=\'content\']/div[2]/a/span[contains(text(),'
# # #                                                     '\'Ausbauen\')]', level_num=None)
# # #
# # # btnBldShp = WebElement('//*[@id=\'content\']/div[3]/a/span[contains(text(),\'Bauen\')]', level_num=None)
# # #
# # #
# # # btnVersorgung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                         ')\'Versorgung\')]'))
# # # levelMetalMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']/span/span'))
# # # btnMetalMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']'))
# # # leveCrysMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']/span/span'))
# # # btnCrysMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']'))
# # # levelDeutlMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']/span/span'))
# # # btnDeutlMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']'))
# # # levelPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']/span/span'))
# # # btnPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']'))
# # # eRessource = WebElement(driver.driver.find_element_by_xpath('//*[@id=\'resources_energy\']'))
# # # crysStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'23\']'))
# # # metStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'22\']'))
# # # deutStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'24\']'))
# # # btnDeutSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']'))
# # # btnMetSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']'))
# # # btnCrysSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']'))
# # # btnPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']'))
# # # crysOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_crystal\' and @class=\'overmark\']'))
# # # metOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_metal\' and @class=\'overmark\']'))
# # # deutOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_deuterium\' and @class=\'overmark\']'))
# # #
# # # """
# # # Anlagen
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAnlagen = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text()\'Anlagen\')]'))
# # # levelRobo = WebElement(driver.find_element_by_xpath('//*[@ref=\'14\']/span/span'))
# # # btnRobo = WebElement(driver.find_element_by_xpath('//*[@ref=\'14\']'))
# # # levelRaumschw = WebElement(driver.find_element_by_xpath('//*[@ref=\'21\']/span/span'))
# # # btnRaumschw = WebElement(driver.find_element_by_xpath('//*[@ref=\'21\']'))
# # # levelFLab = WebElement(driver.find_element_by_xpath('//*[@ref=\'31\']/span/span'))
# # # btnFLab = WebElement(driver.find_element_by_xpath('//*[@ref=\'31\']'))
# # #
# # # """
# # # Händler
# # # --------------------------------------------------------------------------------
# # # """
# # # btnHandler = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Händler\')]'))
# # #
# # # """
# # # Forschung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnForschung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                        ')\'Forschung\')]'))
# # # eTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'113\']/span/span'))
# # # btneTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'113\']'))
# # # laserTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'120\']/span/span'))
# # # btnlaserTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'120\']'))
# # # ioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'121\']/span/span'))
# # # btnioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'121\']'))
# # # hyperTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'114\']/span/span'))
# # # btnhyperTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'114\']'))
# # # plasmaTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'122\']/span/span'))
# # # btnplasmaTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'122\']'))
# # # verbrTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'115\']/span/span'))
# # # btnverbrTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'115\']'))
# # # impTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'117\']/span/span'))
# # # btnimpTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'117\']'))
# # # hyperAntTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'118\']/span/span'))
# # # btnhyperAntTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'118\']'))
# # # spioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'106\']/span/span'))
# # # btnspioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'106\']'))
# # # compTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'108\']/span/span'))
# # # btncompTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'108\']'))
# # # astroTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'124\']/span/span'))
# # # btnastroTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'124\']'))
# # # intergalFTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'123\']/span/span'))
# # # btnintergalFTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'123\']'))
# # # graviTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'199\']/span/span'))
# # # btngraviTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'199\']'))
# # # weapTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'109\']/span/span'))
# # # btnweapTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'109\']'))
# # # shieldTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'110\']/span/span'))
# # # btnshieldTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'110\']'))
# # # panzTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'111\']/span/span'))
# # # btnpanzTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'111\']'))
# # #
# # # """
# # # Schiffswerft
# # # --------------------------------------------------------------------------------
# # # """
# # # btnSchiffswerft = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                           ')\'Schiffswerft\')]'))
# # # numLJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'204\']/span/span'))
# # # btnnumLJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'204\']'))
# # # numSJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'205\']/span/span'))
# # # btnnumSJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'205\']'))
# # # numXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'206\']/span/span'))
# # # btnnumXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'206\']'))
# # # numSS = WebElement(driver.find_element_by_xpath('//*[@ref=\'207\']/span/span'))
# # # btnnumSS = WebElement(driver.find_element_by_xpath('//*[@ref=\'207\']'))
# # # numKT = WebElement(driver.find_element_by_xpath('//*[@ref=\'202\']/span/span'))
# # # btnnumKT = WebElement(driver.find_element_by_xpath('//*[@ref=\'202\']'))
# # # numGT = WebElement(driver.find_element_by_xpath('//*[@ref=\'203\']/span/span'))
# # # btnnumGT = WebElement(driver.find_element_by_xpath('//*[@ref=\'203\']'))
# # # numKolo = WebElement(driver.find_element_by_xpath('//*[@ref=\'208\']/span/span'))
# # # btnnumKolo = WebElement(driver.find_element_by_xpath('//*[@ref=\'208\']'))
# # # numSXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'215\']/span/span'))
# # # btnnumSXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'215\']'))
# # # numBB = WebElement(driver.find_element_by_xpath('//*[@ref=\'211\']/span/span'))
# # # btnnumBB = WebElement(driver.find_element_by_xpath('//*[@ref=\'211\']'))
# # # numZer = WebElement(driver.find_element_by_xpath('//*[@ref=\'213\']/span/span'))
# # # btnnumZer = WebElement(driver.find_element_by_xpath('//*[@ref=\'213\']'))
# # # numDstar = WebElement(driver.find_element_by_xpath('//*[@ref=\'214\']/span/span'))
# # # btnnumDstar = WebElement(driver.find_element_by_xpath('//*[@ref=\'214\']'))
# # # numRec = WebElement(driver.find_element_by_xpath('//*[@ref=\'209\']/span/span'))
# # # btnnumRec = WebElement(driver.find_element_by_xpath('//*[@ref=\'209\']'))
# # # numSpio = WebElement(driver.find_element_by_xpath('//*[@ref=\'210\']/span/span'))
# # # btnnumSpio = WebElement(driver.find_element_by_xpath('//*[@ref=\'210\']'))
# # # numSol = WebElement(driver.find_element_by_xpath('//*[@ref=\'212\']/span/span'))
# # # btnnumSol = WebElement(driver.find_element_by_xpath('//*[@ref=\'212\']'))
# # #
# # # """
# # # Verteidigung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnVerteidigung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                           ')\'Verteidigung\')]'))
# # # numRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'401\']/span/span'))
# # # btnRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'401\']'))
# # # numLLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'402\']/span/span'))
# # # btnLLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'402\']'))
# # # numSLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'403\']/span/span'))
# # # btnSLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'403\']'))
# # # numGaus = WebElement(driver.find_element_by_xpath('//*[@ref=\'404\']/span/span'))
# # # btnGaus = WebElement(driver.find_element_by_xpath('//*[@ref=\'404\']'))
# # # numIoG = WebElement(driver.find_element_by_xpath('//*[@ref=\'405\']/span/span'))
# # # btnIoG = WebElement(driver.find_element_by_xpath('//*[@ref=\'405\']'))
# # # numPlasma = WebElement(driver.find_element_by_xpath('//*[@ref=\'406\']/span/span'))
# # # btnPlasma = WebElement(driver.find_element_by_xpath('//*[@ref=\'406\']'))
# # # numKlKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'407\']/span/span'))
# # # btnKlKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'407\']'))
# # # numGrKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'408\']/span/span'))
# # # btnGrKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'408\']'))
# # # numabfangRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'502\']/span/span'))
# # # btnabfangRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'502\']'))
# # # numInerplaRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'503\']/span/span'))
# # # btnInerplaRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'503\']'))
# # #
# # # """
# # # Flotte
# # # --------------------------------------------------------------------------------
# # # """
# # # btnFlotte = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                     ')\'Flotte\')]'))
# # #
# # # """
# # # Galaxie
# # # --------------------------------------------------------------------------------
# # # """
# # # btnGalaxie = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Galaxie\')]'))
# # #
# # # """
# # # Allianz
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAllianz = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Allianz\')]'))
# # #
# # # """
# # # Offizierkasino
# # # --------------------------------------------------------------------------------
# # # """
# # # btnOffizierkasino = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                             ')\'Offizierkasino\')]'))
# # #
# # # """
# # # Shop
# # # --------------------------------------------------------------------------------
# # # """
# # # btnShop = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text()\'Shop\')]'))
# # #
# # # """
# # # Misc
# # # --------------------------------------------------------------------------------
# # # """
# # # busyBuilding = WebElement(driver.find_element_by_xpath('//span[@name=\'zeit\']'))
# # #
# # # btnBldBldng = WebElement(driver.find_element_by_xpath('//*[@id=\'content\']/div[2]/a/span[contains(text(),'
# # #                                                       '\'Ausbauen\')]'))
# # #
# # # btnBldShp = WebElement(driver.find_element_by_xpath('//*[@id=\'content\']/div[3]/a/span[contains(text(),\'Bauen\')]'))
# # #
# #
# # #
# # # btnVersorgung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                         ')\'Versorgung\')]'))
# # # levelMetalMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']/span/span'))
# # # btnMetalMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']'))
# # # leveCrysMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']/span/span'))
# # # btnCrysMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']'))
# # # levelDeutlMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']/span/span'))
# # # btnDeutlMn = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']'))
# # # levelPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']/span/span'))
# # # btnPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']'))
# # # eRessource = WebElement(driver.driver.find_element_by_xpath('//*[@id=\'resources_energy\']'))
# # # crysStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'23\']'))
# # # metStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'22\']'))
# # # deutStoLVL = WebElement(driver.find_element_by_xpath('//*[@ref=\'24\']'))
# # # btnDeutSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'3\']'))
# # # btnMetSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'1\']'))
# # # btnCrysSto = WebElement(driver.find_element_by_xpath('//*[@ref=\'2\']'))
# # # btnPower = WebElement(driver.find_element_by_xpath('//*[@ref=\'4\']'))
# # # crysOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_crystal\' and @class=\'overmark\']'))
# # # metOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_metal\' and @class=\'overmark\']'))
# # # deutOverm = WebElement(driver.find_element_by_xpath('//[@id=\'resources_deuterium\' and @class=\'overmark\']'))
# # #
# # # """
# # # Anlagen
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAnlagen = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text()\'Anlagen\')]'))
# # # levelRobo = WebElement(driver.find_element_by_xpath('//*[@ref=\'14\']/span/span'))
# # # btnRobo = WebElement(driver.find_element_by_xpath('//*[@ref=\'14\']'))
# # # levelRaumschw = WebElement(driver.find_element_by_xpath('//*[@ref=\'21\']/span/span'))
# # # btnRaumschw = WebElement(driver.find_element_by_xpath('//*[@ref=\'21\']'))
# # # levelFLab = WebElement(driver.find_element_by_xpath('//*[@ref=\'31\']/span/span'))
# # # btnFLab = WebElement(driver.find_element_by_xpath('//*[@ref=\'31\']'))
# # #
# # # """
# # # Händler
# # # --------------------------------------------------------------------------------
# # # """
# # # btnHandler = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Händler\')]'))
# # #
# # # """
# # # Forschung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnForschung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                        ')\'Forschung\')]'))
# # # eTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'113\']/span/span'))
# # # btneTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'113\']'))
# # # laserTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'120\']/span/span'))
# # # btnlaserTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'120\']'))
# # # ioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'121\']/span/span'))
# # # btnioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'121\']'))
# # # hyperTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'114\']/span/span'))
# # # btnhyperTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'114\']'))
# # # plasmaTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'122\']/span/span'))
# # # btnplasmaTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'122\']'))
# # # verbrTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'115\']/span/span'))
# # # btnverbrTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'115\']'))
# # # impTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'117\']/span/span'))
# # # btnimpTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'117\']'))
# # # hyperAntTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'118\']/span/span'))
# # # btnhyperAntTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'118\']'))
# # # spioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'106\']/span/span'))
# # # btnspioTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'106\']'))
# # # compTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'108\']/span/span'))
# # # btncompTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'108\']'))
# # # astroTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'124\']/span/span'))
# # # btnastroTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'124\']'))
# # # intergalFTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'123\']/span/span'))
# # # btnintergalFTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'123\']'))
# # # graviTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'199\']/span/span'))
# # # btngraviTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'199\']'))
# # # weapTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'109\']/span/span'))
# # # btnweapTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'109\']'))
# # # shieldTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'110\']/span/span'))
# # # btnshieldTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'110\']'))
# # # panzTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'111\']/span/span'))
# # # btnpanzTech = WebElement(driver.find_element_by_xpath('//*[@ref=\'111\']'))
# # #
# # # """
# # # Schiffswerft
# # # --------------------------------------------------------------------------------
# # # """
# # # btnSchiffswerft = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                           ')\'Schiffswerft\')]'))
# # # numLJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'204\']/span/span'))
# # # btnnumLJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'204\']'))
# # # numSJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'205\']/span/span'))
# # # btnnumSJ = WebElement(driver.find_element_by_xpath('//*[@ref=\'205\']'))
# # # numXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'206\']/span/span'))
# # # btnnumXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'206\']'))
# # # numSS = WebElement(driver.find_element_by_xpath('//*[@ref=\'207\']/span/span'))
# # # btnnumSS = WebElement(driver.find_element_by_xpath('//*[@ref=\'207\']'))
# # # numKT = WebElement(driver.find_element_by_xpath('//*[@ref=\'202\']/span/span'))
# # # btnnumKT = WebElement(driver.find_element_by_xpath('//*[@ref=\'202\']'))
# # # numGT = WebElement(driver.find_element_by_xpath('//*[@ref=\'203\']/span/span'))
# # # btnnumGT = WebElement(driver.find_element_by_xpath('//*[@ref=\'203\']'))
# # # numKolo = WebElement(driver.find_element_by_xpath('//*[@ref=\'208\']/span/span'))
# # # btnnumKolo = WebElement(driver.find_element_by_xpath('//*[@ref=\'208\']'))
# # # numSXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'215\']/span/span'))
# # # btnnumSXer = WebElement(driver.find_element_by_xpath('//*[@ref=\'215\']'))
# # # numBB = WebElement(driver.find_element_by_xpath('//*[@ref=\'211\']/span/span'))
# # # btnnumBB = WebElement(driver.find_element_by_xpath('//*[@ref=\'211\']'))
# # # numZer = WebElement(driver.find_element_by_xpath('//*[@ref=\'213\']/span/span'))
# # # btnnumZer = WebElement(driver.find_element_by_xpath('//*[@ref=\'213\']'))
# # # numDstar = WebElement(driver.find_element_by_xpath('//*[@ref=\'214\']/span/span'))
# # # btnnumDstar = WebElement(driver.find_element_by_xpath('//*[@ref=\'214\']'))
# # # numRec = WebElement(driver.find_element_by_xpath('//*[@ref=\'209\']/span/span'))
# # # btnnumRec = WebElement(driver.find_element_by_xpath('//*[@ref=\'209\']'))
# # # numSpio = WebElement(driver.find_element_by_xpath('//*[@ref=\'210\']/span/span'))
# # # btnnumSpio = WebElement(driver.find_element_by_xpath('//*[@ref=\'210\']'))
# # # numSol = WebElement(driver.find_element_by_xpath('//*[@ref=\'212\']/span/span'))
# # # btnnumSol = WebElement(driver.find_element_by_xpath('//*[@ref=\'212\']'))
# # #
# # # """
# # # Verteidigung
# # # --------------------------------------------------------------------------------
# # # """
# # # btnVerteidigung = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                           ')\'Verteidigung\')]'))
# # # numRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'401\']/span/span'))
# # # btnRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'401\']'))
# # # numLLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'402\']/span/span'))
# # # btnLLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'402\']'))
# # # numSLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'403\']/span/span'))
# # # btnSLas = WebElement(driver.find_element_by_xpath('//*[@ref=\'403\']'))
# # # numGaus = WebElement(driver.find_element_by_xpath('//*[@ref=\'404\']/span/span'))
# # # btnGaus = WebElement(driver.find_element_by_xpath('//*[@ref=\'404\']'))
# # # numIoG = WebElement(driver.find_element_by_xpath('//*[@ref=\'405\']/span/span'))
# # # btnIoG = WebElement(driver.find_element_by_xpath('//*[@ref=\'405\']'))
# # # numPlasma = WebElement(driver.find_element_by_xpath('//*[@ref=\'406\']/span/span'))
# # # btnPlasma = WebElement(driver.find_element_by_xpath('//*[@ref=\'406\']'))
# # # numKlKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'407\']/span/span'))
# # # btnKlKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'407\']'))
# # # numGrKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'408\']/span/span'))
# # # btnGrKuppel = WebElement(driver.find_element_by_xpath('//*[@ref=\'408\']'))
# # # numabfangRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'502\']/span/span'))
# # # btnabfangRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'502\']'))
# # # numInerplaRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'503\']/span/span'))
# # # btnInerplaRak = WebElement(driver.find_element_by_xpath('//*[@ref=\'503\']'))
# # #
# # # """
# # # Flotte
# # # --------------------------------------------------------------------------------
# # # """
# # # btnFlotte = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                     ')\'Flotte\')]'))
# # #
# # # """
# # # Galaxie
# # # --------------------------------------------------------------------------------
# # # """
# # # btnGalaxie = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Galaxie\')]'))
# # #
# # # """
# # # Allianz
# # # --------------------------------------------------------------------------------
# # # """
# # # btnAllianz = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                      ')\'Allianz\')]'))
# # #
# # # """
# # # Offizierkasino
# # # --------------------------------------------------------------------------------
# # # """
# # # btnOffizierkasino = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text('
# # #                                                             ')\'Offizierkasino\')]'))
# # #
# # # """
# # # Shop
# # # --------------------------------------------------------------------------------
# # # """
# # # btnShop = WebElement(driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text()\'Shop\')]'))
# # #
# # # """
# # # Misc
# # # --------------------------------------------------------------------------------
# # # """
# # # busyBuilding = WebElement(driver.find_element_by_xpath('//span[@name=\'zeit\']'))
# # #
# # # btnBldBldng = WebElement(driver.find_element_by_xpath('//*[@id=\'content\']/div[2]/a/span[contains(text(),'
# # #                                                       '\'Ausbauen\')]'))
# # #
# # # btnBldShp = WebElement(driver.find_element_by_xpath('//*[@id=\'content\']/div[3]/a/span[contains(text(),\'Bauen\')]'))
# # #
# #
# #
# # # defBuildModActivator = classes.metalMine.LVL + classes.crystMine.LVL + classes.deutMine.LVL
# #
# #
# # import time, logInFile
# # from selenium import webdriver
# # from classes import Build, Build2
# #
# # driver = webdriver.Chrome(
# #     r'C:\Users\leosc\Downloads\chromedriver')  # set which
# #
# #
# # def logIn():
# #
# #     logInLoop = True
# #     while logInLoop == True:
# #         try:
# #             global driver
# #             driver = webdriver.Chrome(
# #                 r'C:\Users\leosc\Downloads\chromedriver')  # set which
# #             # driver to use
# #             driver.get('https://de.ogame.gameforge.com/')
# #             loopAdClose = True
# #             while loopAdClose == True:
# #                 try:
# #                     try:
# #                         # time.sleep(4)
# #                     # print ('trying')
# #                         if driver.find_element_by_xpath("//a[@href= 'javascript:;']"):
# #                             driver.find_element_by_xpath("//a[@href= 'javascript:;']").click()
# #                     except:
# #                         break
# #                 except Exception as e:
# #                     print (str(e))
# #                     continue
# #             driver.find_element_by_id('ui-id-1').click()
# #
# #             driver.switch_to.default_content()
# #             logIn_write_name = driver.find_element_by_id('usernameLogin')
# #             time.sleep(2) #otherwise it clicks AGB
# #
# #             logIn_write_name.send_keys('leo.schwab@gmx.net')
# #             logIn_write_pwd = driver.find_element_by_id('passwordLogin')
# #             logIn_write_pwd.send_keys('ls--1989')
# #             accptAGBbutton = driver.find_element_by_id('accept_btn')
# #             accptAGBbutton.click()
# #
# #             time.sleep(2) #otherwise it clicks AGB
# #
# #             logInButton = driver.find_element_by_id('loginSubmit')
# #             logInButton.click()
# #
# #             time.sleep(3) #otherwise it clicks AGB
# #
# #             logInToUni = driver.find_element_by_xpath("//*[contains(text(),"
# #                                                        "'Zuletzt')]")
# #             logInToUni.click()
# #             logInLoop = False
# #             # time.sleep(2) #otherwise it clicks AGB
# #             #
# #             # logInToUni = driver.find_element_by_class_name('btn-primary')
# #             # logInToUni.click()
# #
# #             time.sleep(5) #otherwise it clicks AGB
# #
# #         except Exception as e:
# #             print(str(e))
# #             driver.close()
# #             continue
# #
# #
# # logInFile.logIn()
# #
# # while True:
# #     try:  # if whole thing doesn't work -> reoload -> DOESN'T WORK
# #         print('new loop')
# #         # input()
# #         logInFile.time.sleep(3)
# #         logInFile.browser.get(
# #             'https://s159-de.ogame.gameforge.com/game/index.php?page'
# #             '=resources')
# #         allTabs = logInFile.browser.window_handles
# #
# #         for tab in allTabs:  # ***
# #             logInFile.browser.switch_to.window(tab)
# #             if logInFile.browser.current_url == \
# #                     'https://s159-de.ogame.gameforge.com/game/index.php?page' \
# #                     '=overview' \
# #                     '&relogin=1':
# #                 logInFile.browser.get(
# #                     'https://s159-de.ogame.gameforge.com/game/index.php?page'
# #                     '=resources')
# #                 break
# #     except:
# #         continue
# #
# #
# #     Build2.btnVersorgung.unique_ident.clickElement()
# #     Build2.btnDeutSto.clickElement()
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome(
#                 r'C:\Users\leosc\Downloads\chromedriver')
#
# wait = WebDriverWait(driver, 10)
#
# def build(item, value=None):
#     item.sparte().click()
#     time.sleep(1)
#     item.toolTip().click()
#     time.sleep(1)
#     try:
#         wait.until(EC.presence_of_element_located((By.XPATH, "//input["
#                                                          "@class='amount_input']"))).send_keys(value)
#     except:
#         pass
#     time.sleep(1)
#     item.ausbauButton().click()
#
# def compare(item1=None, item2=None, item3=None, item4=None, item5=None, item6=None):
#     comparedVal = item1.LVL()\
#     - item2.LVL()\
#     - item3.LVL()\
#     - item4.LVL()\
#     - item5.LVL()\
#     - item6.LVL()
#     return comparedVal
#
# def checkIfOvermarked():
#
#     for res in [resMet, resCrys, resDeut]:
#
#         try:
#             if res.overmarked:
#                 return True, res
#
#         except:
#             return False
#
#
# """
# Class Elements
# --------------------------------------------------------------------------------
# """
#
# class Build:
#
#     def __init__(self, ref):
#
#         self.toolTip = lambda: driver.find_element_by_xpath('//*[@ref=\''+str(ref)+'\']')
#         self.LVL = lambda: int(driver.find_element_by_xpath('//*[@ref=\''+str(ref)+'\']/span/span').text)
#         self.techTree = lambda: driver.find_element_by_xpath('//*[contains(text(), \'Techtree\')]')
#
# """
# Versorgung
# --------------------------------------------------------------------------------
# """
#
# class Versorgung(Build):
#
#     def __init__(self, ref):
#         super().__init__(ref)
#         self.sparte = lambda: driver.find_element_by_xpath('//*[contains(text(),\'Versorgung\')]')
#         self.ausbauButton = lambda: driver.find_element_by_xpath('//*[@id=\'content\']/div[text(),\'Ausbauen\')]')
#
# metalMine = Versorgung(1)
# crystMine = Versorgung(2)
# deutMine = Versorgung(3)
# powerPlant = Versorgung(4)
# metalTank = Versorgung(22)
# crystTank = Versorgung(23)
# deutTank = Versorgung(24)
#
# """
# Anlagen
# --------------------------------------------------------------------------------
# """
#
# class Anlagen(Build):
#
#     def __init__(self, ref):
#         super().__init__(ref)
#         self.sparte = lambda: driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text(),\'Anlagen\')]')
#         self.ausbauButton = lambda: driver.find_element_by_xpath('//*[@id=\'content\']/div[text(),\'Ausbauen\')]')
#
# roboFab = Anlagen(14)
# schWerft = Anlagen(21)
# forschLab = Anlagen(31)
#
#
# """
# Forschung
# --------------------------------------------------------------------------------
# """
# class Forschung(Build):
#
#     def __init__(self, ref):
#         super().__init__(ref)
#         self.sparte = lambda: driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text(),\'Forschung\')]')
#         self.ausbauButton = lambda: driver.find_element_by_xpath('//*[@id=\'content\']/div[text(),\'Erforschen\')]')
#
# eTech = Forschung(113)
# laserTech = Forschung(120)
# ioTech = Forschung(121)
# hyperTech = Forschung(114)
# plasmaTech = Forschung(122)
# verbrTech = Forschung(115)
# impTech = Forschung(117)
# hyperAntTech = Forschung(118)
# spioTech = Forschung(106)
# compTech = Forschung(108)
# astroTech = Forschung(124)
# intergalFTech = Forschung(123)
# graviTech = Forschung(199)
# weapTech = Forschung(109)
# shieldTech = Forschung(110)
# panzTech = Forschung(111)
#
#
# """
# Schiffswerft
# --------------------------------------------------------------------------------
# """
#
# class Schiffswerft(Build):
#
#     def __init__(self, ref):
#         super().__init__(ref)
#         self.sparte = lambda: driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text(),\'Schiffswerft\')]')
#         self.ausbauButton = lambda: driver.find_element_by_xpath('//*[@id=\'content\']/div[text(),\'Bauen\')]')
#
#
# numLJ = Schiffswerft(204)
# numSJ = Schiffswerft(205)
# btnnumXer = Schiffswerft(206)
# btnnumSS = Schiffswerft(207)
# btnnumKT = Schiffswerft(202)
# btnnumGT = Schiffswerft(203)
# btnnumKolo = Schiffswerft(208)
# btnnumSXer = Schiffswerft(215)
# btnnumBB = Schiffswerft(211)
# btnnumZer = Schiffswerft(213)
# btnnumDstar = Schiffswerft(214)
# btnnumRec = Schiffswerft(209)
# btnnumSpio = Schiffswerft(210)
# btnnumSol = Schiffswerft(212)
#
#
# """
# Verteidigung
# --------------------------------------------------------------------------------
# """
#
# class Verteidigung(Build):
#
#     def __init__(self, ref):
#         super().__init__(ref)
#         self.sparte = lambda: driver.find_element_by_xpath('//*[@class=\'textlabel\' and contains(text(),\'Verteidigung\')]')
#         self.ausbauButton = lambda: driver.find_element_by_xpath('//*[@id=\'content\']/div[text(),\'Bauen\')]')
#
#
# btnRak = Verteidigung(401)
# btnLLas = Verteidigung(402)
# btnSLas = Verteidigung(403)
# btnGaus = Verteidigung(404)
# btnIoG = Verteidigung(405)
# btnPlasma = Verteidigung(406)
# btnKlKuppel = Verteidigung(407)
# btnGrKuppel = Verteidigung(408)
# btnabfangRak = Verteidigung(502)
# btnInerplaRak = Verteidigung(503)
#
#
# class Resources():
#
#     def __init__(self, resource, tank):
#         self.overmarked = lambda: driver.find_element_by_xpath('//span[@id=\''+resource+'\' and @class=\'overmark\']')
#         self.amount = lambda: int(driver.find_element_by_xpath('//span[@id=\''+resource+'\']'))
#         self.tank = tank
#
#
# resMet = Resources('resources_metal', metalTank)
# resCrys = Resources('resources_crystal', crystTank)
# resDeut = Resources('resources_deuterium', deutTank)
# resPower = Resources('resources_energy', None)
#
# """
# Verteidigung
# --------------------------------------------------------------------------------
# """