import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestFrontEnd(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path = "polls/tests/chromedriver")

    def test_header_name(self):
        self.browser.get('http://127.0.0.1:8000/')
        page_heading = self.browser.find_element_by_tag_name("h1")
        self.assertEqual("Current Polls", page_heading.get_attribute('innerHTML'))
        self.browser.close()

    def test_poll_question(self):
        self.browser.get('http://127.0.0.1:8000/')
        poll = self.browser.find_elements_by_tag_name("li")
        for li in poll:
            question = li.text
        self.assertEqual("Which social media do usually use the most?", question)
        self.browser.close()

    def test_poll_click(self):
        self.browser.get('http://127.0.0.1:8000/')
        poll = self.browser.find_element_by_link_text("Which social media do usually use the most?")
        poll.click()
        selected = self.browser.find_element_by_name("choice").is_selected()
        self.assertFalse(selected)
        self.browser.close()
        
    def test_poll_choice_click(self):
        self.browser.get('http://127.0.0.1:8000/polls/4')
        poll = self.browser.find_element_by_link_text("Login")
        poll.click()
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        username.send_keys("Earnny")
        password.send_keys("earnearn")
        log_in = self.browser.find_element_by_id("login_btn")
        log_in.click()
        vote = self.browser.find_element_by_name("choice")
        vote.click()
        vote_btn = self.browser.find_element_by_id("vote_btn")
        vote_btn.click()
        check_in_result = self.browser.find_element_by_name("result_table")
        self.assertEqual("Choice", check_in_result.get_attribute('innerHTML'))
        self.browser.close()