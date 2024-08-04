from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import logging

months = ["August", "September", "October", "November", "December", "January", "February", "March", "April", "May",
          "June", "July"]
IM_HOME = True


def now_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    return formatted_time


def check(month, date):
    if month == "May":
        return month + " " + date
    elif month == "June":
        if 11 <= date <= 24:
            return False
        else:
            return month + " " + date
    elif month == "July":
        return month + " " + date
    else:
        return False


def month_maker(month):
    for i in range(len(months)):
        if months[i] == month:
            month = months[i + 1]
            return month


found = False
e = 1
s = 1
start_time = datetime.now()
end_time = datetime.now()
iteration = 1
logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    filename=f"LOG/4_4_Iteration.txt",
                    filemode='a')

# Define a handler to output logs to console as well
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

while not found:
    # Set up the WebDriver (assuming you're using Chrome, but you can use other browsers too)
    driver = webdriver.Chrome()
    # Open the website
    driver.get("https://ais.usvisa-info.com/en-am/niv/users/sign_in")  # Replace with the actual website URL
    time.sleep(5)

    # Armania = "https://ais.usvisa-info.com/en-am/niv/users/sign_in"

    # Perform login (assuming there's a login form)
    username = driver.find_element(By.ID, "user_email")
    password = driver.find_element(By.ID, "user_password")

    # Enter your login credentials
    # if s % 2 == 0:
    #     username.send_keys("nassrinsharifi02@gmail.com")
    # password.send_keys("nsrn1381")
    # else:
    username.send_keys("keivanjamali01@gmail.com")
    password.send_keys("Po77#kpsmebestand")

    policy_checkbox = driver.find_element(By.ID, "policy_confirmed")

    # Scroll to the checkbox
    driver.execute_script("arguments[0].scrollIntoView();", policy_checkbox)

    # Click the checkbox using JavaScript
    driver.execute_script("arguments[0].click();", policy_checkbox)

    # Submit the form
    password.send_keys(Keys.RETURN)

    # https://ais.usvisa-info.com/en-am/niv/schedule/52698354/continue_actions
    # https://ais.usvisa-info.com/en-am/niv/schedule/52698354/appointment

    time.sleep(5)

    # Locate the "Continue" button
    continue_button = driver.find_element(By.XPATH, "//a[@class='button primary small']")

    # Extract the URL of the "Continue" button
    button_url = continue_button.get_attribute("href")
    # print("Button URL for continue:", button_url)
    # print("Button URL for appointments:", button_url[:-16] + "appointment")

    # Navigate to the extracted URL
    driver.get(button_url)
    driver.get(button_url[:-16] + "appointment")
    while (end_time - start_time).seconds < 30 * 60:
        time.sleep(600)
        driver.refresh()
        logging.info(f"[Iter {iteration}] (time : {now_time()}) | Refreshing...")
        iteration += 1
        end_time = datetime.now()

    start_time = datetime.now()
    end_time = datetime.now()
    iteration = 1
    s += 1
    logging.info(f"[Success {s}] Found an available date.")
    time.sleep(5 * 60)

    # except:
    #     logging.info(f"[ERROR {e}] There is an error.(time : {now_time()})")
    #     e += 1
    #     time.sleep(1 * 60)
    #     end_time = datetime.now()
