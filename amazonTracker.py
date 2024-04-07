# import requests
# from bs4 import BeautifulSoup

# AMAZON_URL = "https://www.amazon.com/-/zh_TW/Matthes%EF%BC%89-%E7%BE%8E-%E5%9F%83%E9%87%8C%E5%85%8B%C2%B7%E9%A9%AC%E7%91%9F%E6%96%AF%EF%BC%88Eric/dp/B01ION3VWI/ref=sr_1_2?crid=29YFNQPUBQNRM&dib=eyJ2IjoiMSJ9.rc6_IQYJBSFEdWiTtnjUpeOhfI_J14bEVdFJ3JFS4zOu3KfyblTl_V9dg9ADw8oBQuRewMcH1kunfOV2zb4H-EkBsD6Jc9PZnbzL9BupUXWk8taARegdlbyVKrSBM6Ev2LPMwqZVTrgTufDgX9IJosd8gXffwlqHoBrec5-nyjwimneE3ScOw8ervjoFuhQqhkp7V6L5whDc6WG_uaeCHy4sGTNSUelB6QBHxy9ttGTZD_VLrOvm0K3TFBdDQHbp2eIKydyGuRyPXzEnqqZYZKmFQgSW4zNheUJGiJR0EGQ.fxydwb1LOPUhfZdWvgTlef_b5aYUwmK45apYaYZ0OO0&dib_tag=se&keywords=python&qid=1712483171&refinements=p_n_feature_nine_browse-bin%3A3291442011&rnid=3291435011&s=books&sprefix=pyth%2Caps%2C255&sr=1-2"

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
# }

# def amazon_tracking_price():
#     amazon_page = requests.get(AMAZON_URL, headers=headers)
#     soup = BeautifulSoup(amazon_page.content,'html.parser')
#     title = soup.find(id='productTitle')
#     print(title)

# amazon_tracking_price()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

AMAZON_URL = "https://www.amazon.com/-/zh_TW/Matthes%EF%BC%89-%E7%BE%8E-%E5%9F%83%E9%87%8C%E5%85%8B%C2%B7%E9%A9%AC%E7%91%9F%E6%96%AF%EF%BC%88Eric/dp/B01ION3VWI/ref=sr_1_2?crid=29YFNQPUBQNRM&dib=eyJ2IjoiMSJ9.rc6_IQYJBSFEdWiTtnjUpeOhfI_J14bEVdFJ3JFS4zOu3KfyblTl_V9dg9ADw8oBQuRewMcH1kunfOV2zb4H-EkBsD6Jc9PZnbzL9BupUXWk8taARegdlbyVKrSBM6Ev2LPMwqZVTrgTufDgX9IJosd8gXffwlqHoBrec5-nyjwimneE3ScOw8ervjoFuhQqhkp7V6L5whDc6WG_uaeCHy4sGTNSUelB6QBHxy9ttGTZD_VLrOvm0K3TFBdDQHbp2eIKydyGuRyPXzEnqqZYZKmFQgSW4zNheUJGiJR0EGQ.fxydwb1LOPUhfZdWvgTlef_b5aYUwmK45apYaYZ0OO0&dib_tag=se&keywords=python&qid=1712483171&refinements=p_n_feature_nine_browse-bin%3A3291442011&rnid=3291435011&s=books&sprefix=pyth%2Caps%2C255&sr=1-2"

def amazon_tracking_price():
    # 初始化WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get(AMAZON_URL)
    time.sleep(5)  # 等待JavaScript加載
    
    try:
        title = driver.find_element(By.ID, 'productTitle').text
        print(title)
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

amazon_tracking_price()