from selenium import webdriver
from selenium.webdriver.common.by import By

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/adddressook")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("first")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("first_header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()

        def is_element_present(self, how, what):
            try: self.wd.find_element(by=how, value=what)
            except NoSuchElementException as e: return False
            return True

        def is_alert_present(self):
            try: self.wd.switch_to_alert()
            except NoSuchElementException as e: return False
            return True




        def tearDown(self):
            self.wd.quit()

if __name__ == "__main__":
    if __name__ == '__main__':
        unettest()








