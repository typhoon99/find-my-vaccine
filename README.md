# Find my Vaccine

**A selenium scrapper which checks cowin website every 5 seconds(can be customized on line 32 of alert.py). Please avoid scrapping less than 5-10 seconds, you may get 403 forbidden error.**

# Steps to run the script:

1. Clone this repo.
2. Check your Chrome version and download an appropriate webdriver from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). (I have included the webdriver for windows, ChromeDriver 90.0.4430.24.)
3. Copy the downloaded driver file to the code folder and replace the chromedriver.exe file.
4. [Optional] You can create a virtual evnironment for the project to install dependencies

- run `python -m venv mynenv` (myvenv can be replaced by any name of your choice)
- run `myvenv\Scripts\activate`
5. Install the required libraries. 
- run `pip install -r requirements.txt` 
6. Change your pincode on line 10 `search.send_keys('your_pincode')`
7. Run the alert.py script
- run `py alert.py`
