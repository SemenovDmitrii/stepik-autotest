import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("")
input1 = driver.find_element(By.ID, "")
input1.send_keys("")
input2 = driver.find_element(By.ID, "")
input2.send_keys("")
button = driver.find_element(By.ID, "")
button.click()
time.sleep(30)
driver.quit()



import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(30)
browser.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла
driver.findElement(By.xpath("//button[normalize-space()='Submit']"))



# Код по заполнению обязательных полей, и проверка успешной авторизации
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")

input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
input3.send_keys("Smolensk@mail.ru")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10)
browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("Мой ответ")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
url = 'https://google.com'
try:
    # open google.com
    browser.get(url)
    search = browser.find_element_by_tag_name('input')

    # search request for OZON.ru
    search.send_keys('ozon.ru')
    search.send_keys(Keys.RETURN)

    # locate by partial link and open ozon.ru
    browser.find_element_by_partial_link_text('OZON — интернет-магазин').click()
    # sleep(5)
    wait = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "div[type='addToCartButton']"))

    prod_1 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(3) div[type='addToCartButton']").click()

    prod_2 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(4) div[type='addToCartButton']").click()

    prod_3 = browser.find_element_by_css_selector(
        "div.a1p4.a3j0.a1p6.co7.cp1:nth-child(5) div[type='addToCartButton']").click()

    cart = browser.find_element_by_css_selector("a[href='/cart/']").click()
    wait1 = WebDriverWait(browser, 20).until(EC.element_to_be_selected(By.CSS_SELECTOR, '.container:nth-child(3) .a7m4'))
    goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')

    print(goods)
    print(len(goods))

    assert len(goods) == 3, 'в корзине не 3 вещи'
finally:
    sleep(2)
    browser.close()
    browser.quit()
    
    
    
    
    
import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

txt = browser.find_element(By.ID,'input_value')
x = txt.text
print(x)
y = calc(x)
print(y)

option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()

button = browser.find_element(By.CSS_SELECTOR, "btn.btn-default").click()

time.sleep(60)
browser.quit()







import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
x = x_element.text

y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()

butSubmit = browser.find_element(By.CLASS_NAME, value='btn.btn-default').click()

time.sleep(60)
browser.quit()





import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()

butSubmit = browser.find_element(By.CLASS_NAME, value='btn.btn-default').click()

time.sleep(60)
browser.quit()


















import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "num1").text
y = browser.find_element(By.ID, "num2").text
sum1 = str(int(x) + int(y))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(sum1)

butSubmit = browser.find_element(By.CLASS_NAME, value='btn.btn-default').click()

time.sleep(30)
browser.quit()







import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

browser.execute_script("window.scrollBy(0, 150);")

option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()

button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(30)
browser.quit()






from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("Smolensk@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

time.sleep(30)
browser.quit()









import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
confirm = browser.switch_to.alert.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(30)
browser.quit()







import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
confirm = browser.switch_to.alert.accept()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(30)
browser.quit()









import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.ID, 'book').click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input2 = browser.find_element(By.ID, "answer")
input2.send_keys(y)

button = browser.find_element(By.ID, 'solve').click()

#print(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(30)
browser.quit()





# mozila
import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
confirm = browser.switch_to.alert.accept()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(30)
browser.quit()