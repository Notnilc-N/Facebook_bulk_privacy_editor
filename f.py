from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

profilepage = "https://www.facebook.com/notnilc.21.July.2001/grid"
user = ""
pswd = ""

# Log in
driver = webdriver.Firefox()
driver.get(profilepage)
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.send_keys(user)
password.send_keys(pswd)
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Log In']"))).click()
#################################################################################################################

# filter
scrolldown = ActionChains(driver).send_keys(Keys.END)
filterpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]'
filterprivacypath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[3]/div[2]/div/div/div'
filteryearpath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div[2]/div/div/div'
oldprivacy = ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
yearfilter = ActionChains(driver).send_keys(Keys.ARROW_UP * (2018-1979)).send_keys(Keys.ENTER)

donepath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[3]/div/div[2]/div[1]'

friendbuttonpath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div[1]'
endpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[5]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div'
newprivacypath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[7]/div'
privacy1path = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/span/div/span/span/div/div[1]/div[1]/img'

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filterpath))).click() # click filter
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filterprivacypath))).click() # click filter privacy
oldprivacy.perform()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filteryearpath))).click() # click filter year
yearfilter.perform()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, donepath))).click() # click done


act1 = ActionChains(driver).send_keys(Keys.TAB * 4).send_keys(Keys.ENTER)
act2 = ActionChains(driver).send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN * 6).send_keys(Keys.ENTER)
new = ActionChains(driver).send_keys(Keys.TAB * 7).send_keys(Keys.ENTER)
time.sleep(0.5)
new.perform()
time.sleep(0.1)
act2.perform()
listlength=0
i=0
endcheck = True
while i<10:
    try: 
        #WebDriverWait(driver, 2).until_not(EC.element_to_be_clickable((By.XPATH, newprivacypath))) # Wait til out of edit privacy
        time.sleep(1.25)
        act1.perform()
    except:
        act1.perform()
    
    #WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, newprivacypath))) # Wait til edit privacy loaded
    time.sleep(1.25)
    act2.perform()
    if (i>50):
        endcheck=False
    if i%6 == 0:
        time.sleep(0.1)
        privacypaths = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[position()>2]/div/div/div[2]/div/div/div/div[position()>0]/div/div/div/div/div/div[2]/div[2]/div/div[2]/span/div/span/span/div/div[1]/div[1]/img')
        oldlistlength = listlength
        listlength = len(privacypaths)
        if listlength == oldlistlength:
            endcheck=False
        #driver.get("https://www.facebook.com/notnilc.21.July.2001/grid")
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filterpath))).click() # click filter
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filterprivacypath))).click() # click filter privacy
        #oldprivacy.perform()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, filteryearpath))).click() # click filter year
        #yearfilter.perform()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, donepath))).click() # click done
        #time.sleep(10)
        #new.perform()
        #act2.perform()
    i=i+1