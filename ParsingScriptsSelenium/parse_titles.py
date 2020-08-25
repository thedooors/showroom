import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

selectservice_list = ["hbo", "netflix", "apple-tv", "fx", "amc", \
    "amazon", "showtime", "disney", "the-cw", "abc", "syfy", \
        "bbc", "cbs", "fox", "hulu"]
options = webdriver.ChromeOptions()
options.add_extension('extension_1_4_3_0.crx')
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
# Link_Names - array of links and titles of shows (Unique) 
link_names = []
for selectservice in selectservice_list:
    driver.get("https://www.kp.ru/putevoditel/serialy/" + selectservice + "/")
    next_page_exist = True
    while(next_page_exist):
        try:
            grid_of_page = driver.find_elements_by_xpath("//div[@class='large-4 medium-4 small-6 cell']")
            for link_name in grid_of_page:
                title = link_name.find_element_by_xpath('.//span[@class="serial-related_title"]').text
                link = link_name.find_element_by_xpath('.//a[@class="serial-related_wrapper"]').get_attribute('href')

                link_names.append({'title': title, 'link': link, 'selectservice': selectservice.upper()})
        except NoSuchElementException:
            print("Nothing found - check linking")
        try:
            nxt = driver.find_element_by_class_name('next').get_attribute('href')
            driver.get(nxt)
        except NoSuchElementException:
            next_page_exist = False
print("Всего изначально - " + str(len(link_names)))
# Обрезаем повторы - Линейно по времени и памяти - но так как это единственная операция, то не критично
result = list({d['title']: d for d in link_names}.values())
print("После удаления дубликатов - " + str(len(result)))
print("Сохраняем showlist.json:")
with open('showlist.json', 'w') as f:
    json.dump(result, f)
print("Завершение работы...")