import unittest

from selenium import webdriver

from Answers.Module1.lesson6_step10 import insert_required_data


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_insert_required1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result = insert_required_data(self.browser, link)
        self.assertEqual(None, result, "Something got wrong with first link")

    def test_insert_required2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = insert_required_data(self.browser, link)
        self.assertEqual(None, result, "Something got wrong with second link")


if __name__ == "__main__":
    unittest.main()
