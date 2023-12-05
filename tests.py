# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from django.test import TestCase
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.by import By


# class LoginTestCase(LiveServerTestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/login'  # Set the live server URL here

#     def tearDown(self):
#         self.driver.quit()

#     def test_login(self):
#         self.driver.get(self.live_server_url)  # Use self.driver consistently

#         # Interact with the login form
#         username_input = self.driver.find_element(By.ID, 'username-input')
#         password_input = self.driver.find_element(By.ID, 'password-input')
#         login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

#         username_input.send_keys('ivan1@gmail.com')  # Replace with a valid username
#         password_input.send_keys('12346')  # Replace with a valid password
#         login_button.click()

#         # Add assertions based on your expected behavior after login


#         # Example: Check if a welcome message is present


from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/login'  # Set the live server URL here

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get(self.live_server_url)  # Use self.driver consistently

        # Interact with the login form
        username_input = self.driver.find_element(By.ID, 'username-input')
        password_input = self.driver.find_element(By.ID, 'password-input')
        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

        username_input.send_keys('admin')  # Replace with a valid username
        password_input.send_keys('admin')  # Replace with a valid password
        login_button.click()

        # Add assertions based on your expected behavior after login
    # Wait for the 'generate_user' page to load
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'generate_user-page-element'))
        # )

        # Add assertions based on your expected behavior after login
        self.assertEqual(self.driver.current_url,  'http://127.0.0.1:8000/generate_user/')
      # Click the "Add Subjects" link
        add_students_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'add_student'))
        )


        # Now you can click the element
        add_students_link.click()
        # Add assertions based on your expected behavior after clicking the link
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/update-students/')
        
        file_input = self.driver.find_element(By.NAME, 'excel_file')

        # Set the file path for the input element
        file_input.send_keys('E:/Project Daily Update/Backup Folders/New folder/New folder/New folder/30-11-23/22-11-2023/1.MiniProject/Book1.xlsx')  # Replace with the actual path to your file
        # Locate and click the submit button
        submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()
