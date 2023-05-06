import time
import urllib.request
import os
from selenium import webdriver


def play(img):
    """
    img : 이미지 주소
    answer : 해당 이미지를 크롤링해서 나온 점자
    """

    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    path = r"C:\Users\j3hea\OneDrive\바탕 화면\Python-CapstonDesign-main\Kyebraiile\main\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://angelina-reader.ru/")
    driver.find_element_by_css_selector(
        "body > div.site-wrapper > div.site-wrapper__top > div > main > div.site-block.load-block > div:nth-child(8) > div:nth-child(1) > label").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector(
        "#file-input_loadpc").send_keys(img)

    time.sleep(0.5)
    answer = driver.find_element_by_css_selector(
        "body > div.site-wrapper > div.site-wrapper__top > div.site-content.site-content_result_1and2.container > div.site-content__col.site-content__col_tline > div > div:nth-child(2) > div > div > tt").text
    time.sleep(0.5)
    
    return answer
