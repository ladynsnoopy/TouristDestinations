from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys

with open(r'C:\Users\S510\PycharmProjects\ToursitDest\tourdestination\countrynames.csv', newline='') as csvfile:
    country_names = []
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        country_name = str(row[0])
        if i == 0:
            pass
        else:
            country_names.append(country_name)
        i += 1
k = 0
rows_list = []
for country in country_names:
    search_query = country_names[k]+" attractions"
    driver = webdriver.Chrome(r"C:\Users\S510\PycharmProjects\ToursitDest\Drivers\chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("https://www.tripadvisor.com.sg/")
    driver.find_element_by_class_name("_3qLQ-U8m").send_keys(search_query)
    driver.find_element_by_class_name("_3qLQ-U8m").send_keys(Keys.ENTER)
    attraction_categories = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "filter_list_0", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "filterName", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "taLnk", " " ))]')
    for category in attraction_categories:
        weblink = category.get_attribute('href')
        url = []
        url.append(weblink)
        url.append(country_names[k])
        rows_list.append(url)
    k += 1
    driver.quit()
with open('weblinks.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows_list)





