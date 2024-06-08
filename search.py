import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

def scrape_bing(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(f"https://www.bing.com/search?q={query}")

    time.sleep(5)

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
    
    driver.quit()

    return links[:10]

def fetch_content(url):
    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, "html.parser")
        paragraphs = soup.find_all('p')
        page_text = " ".join([para.get_text() for para in paragraphs])
        return page_text
    except Exception as e:
        return f"Error fetching content from {url}: {e}"
