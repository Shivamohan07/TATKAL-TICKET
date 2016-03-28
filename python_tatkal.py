# TATKAL-TICKET
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, strftime

def waituntil(s):
    while strftime('%H:%M:%S') < s:
        print strftime('%H:%M:%S')
        sleep(1)

def login():
    driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, 'j_username'))
        ).send_keys(IRCTC_USERNAME)
    driver.find_element_by_name('j_password').send_keys(IRCTC_PASSWORD)
    driver.find_element_by_name('j_captcha').send_keys('')

def planjourney():
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'jpform:fromStation'))
        ).send_keys(FROM_STATION)
    driver.find_element_by_id('jpform:toStation').send_keys(TO_STATION)
    driver.find_element_by_id('jpform:journeyDateInputDate').send_keys(DATE)
    #waituntil('10:00:05')
    driver.find_element_by_id('jpform:jpsubmit').click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.NAME, 'quota'))
        )[0].click()
    driver.find_element_by_id('cllink-%s-%s-%s' % (TRAIN_NO, CLASS, CLASS_INDEX)).click()
    # WebDriverWait(driver, 60).until(
    #     EC.presence_of_all_elements_located((By.ID, '%s-%s-CK-0' % (TRAIN_NO, CLASS)))
    #     )[-1].click()

def filldetails():
    WebDriverWait(driver, 60).until(EC.title_contains('Book Ticket'))
    for name, el in zip(NAMES, driver.find_elements_by_class_name('psgn-name')):
        el.send_keys(name)
    for age, el in zip(AGES, driver.find_elements_by_class_name('psgn-age')):
        el.send_keys(age)
    for gender, el in zip(GENDERS, driver.find_elements_by_class_name('psgn-gender')):
        Select(el).select_by_value(gender)
    for berth, el in zip(BERTHS, driver.find_elements_by_class_name('psgn-berth-choice')):
        Select(el).select_by_value(berth)
    

def sbi():
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.ID, 'PREFERRED'))
        )[-1].click()
    driver.find_element_by_id('validate').click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'debitCardNumber'))
        ).send_keys(SBI_CARD_NUMBER)
    driver.find_element_by_id('debitCardholderName').send_keys(SBI_CARD_NAME)
    driver.find_element_by_id('debiMonth').send_keys(SBI_CARD_EXPIRY_MM)
    driver.find_element_by_id('debiYear').send_keys(SBI_CARD_EXPIRY_YYYY)
    driver.find_element_by_id('cardPin').send_keys(SBI_CARD_PIN)
    #for MONTH, el in zip(SBI_CARD_EXPIRY_MM, driver.find_elements_by_class_name('tbox')):
        #Select(el).select_by_value(MONTH)
    


IRCTC_USERNAME = 'IRCTC_USERNAME'  #Enter you irctc username
IRCTC_PASSWORD = 'IRCTC_PASS'  #Enter you irctc password
FROM_STATION = 'LUCKNOW NR - LKO' #Enter the name of the boarding station.
FROM_STATION_CODE = 'LKO'
TO_STATION = 'PRAYAG - PRG' #Enter the name of the deboarding station.
TO_STATION_CODE = 'PRG'
DATE = '27-03-2016'   #Enter the date of journey
TRAIN_NO = '14210'   #Enter the train number
CLASS = 'CC'         #Enter the class
CLASS_INDEX = '0'    #Enter the class index that you will find the source code 
NAMES = ['NAME1'] #Passenger name list
AGES = ['20']            #Passenger age list
GENDERS = ['M']          #Passenger sex list
BERTHS = ["  "]          #Passenger preference list. Double space represent no preference.    
''
SBI_CARD_NUMBER = ''
SBI_CARD_EXPIRY_MM=''
SBI_CARD_EXPIRY_YYYY=''
SBI_CARD_PIN='ATM'   #ATM PIN
SBI_CARD_NAME=''  

if __name__ == '__main__':
    profile = webdriver.FirefoxProfile()
    profile.set_preference('webdriver.load.strategy', 'unstable')
    #waituntil('10:00:05')
    driver = webdriver.Firefox(profile)
    login()
    planjourney()
    filldetails()
    sbi()
