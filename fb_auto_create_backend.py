from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

def create_facebook_account(email, password, firstname, lastname, dob):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for Render
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:
        # Open Facebook Signup Page
        driver.get("https://www.facebook.com/r.php")
        time.sleep(3)

        # Fill in the signup form
        driver.find_element(By.NAME, "firstname").send_keys(firstname)
        driver.find_element(By.NAME, "lastname").send_keys(lastname)
        driver.find_element(By.NAME, "reg_email__").send_keys(email)
        driver.find_element(By.NAME, "reg_passwd__").send_keys(password)

        # Split DOB (YYYY-MM-DD) into day, month, year
        year, month, day = dob.split("-")
        driver.find_element(By.ID, "year").send_keys(year)
        driver.find_element(By.ID, "month").send_keys(month)
        driver.find_element(By.ID, "day").send_keys(day)

        # Select Gender (Assume Male)
        driver.find_element(By.XPATH, "//input[@value='2']").click()

        # Submit the form
        driver.find_element(By.NAME, "websubmit").click()
        time.sleep(5)

        # Check for any errors
        if "confirmemail" in driver.page_source:
            return {"status": "success", "message": "Account created! Check email for confirmation."}
        else:
            return {"status": "failed", "message": "Account creation failed."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        driver.quit()


@app.route("/create_fb_account", methods=["POST"])
def create_fb_account():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    dob = data.get("dob")

    if not all([email, password, firstname, lastname, dob]):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    result = create_facebook_account(email, password, firstname, lastname, dob)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
