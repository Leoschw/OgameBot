import logInFile
# <a class="slideIn timeLink" href="javascript:void(0);" ref="2">
#                 <span class="time" id="test" name="zeit">3m 28s</span>
#             </a>


def someBeingBuilt():
    (logInFile.browser.find_element_by_xpath("//span[@name='zeit']"))
    return

def levelOfMetalMineOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='1']/span/span").text)
    return

def levelOfCrystalMineOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*["
                                                "@ref='2']/span/span").text)
    return

def levelOfDeutMineOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='3']/span/span").text)
    return

def levelOfPowerStationOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='4']/span/span").text)
    return

def buildButton():
    logInFile.browser.find_element_by_xpath("//*[ "
     "@id='content']/div[2]/a/span[contains(text(),  'Ausbauen')]")
    return

def energyRessource()-> int:
    int((logInFile.browser.find_element_by_xpath("//*["
                                                 "@id='resources_energy']")).text)
    return

def crystalStorageOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='23']").text)
    return

def metalStorageOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='22']").text)
    return

def deutStorageOnTooltip()-> int:
    int(logInFile.browser.find_element_by_xpath("//*[@ref='24']").text)
    return

def toolTipToDetailsDeut():
    logInFile.browser.find_element_by_xpath("//*[@ref='3']")
    return

def toolTipToDetailsCryst():
    logInFile.browser.find_element_by_xpath("//*[@ref='2']")
    return

def toolTipToDetailsMet():
    logInFile.browser.find_element_by_xpath("//*[@ref='1']")
    return

def toolTipToDetailsPower():
    logInFile.browser.find_element_by_xpath("//*[@ref='4']")
    return

def crystalOvermarked():
    logInFile.browser.find_element_by_xpath("//[@id= 'resources_crystal'"
      " and @class='overmark']")
    return

def metalOvermarked():
    logInFile.browser.find_element_by_xpath(("//["
   "@id= 'resources_metal' and @class='overmark']"))
    return

def deuteriumOvermarked():
    logInFile.browser.find_element_by_xpath((
    "//[@id= 'resources_deuterium' and @class='overmark']"))
    return



# webElements = {
# someBeingBuilt = (logInFile.browser.find_element_by_xpath("//*[@name='zeit']"))
# levelOfCrystalMineOnTooltip = (logInFile.browser.find_element_by_xpath("//*["
#                                                                           "@ref='2']/span/span"))
# levelOfMetalMineOnTooltip = (logInFile.browser.find_element_by_xpath("//*[@ref='1']/span/span"))
# levelOfDeutMineOnTooltip = (logInFile.browser.find_element_by_xpath("//*[@ref='3']/span/span"))
# levelOfPowerStationOnTooltip = (logInFile.browser.find_element_by_xpath("//*[@ref='4']/span/span"))
# buildButton = logInFile.browser.find_element_by_xpath("//*[@id='content']/div[2]/a/span[contains(text(), 'Ausbauen')]")
# energyRessource = (logInFile.browser.find_element_by_xpath("//*[@id='resources_energy']"))
#
# crystalStorageOnTooltip = (logInFile.browser.find_element_by_xpath("//*[@ref='23']"))
#
# metalStorageOnTooltip = (logInFile.browser.find_element_by_xpath("//*["
#                                                                           "@ref='22']"))
#
# deutStorageOnTooltip = (logInFile.browser.find_element_by_xpath("//*["
#                                                                           "@ref='24']"))
#
# toolTipToDetailsDeut = logInFile.browser.find_element_by_xpath("//*[@ref='3']")
# toolTipToDetailsCryst = logInFile.browser.find_element_by_xpath("//*[@ref='2']")
# toolTipToDetailsMet = logInFile.browser.find_element_by_xpath("//*[@ref='1']")
# toolTipToDetailsPower = logInFile.browser.find_element_by_xpath("//*[@ref='4']")
#
# crystalOvermarked = logInFile.browser.find_element_by_xpath(("//[@id= 'resources_crystal' and "
#                                                              "@class='overmark']"))
# metalOvermarked = logInFile.browser.find_element_by_xpath(("//[@id= 'resources_metal' and "
#                                                              "@class='overmark']"))
# deuteriumOvermarked = logInFile.browser.find_element_by_xpath(("//[@id= 'resources_deuterium' and "
#                                                              "@class='overmark']"))
#
# }
# <li id="crystal_box" class="crystal tooltipHTML" title="">
#                 <div class="resourceIcon crystal"></div>
#                 <span class="value">
#                     <span id="resources_crystal" class="overmark">10.000</span>
#                 </span>
#             </li>

# #
# # //*[@id="MAX_531585f6"]/div[1]/a
# //*[@id="MAX_531585f6"]/div[1]/br
# //*[@id="test"]