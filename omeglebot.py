from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time


driver = webdriver.Firefox()
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)


start_url = "https://omegle.com/"
driver.get(start_url)

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
textbutton = driver.find_element_by_xpath('//*[@id="textbtn"]')
textbutton.click()
agree1 = driver.find_element_by_xpath('/html/body/div[7]/div/p[1]/label/input')
agree1.click()
agree2 = driver.find_element_by_xpath('/html/body/div[7]/div/p[2]/label/input')
agree2.click()
agree3 = driver.find_element_by_xpath('/html/body/div[7]/div/p[3]/input')
agree3.click()

def messagesend():
    time.sleep(1)
    try:
        message = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')
        message.click()
        time.sleep(1)
        message.send_keys("f19 selling my feet/whole body content (custom/premade) on snap: real_issabella add me for preview, verification and menu!")
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



#driver.maximize_window()


