from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def init_driver():
    driver_path = "D:\projects for DS\whatsapp message sender\chromedriver.exe"
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_whatsapp(driver):
    driver.get('https://web.whatsapp.com')
    input("Press Enter after scanning the QR code and logging in on WhatsApp Web.")

def send_whatsapp_message(driver, contact, message):
    try:
        search_box = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)
        
        # Wait for the chat to load
        time.sleep(3)

        # Locate the message input box using the provided full XPath
        message_box = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
        )
        message_box.click()  # Ensure the box is in focus
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        # Wait a bit before sending the next message
        time.sleep(2)

    except Exception as e:
        print(f"Failed to locate message box or send message to contact: {contact}. Error: {e}")

def close_driver(driver):
    driver.quit()
