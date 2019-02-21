#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time

options = Options()
options.headless = True

drv = webdriver.Chrome(
    options=options
)
drv.get('https://discordapp.com/jobs?team=engineering')

time.sleep(20)

# get an HTML representation of the entire DOM
# after the JS has run
everything = drv.execute_script("return document.documentElement.outerHTML")

if "FRONT" in everything.upper():
    print("IT WORKED")
else:
    print("IT FAILED")

# quit the browser after our request
drv.quit()

