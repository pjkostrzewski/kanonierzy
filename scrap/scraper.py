from selenium import webdriver
from scrap.config import chromedriver_path
from time import sleep


class Scraper:
    url = "https://www.kanonierzy.com/"

    def __init__(self):
        self.options = self.get_options()
        self.browser = webdriver.Chrome(chromedriver_path, options=self.options)
        self.browser.get(self.url)
        # self.browser.find_elements_by_xpath('//*[@id="oa-360-1604156168102_cdqdj3exp"]/div/div/div/div/div[3]/div[2]/button').click()

    @staticmethod
    def get_options():
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        return options

    def all_news(self):
        return self.browser.find_elements_by_class_name("singlenews")

    def scroll_down_page(self, speed=8):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.browser.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            
            
scraper = Scraper()
# scraper.scroll_down_page()
all_news = scraper.all_news()
for x in all_news:
    # print(x.find_element_by_class_name("newscont").find_element_by_class_name("title").find_element_by_css_selector('a').get_attribute('href'))
    # print(x.find_element_by_class_name("newscont").find_element_by_class_name("title").find_element_by_css_selector('a').get_attribute('text'))
    print(x.find_element_by_class_name("newsimg").get_attribute("src"))
    print(x.find_element_by_class_name("newsimg").get_attribute("alt"))
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_css_selector('a').get_attribute('href'))
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("text").text)
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("details").find_element_by_class_name("date").text)
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("details").find_element_by_class_name("comments").text)
    print()
sleep(30)