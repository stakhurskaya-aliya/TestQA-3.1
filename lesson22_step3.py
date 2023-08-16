import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome() #загружаем браузер
browser.get(link) #вставляем ссылку

num_1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text #находим элекмент  с 1 цифрой
num_1 = int(num_1) #получаем элемент с 1 числом и переволим в инт
num_2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text #находим элекмент  с 2 цифрой
num_2 = int(num_2) #получаем элемент с 1 числом и переволим в инт
value = str(num_1 + num_2) #получаем строчное значение
print('num1 + num2 =', value) # складывем 1 и 2 цифру 

select = Select(browser.find_element(By.TAG_NAME, "select")) #находим выпадающий список
select.select_by_visible_text(value) # выбираем нужный элемент списка

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button') #находим кнопку
button.click() # кликаем по кнопке

# закрываем браузер после всех манипуляций
time.sleep(30)
browser.quit()