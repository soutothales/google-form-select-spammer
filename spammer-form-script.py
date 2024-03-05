from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep
import random

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("service_log_path=NUL")
option.add_argument("--headless")  # faster, optional
option.add_argument("disable-gpu") # faster, optional
# option.add_argument("--proxy-server=23.227.39.1")
browser = webdriver.Chrome(options=option)

# Start time
start_time = time()

prefix_html = "/html/body/div/div[2]/form/div[2]/div/div[2]"
chosen_question_title = "<QUESTION_TITLE_WITHOUT_SPACE>" # Replace with the question you want to spam an specific answer
question_css_class = ".Qr7Oae" # Replace with the CSS Selector of your question items
iterations = 1 # Number of votes
delay = 2
chosen_option_index = 5 # Index of answer option you want to spam

for i in range(0, iterations):
    print("Start voting...")
    constant_url = "<FORM_URL>" # Your form URL
    browser.get(constant_url)
    sleep(delay)
    list_questions = browser.find_elements(By.CSS_SELECTOR, question_css_class)

    for cq in range(1, len(list_questions) + 1):
        print(cq)
        question_title = browser.find_element(By.XPATH, "{}/div[{}]/div/div/div[1]/div/div/span[1]".format(prefix_html, cq))
        print(question_title.text)
        if (question_title.text.replace(" ", "") == chosen_question_title):
            chosen_option = browser.find_element(By.XPATH, "{}/div[{}]/div/div/div[2]/div/div/span/div/div[{}]".format(prefix_html, cq, chosen_option_index))
            print(chosen_option.text)
            chosen_option.click()
        else:
            list_options = browser.find_elements(By.XPATH, "{}/div[{}]/div/div/div[2]/div/div/span/div/div".format(prefix_html, cq))
            random_option = random.randint(1, len(list_options))
            chosen_option = browser.find_element(By.XPATH, "{}/div[{}]/div/div/div[2]/div/div/span/div/div[{}]".format(prefix_html, cq, random_option))
            chosen_option.click()

    submit_button = browser.find_element(By.XPATH, "//*[text()='<SEND_BUTTON>']") # Replace with the submit text button
    submit_button.click()

print("Vote script executed in {} seconds".format(time() - start_time))