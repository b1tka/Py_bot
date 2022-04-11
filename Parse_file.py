import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime as dt
import time

url = 'https://giseo.rkomi.ru/about.html'


class Parse:
    def __init__(self, user, password, cur_w):
        self.user = user
        self.password = password
        self.cur_w = cur_w
        print(self.cur_w)

    def schedule(self):
        driver = webdriver.Chrome(executable_path='D:\\Py_bot\\chromedriver\\chromedriver.exe')
        try:
            driver.get(url=url)
            time.sleep(1)
            school_input = Select(driver.find_element_by_id('schools'))
            school_input.select_by_visible_text('МАОУ "Гимназия им. А.С. Пушкина"')
            name_input = driver.find_element_by_name('UN')
            name_input.send_keys(self.user)
            password_input = driver.find_element_by_name('PW')
            password_input.send_keys(self.password)
            button = driver.find_element_by_xpath('//*[@id="message"]/div/div/div[12]/a/span')
            button.click()
            time.sleep(1)
            try:
                button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[4]/div/div/div/div/button[2]')
                button.click()
            finally:
                time.sleep(0.5)
                dinary_button = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[2]/a')
                dinary_button.click()
                time.sleep(0.5)
                dinary_button = driver.find_element_by_xpath('/html/body/div[1]/div[4]/nav/ul/li[2]/ul/li[3]/a')
                dinary_button.click()
                time.sleep(0.5)
                page = BeautifulSoup(driver.page_source, 'lxml')
                shedule = page.find('table', class_='schedule-table table table-bordered table-condensed print-block').find_all(
                    'tr')
                clear_shedule = shedule[self.cur_w]
                s = clear_shedule.find_all('td')[1]
                ready_shedule = list()
                for item in s:
                    if 'Англ.яз' in item:
                        ready_shedule.append('Англ.яз')
                    elif 'франц' in item or 'немец' in item:
                        ready_shedule.append('Французский|Немецкий')
                    elif item.text != '':
                        ready_shedule.append(item.text)
                for i in range(len(ready_shedule)):
                    ready_shedule[i] = f'{str(i + 1)}) ' + ready_shedule[i]
                return '\n'.join(ready_shedule)
        except:
            return 'Ошибка'
        finally:
            driver.close()
            driver.quit()
