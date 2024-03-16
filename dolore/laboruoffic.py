import re
import time
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def fix_lavamoat(driver: webdriver.Chrome, url: str, email: str, password: str):
    """
    This function fixes the lavamoat captcha by clicking on the correct images.

    Args:
        driver (webdriver.Chrome): The selenium webdriver instance.
        url (str): The URL of the website with the lavamoat captcha.
        email (str): The email address to use for logging in.
        password (str): The password to use for logging in.
    """

    # Go to the URL
    driver.get(url)

    # Wait for the login button to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))

    # Click on the login button
    driver.find_element(By.ID, "login-button").click()

    # Wait for the email field to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    # Enter the email address
    driver.find_element(By.ID, "email").send_keys(email)

    # Enter the password
    driver.find_element(By.ID, "password").send_keys(password)

    # Click on the login button
    driver.find_element(By.ID, "login-button").click()

    # Wait for the lavamoat captcha to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lavamoat-container")))

    # Get the images from the lavamoat captcha
    images = driver.find_elements(By.CLASS_NAME, "lavamoat-image")

    # Click on the correct images
    for image in images:
        if image.get_attribute("data-correct") == "true":
            image.click()

    # Wait for the captcha to be solved
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "lavamoat-container")))
