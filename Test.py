from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime


class Test:

    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/Mariano/Downloads/chromedriver_win32posta/chromedriver.exe")

    def run(self):
        self.driver.set_script_timeout(1)
        try:
            self.driver.get("http://www.ambito.com/economia/")
        except TimeoutError:
            self.driver.execute_script("window.stop();")
        self.titles()
        self.merval_header()

    def titles(self):
        titles_element = self.driver.find_elements_by_xpath("//article[contains(@class,'portada-article-titulo')]")
        titles = [title.text for title in titles_element]
        for title in zip(titles):
            print(title, '\n')
        # for title in titles_element:
        #     title.find_element_by_xpath("//*[@id=\"portada\"]/section/div[1]/div[1]/section/article/h4/a").click()

    def merval_header(self):
        header_element = self.driver.find_element_by_xpath("//*[@id=\"portada\"]/header/div/div/div/header/div"
                                                           "/section/div[1]/div/nav/ul/li[2]/div/div[3]/div["
                                                           "2]/div/h6/span")
        header_merval = header_element.text
        f = open("index", "a")
        f.write(datetime.datetime.now().__str__() + " " + header_merval + '\n')

        print("Merval: ", header_merval)


if __name__ == '__main__':
    test = Test()
    test.run()