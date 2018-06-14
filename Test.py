from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime


class Test:

    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/Mariano/Downloads/chromedriver_win32posta/chromedriver.exe")

    def run(self):
        self.driver.set_script_timeout(5)
        try:
            self.driver.get("http://www.ambito.com/economia/")
        except TimeoutError:
            self.driver.execute_script("window.stop();")
        self.titles()

    def titles(self):
        titles_element = self.driver.find_elements_by_xpath("//article[contains(@class,'portada-article-titulo')]")
        href_list = [title.find_element_by_css_selector('a').get_attribute('href') for title in titles_element]
        for i in range(0, href_list.__len__() - 1):
            self.driver.set_script_timeout(5)
            try:
                self.driver.get(href_list[i])
                title = self.driver.find_element_by_xpath("//header[contains(@class,'titulo-noticia')]")
                title_text = title.text
                body = self.driver.find_element_by_xpath(
                    "//article[contains(@class,'container-fluid despliegue-noticia')]")
                body_text = body.text
            except TimeoutError:
                self.driver.execute_script("window.stop();")
            f = open(title.text + ".txt", "w")
            f.write("Title: " + title.text + '\n')
            f.write("Body" + '\n' + body.text)
            f.close()
            sleep(5)
        self.driver.close()


if __name__ == '__main__':
    test = Test()
    test.run()