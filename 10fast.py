from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_delayed_keys(element, text, delay=0.03): #text yazarken yavaşlatma fonksiyonu
    for character in text:
        element.send_keys(character)
        time.sleep(delay)




options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

url= "https://10fastfingers.com/login"
driver.get(url)
time.sleep(1)

driver.find_element_by_xpath("//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()

email_giris = driver.find_element_by_xpath("//*[@id='UserEmail']")
email_giris.send_keys("mail")
time.sleep(1)

sifre_giris= driver.find_element_by_xpath("//*[@id='UserPassword']")
sifre_giris.send_keys("pass")
time.sleep(1)

girisbuton=driver.find_element_by_xpath("//*[@id='login-form-submit']")
girisbuton.click()
time.sleep(2)

driver.get("https://10fastfingers.com/typing-test/english") #change typing test url or stay
time.sleep(1)

i=1
yazigiris=driver.find_element_by_xpath("//*[@id='inputfield']")


while i<250:
    kelime= driver.find_element_by_xpath("//*[@id='row1']/span["+str(i)+"]").text

    i += 1
    print(kelime)
    send_delayed_keys(yazigiris, kelime, 0.03)#girilecek text area , girilecek text, delay
    driver.find_element_by_xpath("//*[@id='inputfield']").send_keys(Keys.SPACE)
    





time.sleep(200)