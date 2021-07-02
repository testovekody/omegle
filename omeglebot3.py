from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import threading

def druhythread():
    driver = webdriver.Firefox()
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    start_url = "https://omegle.com/"
    driver.get(start_url)

    driver.maximize_window()
    interests = driver.find_element_by_class_name("topicplaceholder")
    interests.click()
    input = driver.find_element_by_class_name("newtopicinput")
    input.send_keys("feet")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("foot")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("sole")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("soles")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("heel")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("heels")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("feet pics")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("foot pics")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("feet fetish")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("foot fetish")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("domination")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("videocalls")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("spoil")
    input.send_keys(Keys.RETURN)
    input.click()
    input.send_keys("spoiled")
    input.send_keys(Keys.RETURN)
    input.send_keys("tiktok")
    input.send_keys(Keys.RETURN)
    input.send_keys("cosplay")
    input.send_keys(Keys.RETURN)
    input.send_keys("venmo")
    input.send_keys(Keys.RETURN)
    input.send_keys("paypal")
    input.send_keys(Keys.RETURN)
    input.send_keys("cashapp")
    input.send_keys(Keys.RETURN)
    textbutton = driver.find_element_by_xpath('//*[@id="textbtn"]')
    textbutton.click()
    time.sleep(1)
    agree1 = driver.find_element_by_xpath('/html/body/div[8]/div/p[1]/label/input')
    agree1.click()
    agree2 = driver.find_element_by_xpath('/html/body/div[8]/div/p[2]/label/input')
    agree2.click()
    agree3 = driver.find_element_by_xpath('/html/body/div[8]/div/p[3]/input')
    agree3.click()

    def messagesend():
        time.sleep(1)
        try:
            message = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')
            message.click()
            time.sleep(1)
            message.send_keys(
                "Hey! Curvy f18 selling nude and feet content. I verify and give one clothed preview, taking CashApp, PayPal, Venmo and Apple Pay. Upfront payment only, snap: jasminesselling")
            message.send_keys(Keys.ENTER)
            time.sleep(5)
        except:
            try:
                time.sleep(1)
                new = driver.find_element_by_xpath("//button[contains(text(),'New')]")
                new.click()
            except:
                time.sleep(1)
                messagesend()

    def loop():
        messagesend()
        try:
            stop = driver.find_element_by_xpath("//button[contains(text(),'Stop')]")
            stop.click()
            really = driver.find_element_by_xpath("//button[contains(text(),'Really?')]")
            really.click()
            new = driver.find_element_by_xpath("//button[contains(text(),'New')]")
            new.click()
        except:
            new = driver.find_element_by_xpath("//button[contains(text(),'New')]")
            new.click()
        finally:
            loop()

    loop()
def spustacprvehothreadu():
    for i in range(3):
        threading.Thread(target=druhythread).start()
spustacprvehothreadu()



