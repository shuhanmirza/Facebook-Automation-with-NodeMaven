import json
import time

from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_nodemaven_proxy():
    proxy_options = {
        'proxy': {
            'http': f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@gate.nodemaven.com:8080",
            'https': f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@gate.nodemaven.com:8080",
            'verify_ssl': True
        }
    }

    return proxy_options


def get_browser():
    # Create Chrome options with notification blocking
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications": 2
        }
    )
    browser = webdriver.Chrome(seleniumwire_options=get_nodemaven_proxy(), options=chrome_options)

    return browser


def accept_cookies(browser):
    try:
        # Wait for the button to be clickable (you can adjust the timeout as needed)
        cookie_button = WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[data-cookiebanner='accept_button']"))
        )

        # Click the button
        cookie_button.click()
    except TimeoutException:
        logger.warning("Cookie button click timed out")


def facebook_login(browser):
    browser.get('https://www.facebook.com')

    accept_cookies(browser)

    browser.find_element(By.ID, 'email').send_keys(FB_USERNAME)
    browser.find_element(By.ID, 'pass').send_keys(FB_PASSWORD)
    browser.find_element(By.NAME, "login").click()

    time.sleep(2)


def facebook_goto_post(browser, target_post):
    browser.get(target_post)


def facebook_react(browser, reaction_label):
    # Wait for the button to be clickable (you can adjust the timeout as needed)
    like_button = WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Like']"))
    )

    # Hover on like button
    action_chains = ActionChains(browser)
    action_chains.move_to_element(like_button).perform()

    react_button = WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, f"[aria-label='{reaction_label}']"))
    )

    # click the target reaction button

    action_chains = ActionChains(browser)
    action_chains.move_to_element(react_button)
    action_chains.pause(1)
    action_chains.click(react_button)
    action_chains.perform()


def facebook_like(browser):
    # Wait for the button to be clickable (you can adjust the timeout as needed)
    like_button = WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Like']"))
    )

    # Hover on like button and click
    action_chains = ActionChains(browser)
    action_chains.move_to_element(like_button)
    action_chains.pause(2)
    action_chains.click(like_button)
    action_chains.perform()


def facebook_love(browser):
    facebook_react(browser, reaction_label="Love")


def facebook_care(browser):
    facebook_react(browser, reaction_label="Care")


def facebook_haha(browser):
    facebook_react(browser, reaction_label="Haha")


def workflow():
    # Define your workflow here!

    target_post = 'https://www.facebook.com/nixcraft/posts/pfbid02UL8ijMgqMgDJ6aqiu6bHEaFmaFG519Nf58oNXcUQrYvi84tgUb5idhQnTpEDeFAHl'
    browser = get_browser()
    facebook_login(browser)
    facebook_goto_post(browser=browser, target_post=target_post)
    facebook_haha(browser)


if __name__ == "__main__":
    # Opening env.json file
    file = open('env.json', )

    # returns JSON object as a dictionary
    env = json.load(file)

    # Closing file
    file.close()

    FB_USERNAME = env['username']
    FB_PASSWORD = env['password']
    PROXY_USERNAME = env['proxy_username']
    PROXY_PASSWORD = env['proxy_password']

    # Installing chromedriver
    ChromeDriverManager().install()

    workflow()

    time.sleep(100)
