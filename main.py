from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=0).install())
link = "https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itm2644c3764fc54?pid=MOBFKCTSHAWGGFHM&lid=LSTMOBFKCTSHAWGGFHMCPQSMX&marketplace=FLIPKART&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&fm=organic&iid=505d8cab-debd-4157-8157-c6c910875182.MOBFKCTSHAWGGFHM.SEARCH&ssid=cie4w1suy80000001601195482047&qH=7b7504afcaf2e1ea"
driver.get(link)

timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'container'))
    WebDriverWait(driver, timeout).until(element_present)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    name = soup.find('span', attrs={'class': '_35KyD6'}).text
    price = soup.find('div', attrs={'class': '_3qQ9m1'}).text
    description = soup.find('div', attrs={'class': '_38NXIU'}).text
    rating = soup.find('div', attrs={'class': '_1i0wk8'}).text
    comment = soup.find('div', attrs={'class': 'qwjRop'}).text
    result = {
        "product_name" : name,
        "product_link" : link,
        "product_price" : price,
        "product_description" : description,
        "product_rating" : rating,
        "review_comment" : comment,
    }
    print(result)
except TimeoutException:
    print("Timed out waiting for page to load")