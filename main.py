from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 100
PROMISED_UP = 5
TWITTER_EMAIL = "Enter email here"
TWITTER_PASSWORD = "Enter password Here"
CHROME_DRIVER_PATH = "C:\python\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.google.com/search?q=speed+test&rlz=1C1GCEA_enUS1032US1032&oq=speed+test&aqs=chrome.0.69i59j0i131i433i512j0i433i512j0i131i433i512j0i10i131i433i512j0i131i433i512j0i512j69i60.1329j0j7&sourceid=chrome&ie=UTF-8")
        start_button = self.driver.find_element(By.XPATH, "//g-raised-button[contains(@id, 'knowledge-verticals-internetspeedtest__test_button')]")
        start_button.click()
        time.sleep(30)
        self.down = float(self.driver.find_element(By.ID, "knowledge-verticals-internetspeedtest__download").text.split("\n")[0])
        self.up = float(self.driver.find_element(By.ID, "knowledge-verticals-internetspeedtest__upload").text.split("\n")[0])

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()
        time.sleep(2)
        email_field = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_field.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()

        time.sleep(3)
        phone_field = self.driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')
        phone_field.send_keys("5038878052")
        phone_next = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
        phone_next.click()

        time.sleep(3)
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-18jsvk2.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input")
        password_field.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()

        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()

        time.sleep(2)
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        time.sleep(3)
        tweet_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up, when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(1)
        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        send_tweet.click()
        print("Tweet Sent.")
        time.sleep(3)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()
    print(f"Download Speed: {bot.down}")
    print(f"Upload Speed: {bot.up}")
else:
    print("Promised internet speeds achieved, no need to complain.")