from selenium import webdriver ##library to automate the web browser
from selenium.webdriver.common.keys import Keys ##to send special keys from keyboard
from pytesseract import image_to_string ##This is for solving captcha (I love this)
from PIL import Image ## python imaginging library for pytesseract dependencies
import time ##library for delay 

driver = webdriver.Chrome()  ##put chrome driver in the same directory as your python script 
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf") ## our url 
driver.find_element_by_id('usernameId').clear()
driver.find_element_by_id('usernameId').send_keys("xxxxxxx") ##input your username here.
driver.find_element_by_name('j_password').clear()
driver.find_element_by_name('j_password').send_keys("xyxyxyxysysysj") ## input your password here.

# now that we have the preliminary stuff out of the way time to get that image :D
element = driver.find_element_by_id('cimage') # find part of the page you want image of
location = element.location
size = element.size
driver.save_screenshot('screenshot.png') # saves screenshot of entire page

im = Image.open('screenshot.png') # uses PIL library to open image in memory
##crop according to the size of captcha image
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom)) # defines crop points

#solve the captcha using pytesseract engine
image_text = image_to_string(im)
image_text = image_text.replace(" " , "").upper()
##enter the captcha in the field
driver.find_element_by_name('j_captcha').clear()
driver.find_element_by_name('j_captcha').send_keys(image_text)
im.close()
time.sleep(4) ##this is necessary as it makes the server believe that you are a human :D
driver.find_element_by_id('loginbutton').click()

driver.find_element_by_id('jpform:fromStation').clear()
driver.find_element_by_id('jpform:fromStation').send_keys('GWALIOR - GWL') ##Enter your source station here.
driver.find_element_by_id('jpform:toStation').clear()
driver.find_element_by_id('jpform:toStation').send_keys('H NIZAMUDDIN - NZM') ##Enter your destination station here.
driver.find_element_by_id('jpform:journeyDateInputDate').send_keys('20-07-2017') ##Your journey date.
driver.find_element_by_id('jpform:jpsubmit').click()
driver.find_element_by_id('cllink-12279-2S-1').click() ## I have selected sleeper coach. you can change if you want.
time.sleep(10) ##This is for clicking on book now option and enter your passenger name.
## click on book now.
drver.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnAge"]').send_keys('22')
driver.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnGender"]/option[2]').click()
driver.find_element_by_xpath('//*[@id="addPassengerForm:autoUpgrade"]').click()
driver.find_element_by_xpath('//*[@id="addPassengerForm:mobileNo"]').send_keys('xxxxxxxxx') ##enter your mobile nummber
time.sleep(6) ##solve the captcha (I am working on this part of code now. The captcha has dymanic id.)
driver.find_element_by_xpath('//*[@id="validate"]').click()
