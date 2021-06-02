from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

def send_delayed_keys(element, text, delay=0.01): #text yazarken yavaşlatma fonksiyonu
    """Send a text to an element one character at a time with a delay."""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

url= "https://10fastfingers.com/login"
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()

email_giris = driver.find_element_by_xpath("//*[@id='UserEmail']")
email_giris.send_keys("torerohdd@gmail.com")
time.sleep(2)

sifre_giris= driver.find_element_by_xpath("//*[@id='UserPassword']")
sifre_giris.send_keys("memleket12")
time.sleep(2)

girisbuton=driver.find_element_by_xpath("//*[@id='login-form-submit']")
girisbuton.click()
time.sleep(2)

anticheaturl= "https://10fastfingers.com/anticheat/view/1/1"
driver.get(anticheaturl)
time.sleep(1)
antibuton=driver.find_element_by_xpath("//*[@id='start-btn']")
antibuton.click()

time.sleep(1)


image = pyautogui.screenshot(region=(554,280, 620, 160))

ocr= "ocr.jpg"

image.save(ocr)


resim= "C:\\Users\\Administrator\\Desktop\\selenium\\ocr.jpg"

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1]) #yeni bir pencere açma

url3="https://www.onlineocr.net/"
driver.get(url3)

upload = driver.find_element_by_xpath("//*[@id='fileupload']")
upload.send_keys(resim)

#languageselect= driver.find_element_by_xpath("//select[@name='ctl00$MainContent$comboLanguages']/option[text()='TURKISH']").click()#if turkish

optionselect= driver.find_element_by_xpath("//select[@name='ctl00$MainContent$comboOutput']/option[text()='Text Plain (txt)']").click()
time.sleep(0.7)
buttons = driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)
copytext= driver.find_element_by_xpath("//*[@id='MainContent_txtOCRResultText']").text
driver.close()

driver.switch_to.window(driver.window_handles[0]) #ana pencereye dönüş



fastfingerinput=driver.find_element_by_xpath("//*[@id='word-input']")
send_delayed_keys(fastfingerinput, copytext, 0.01)#girilecek text area , girilecek text, delay


antisumbit=driver.find_element_by_xpath("//*[@id='submit-anticheat']").click()




time.sleep(100)