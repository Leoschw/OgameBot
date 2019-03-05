import logInFile

logInFile.logIn()

logInFile.time.sleep(5)

allTabs = logInFile.browser.window_handles

for tab in allTabs:  # ***
    logInFile.browser.switch_to.window(tab)
    if logInFile.browser.current_url == 'https://lobby.ogame.gameforge.com/de_DE/accounts':
        # logInFile.browser.get(
        #     'https://s159-de.ogame.gameforge.com/game/index.php?page'
        #     '=resources')
        logInFile.browser.close()
        break

"""
Defining variables
--------------------------------------------------------------------------------
"""

global defBuildModActivator
global defBuildMod
defBuildModActivator = 0
defBuildMod = False

"""
STAY ON RIGHT TAB
Making sure the bot stays on the right Tab. Somehow it would also work with 
switch to default content/switch to handle or so, but this is good workaround
for now
--------------------------------------------------------------------------------
"""
# ***
"""
--------------------------------------------------------------------------------

"""

"""
WHILE LOOP FOR BUILDING AND WAITING
somehow it was not possible to "outsource" the commands by putting them into 
a variable in another file since when I just put them into a variable in 
another file they are executed when the file is imported; if I write them as 
functions they give out a non_type return making it impossible to use them 
for calculations. 
--------------------------------------------------------------------------------
"""
while True:
    try:   # if whole thing doesn't work -> reoload -> DOESN'T WORK
        print('new loop')
        logInFile.time.sleep(15)
        # logInFile.browser.get(
        #     'https://s159-de.ogame.gameforge.com/game/index.php?page'
        #     '=resources')

        newTabs = logInFile.browser.window_handles

        for tab in newTabs:
            logInFile.browser.switch_to.window(tab)
            logInFile.time.sleep(1)
            logInFile.browser.find_element_by_xpath('//*[contains(text(),\'Versorgung\')]').click()

            """
            TRY: IF SOMETHIN IS BEING BUILT
            --------------------------------------------------------------------------------
            """
            try:  # looking if something is already built

                print('trying')
                if logInFile.browser.find_element_by_xpath("//span[@name='zeit']"
                                                           ""):
                    print('Busy!')
                    continue

            except Exception as e:
                print(e)
                pass

            """
            --------------------------------------------------------------------------------
            """


            """
            WHILE LOOP: DefBuildMod
            --------------------------------------------------------------------------------
            """


            while defBuildMod == True:
                try:

                    """
                    TRY: check if conditions are met and buildings are done  
                         for DefBuildMod
                    --------------------------------------------------------------------------------
                    """

                    # if int(logInFile.browser.find_element_by_xpath("//*["
                    #                                                "@ref='1']/span/span").text) == 10 and int(
                    #     logInFile.browser.find_element_by_xpath("//*["
                    #                                             "@ref='2']/span/span").text) \
                    #         == 8 and int(
                    #     logInFile.browser.find_element_by_xpath(
                    #         "//*[@ref='3']/span/span").text) == 6:
                    #     logInFile.browser.find_element_by_xpath("//*["
                    #                                             "@class='textlabel' "
                    #                                             "and "
                    #                                             "contains("
                    #                                             "text(),"
                    #                                             "'Anlagen')]").click()
                    #
                    #     if int(logInFile.browser.find_element_by_xpath("//*["
                    #                                                    "@ref='14']/span/span").
                    #                    text) < 2:
                    #         logInFile.browser.find_element_by_xpath(
                    #             "//*[@ref='14']").click()
                    #         logInFile.time.sleep(2)
                    #         logInFile.browser.find_element_by_xpath("//*[ "
                    #                                                 "@id='content']/div["
                    #                                                 "2]/a/span["
                    #                                                 "contains("
                    #                                                 "text(),  "
                    #                                                 "'Ausbauen')]") \
                    #             .click()
                    #
                    #
                    #     elif int(logInFile.browser.find_element_by_xpath("//*["
                    #                                                      "@ref='14']/span/span").
                    #                      text) == 2 and int(
                    #         logInFile.browser.find_element_by_xpath("//*["
                    #                                                 "@ref='21']/span/span").
                    #                 text) < 1:
                    #         logInFile.browser.find_element_by_xpath(
                    #             "//*[@ref='21']").click()
                    #         logInFile.time.sleep(2)
                    #         logInFile.browser.find_element_by_xpath("//*[ "
                    #                                                 "@id='content']/div["
                    #                                                 "2]/a/span["
                    #                                                 "contains("
                    #                                                 "text(),  "
                    #                                                 "'Ausbauen')]") \
                    #             .click()
                    #
                    #
                    #     elif int(logInFile.browser.find_element_by_xpath("//*["
                    #                                                      "@ref='14']/span/span").
                    #                      text) == 2 and int(
                    #         logInFile.browser.find_element_by_xpath("//*["
                    #                                                 "@ref='21']/span/span").
                    #                 text) == 1:
                    #         logInFile.browser.find_element_by_xpath("//*["
                    #                                                 "@class='textlabel' "
                    #                                                 "and "
                    #                                                 "contains("
                    #                                                 "text(),"
                    #                                                 "'Verteidigung')]").click()



                    """
                    TRY/IF: check how many def is built and give 
                    build commands --> STILL NEED TO DO CLICKING 
                    PROBLEM WHILE SOMEHING IS BEING BUILT ALREADY   
                    --------------------------------------------------------------------------------
                    """

                    if int(logInFile.browser.find_element_by_xpath(
                            "//*["
                            "@ref='401']/span/span").
                                   text) < 2 * defBuildModActivator:
                        # defBuildMod = True
                        try:
                            if logInFile.browser.find_element_by_xpath(
                                    "//*["
                                    "@id='shipcount']").text:
                                print("try")
                                logInFile.browser.find_element_by_xpath(
                                    "//*[@class='item_box defense401 "
                                    "tooltip "
                                    "js_hideTipOnMobile']").click()
                                logInFile.time.sleep(2)
                                amountToBuild = 20 - int(
                                    logInFile.browser.find_element_by_xpath(
                                        "//*["
                                        "@ref='401']//*["
                                        "@id='bestand']").
                                        text) - \
                                                logInFile.browser.find_element_by_xpath(
                                                    "//*["
                                                    "@id='shipcount']").text
                                print(str(amountToBuild))

                                logInFile.browser.find_element_by_xpath(
                                    "//input["
                                    "@class='amount_input']").click()
                                logInFile.browser.find_element_by_xpath(
                                    "//*["
                                    "@class='amount_input']").send_keys(
                                    amountToBuild)
                                logInFile.time.sleep(2)
                                logInFile.browser.find_element_by_xpath(
                                    "//*["
                                    "@id='content']/div["
                                    "3]/a/span["
                                    "contains("
                                    "text(),  "
                                    "'In')]").click()
                        except:
                            print("except")
                            logInFile.browser.find_element_by_xpath(
                                "//*[@ref='401']").click()
                            logInFile.time.sleep(2)
                            amountToBuild = str(20 - int(
                                logInFile.browser.find_element_by_xpath(
                                    "//*["
                                    "@ref='401']//*["
                                    "@class='level']").text))
                            logInFile.browser.find_element_by_xpath(
                                "//input["
                                "@class='amount_input']").click()
                            logInFile.time.sleep(4)
                            logInFile.browser.find_element_by_xpath(
                                "//input["
                                "@class='amount_input']").send_keys(
                                amountToBuild)
                            logInFile.time.sleep(4)
                            logInFile.browser.find_element_by_xpath(
                                "//*["
                                "@id='content']/div["
                                "3]/a/span["
                                "contains("
                                "text(),  "
                                "'Bauen')]").click()
                            continue
                    else:
                        defBuildMod = False
                        continue
                    continue

                except Exception as e:
                    print(str(e))
                    pass

            """
            IF: Mine building section   
            --------------------------------------------------------------------------------
            """


            defBuildModActivator = int(logInFile.browser.find_element_by_xpath("//*["
                                                                   "@ref='1']/span/span").text) + int(
                        logInFile.browser.find_element_by_xpath("//*["
                                                                "@ref='2']/span/span").text) \
                            + int(logInFile.browser.find_element_by_xpath("//*[@ref='3']/span/span").text)

            try:
                if defBuildModActivator == 39:
                    defBuildMod = False
                    print('DEF BUILD MODUS ACTIVATED!')


                try:
                    logInFile.time.sleep(1)
                    if logInFile.browser.find_element_by_xpath("//span["
                                                               "@id='resources_crystal' and @class='overmark']"):
                        logInFile.browser.find_element_by_xpath(
                            "//*[@ref='23']").click()
                        logInFile.time.sleep(2)
                        logInFile.browser.find_element_by_xpath("//*["
                                                                "contains("
                                                                "text(),  "
                                                                "'Ausbauen')]") \
                            .click()
                except Exception as e:
                    print(e)
                    pass
                    print("5")
                try:
                    logInFile.time.sleep(1)
                    if logInFile.browser.find_element_by_xpath(("//*["
                                                                "@id= "
                                                                "'resources_metal' and @class='overmark']")):
                        logInFile.browser.find_element_by_xpath(
                            "//*[@ref='22']").click()
                        logInFile.time.sleep(2)
                        logInFile.browser.find_element_by_xpath("//*["
                                                                "contains("
                                                                "text(),  "
                                                                "'Ausbauen')]") \
                            .click()
                except Exception as e:
                    print(e)
                    pass
                    print("6")
                try:
                    logInFile.time.sleep(1)
                    if logInFile.browser.find_element_by_xpath((
                            "//span[@id='resources_deuterium' and "
                            "@class='overmark']")):
                        logInFile.browser.find_element_by_xpath(
                            "//*[@ref='24']").click()
                        logInFile.time.sleep(2)
                        logInFile.browser.find_element_by_xpath("//*["
                                                                "contains("
                                                                "text(),  "
                                                                "'Ausbauen')]") \
                            .click()
                except:
                    pass

                if int((logInFile.browser.find_element_by_xpath("//*["
                                                                "@id='resources_energy']")).text) < 0:
                    logInFile.browser.find_element_by_xpath("//*[@ref='4']").click()
                    logInFile.time.sleep(2)
                    logInFile.browser.find_element_by_xpath("//*[contains"
                                                            "(text(),'Ausbauen')]") \
                        .click()
                    print("1")

                elif int(logInFile.browser.find_element_by_xpath("//*["
                                                                 "@ref='2']/span/span").
                                 text) - int(logInFile.browser.find_element_by_xpath
                                                 ("//*[@ref='1']/span/span")
                                                     .text) > -2 and int(
                    (logInFile.browser.find_element_by_xpath("//*["
                                                             "@id='resources"
                                                             "_energy']")).text) > 0:
                    logInFile.browser.find_element_by_xpath("//*[@ref='1']").click()
                    logInFile.time.sleep(2)
                    logInFile.browser.find_element_by_xpath("//*[contains("
                                                            "text(),  'Ausbauen')]") \
                        .click()
                    print("2")
                    # and (int(webElements.levelOfDeutMineOnTooltip.text) - int(
                    #  webElements.levelOfCrystalMineOnTooltip.text)) >= \
                    # -2 \


                elif int(logInFile.browser.find_element_by_xpath("//*["
                                                                 "@ref='2']/span/span").text) - \
                        int(logInFile.browser.find_element_by_xpath(
                            "//*[@ref='1']/span/span").text) < -2 and \
                        int((logInFile.browser.find_element_by_xpath("//*["
                                                                     "@id="
                                                                     "'resources_energy']"))
                                    .text) > 0:
                    logInFile.browser.find_element_by_xpath("//*[@ref='2']").click()
                    logInFile.time.sleep(2)
                    logInFile.browser.find_element_by_xpath("//*[ "
                                                            "@id='content']/div["
                                                            "2]/a/span[contains("
                                                            "text(),  'Ausbauen')]") \
                        .click()
                    print("3")


                elif int(logInFile.browser.find_element_by_xpath("//*[@ref='3']/span"
                                                                 "/span").text) - \
                        int(logInFile.browser.find_element_by_xpath("//*["
                                                                    "@ref='2']/span/"
                                                                    "span").text) < \
                        -2 and \
                        int((logInFile.browser.find_element_by_xpath("//*[@id="
                                                                     "'resources_energy']"))
                                    .text) > 0:
                    logInFile.browser.find_element_by_xpath("//*[@ref='3']").click()
                    logInFile.time.sleep(2)
                    logInFile.browser.find_element_by_xpath("//*[ "
                                                            "@id='content']/div["
                                                            "2]/a/span[contains("
                                                            "text(),  'Ausbauen')]") \
                        .click()
                    print("4")



                    """
                    ELSE/TRY: Storage building section when storages are full   
                     --------------------------------------------------------------------------------
                    """

                else:
                    print(e)
                    print("7")
                    print("everything pass")
                    logInFile.browser.find_element_by_xpath("//*[@ref='1']").click()
                    logInFile.time.sleep(2)
                    logInFile.browser.find_element_by_xpath("//*[ "
                                                            "@id='content']/div["
                                                            "2]/a/span[contains("
                                                            "text(),  "
                                                            "'Ausbauen')]") \
                        .click()

                    pass
            except:
                pass

    except Exception as e:
        print(e)
        try:
            continue
        except:
            logInFile.logIn()

"""
--------------------------------------------------------------------------------

"""
