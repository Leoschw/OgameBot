import classes as c
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def findTech(item):
    (c.wait.until(
            EC.presence_of_element_located(
                    (By.XPATH, ('//*[contains(@id="href",\'https://s158-de.ogame.gameforge.com'
                                '/game\
                                /index.php?page=techtree&tab=2&techID'
                                '=113\')]')))).click()).wait.until(
            EC.presence_of_element_located(
                    (By.XPATH, ('//*[contains(@id="href", \'Technik\')]')))).click(

            ).wait.until(
            EC.presence_of_element_located((By.XPATH, (
                '//*[@id="technology"]/div/h3[contains(text(),\'{}}\']').format(
                    item.techTree)))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, (
        '//*[@id="technology"]/div/div[5]/table/tbody/tr[2]/td[1]/a/[contains(text('
        '),\'{}\')]//ancestor::td[2]/a/ul/li[1]').format(item.name))))