# # from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from django.test import TestCase
# # from django.test import LiveServerTestCase
# # from selenium.webdriver.common.by import By


# # class LoginTestCase(LiveServerTestCase):

# #     def setUp(self):
# #         self.driver = webdriver.Chrome()
# #         self.driver.implicitly_wait(10)
# #         self.live_server_url = 'http://127.0.0.1:8000/login'  # Set the live server URL here

# #     def tearDown(self):
# #         self.driver.quit()

# #     def test_login(self):
# #         self.driver.get(self.live_server_url)  # Use self.driver consistently

# #         # Interact with the login form
# #         username_input = self.driver.find_element(By.ID, 'username-input')
# #         password_input = self.driver.find_element(By.ID, 'password-input')
# #         login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')

# #         username_input.send_keys('ivan1@gmail.com')  # Replace with a valid username
# #         password_input.send_keys('12346')  # Replace with a valid password
# #         login_button.click()

# #         # Add assertions based on your expected behavior after login


# #         # Example: Check if a welcome message is present


# from selenium.webdriver.support import expected_conditions as EC
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from django.test import TestCase
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


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

#         username_input.send_keys('admin')  # Replace with a valid username
#         password_input.send_keys('admin')  # Replace with a valid password
#         login_button.click()

#         # Add assertions based on your expected behavior after login
#     # Wait for the 'generate_user' page to load
#         # WebDriverWait(self.driver, 10).until(
#         #     EC.presence_of_element_located((By.ID, 'generate_user-page-element'))
#         # )

#         # Add assertions based on your expected behavior after login
#         self.assertEqual(self.driver.current_url,  'http://127.0.0.1:8000/generate_user/')
#       # Click the "Add Subjects" link
#         add_students_link = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.NAME, 'add_student'))
#         )


#         # Now you can click the element
#         add_students_link.click()
#         # Add assertions based on your expected behavior after clicking the link
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/update-students/')
        
#         file_input = self.driver.find_element(By.NAME, 'excel_file')

#         # Set the file path for the input element
#         file_input.send_keys('E:/Project Daily Update/Backup Folders/New folder/New folder/New folder/30-11-23/22-11-2023/1.MiniProject/Book1.xlsx')  # Replace with the actual path to your file
#         # Locate and click the submit button
#         submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
#         submit_button.click()











# from selenium.webdriver.support import expected_conditions as EC
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from django.test import TestCase
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


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

#         username_input.send_keys('admin')  # Replace with a valid username
#         password_input.send_keys('admin')  # Replace with a valid password
#         login_button.click()

#         # Add assertions based on your expected behavior after login
#     # Wait for the 'generate_user' page to load
#         # WebDriverWait(self.driver, 10).until(
#         #     EC.presence_of_element_located((By.ID, 'generate_user-page-element'))
#         # )

#         # Add assertions based on your expected behavior after login
#         self.assertEqual(self.driver.current_url,  'http://127.0.0.1:8000/generate_user/')
#       # Click the "Add Subjects" link
#         add_students_link = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.NAME, 'add_subject'))
#         )


#         # Now you can click the element
#         add_students_link.click()
#         # Add assertions based on your expected behavior after clicking the link
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/add_subject/')
        
#         file_input = self.driver.find_element(By.NAME, 'excel_file')

#         # Set the file path for the input element
#         file_input.send_keys('E:/Project Daily Update/Backup Folders/New folder/New folder/New folder/30-11-23/22-11-2023/1.MiniProject/Book1.xlsx')  # Replace with the actual path to your file
#         # Locate and click the submit button
#         submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
#         submit_button.click()






#1




# from datetime import datetime
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/login'

#     def tearDown(self):
#         self.driver.quit()
        
#     def test_01_login_page(self):

#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)
#         username=driver.find_element(By.CSS_SELECTOR,"input#username-input[name='username']")
#         username.send_keys("admin")
#         password=driver.find_element(By.CSS_SELECTOR,"input[type='password']#password-input[name='password']")
#         password.send_keys("admin")
#         time.sleep(2)
#         submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         submit.click()
#         time.sleep(2)
        
        
        
        
        
        
        
        
 #2       
        
        
        
        
# from datetime import datetime
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/login'

#     def tearDown(self):
#         self.driver.quit()
        
#     def test_01_login_page(self):

#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)
#         username=driver.find_element(By.CSS_SELECTOR,"input#username-input[name='username']")
#         username.send_keys("admin")
#         password=driver.find_element(By.CSS_SELECTOR,"input[type='password']#password-input[name='password']")
#         password.send_keys("admin")
#         time.sleep(2)
#         submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         submit.click()
#         time.sleep(2)
#         redirect=driver.find_element(By.CSS_SELECTOR,"a.nav-link[name='add_student'][href='/update-students/']")
#         redirect.click()
#         time.sleep(2)
#         AddStudent=driver.find_element(By.CSS_SELECTOR,"a[href='/myhome']")
#         AddStudent.click()
#         time.sleep(2)
#         email=driver.find_element(By.CSS_SELECTOR,"input[type='email']#email[name='email'][required]")
#         email.send_keys("raju@gmail.com")
#         time.sleep(2)
#         fname=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='first_name'][required]")
#         fname.send_keys("Raju")
#         time.sleep(2)
#         lname=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='last_name'][required]")
#         lname.send_keys("joseph")
#         time.sleep(2)
#         address=driver.find_element(By.CSS_SELECTOR,"textarea[name='address'][rows='4'][required]")
#         address.send_keys("Kurishmootil(H), Pala")
#         time.sleep(2)
#         pno=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='phone_no'][required]")
#         pno.send_keys("9876543210")
#         time.sleep(2)
#         course=driver.find_element(By.CSS_SELECTOR,"select[name='course'][required]")
#         course.click()
#         course1=driver.find_element(By.CSS_SELECTOR,"option[value='3']")
#         course1.click()
#         time.sleep(2)
#         gender=driver.find_element(By.CSS_SELECTOR,"select[name='gender'][required]")
#         gender.click()
#         gender1=driver.find_element(By.CSS_SELECTOR,"select[name='gender'] option[value='male']")
#         gender1.click()
#         time.sleep(2)
        
        
        
 #3       
        
        
        
# from datetime import datetime
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/login'

#     def tearDown(self):
#         self.driver.quit()
        
#     def test_01_login_page(self):

#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)
#         username=driver.find_element(By.CSS_SELECTOR,"input#username-input[name='username']")
#         username.send_keys("admin")
#         password=driver.find_element(By.CSS_SELECTOR,"input[type='password']#password-input[name='password']")
#         password.send_keys("admin")
#         time.sleep(2)
#         submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         submit.click()
#         time.sleep(2)
#         redirect=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/add_subject/']")
#         redirect.click()
#         time.sleep(2)
#         sname=driver.find_element(By.CSS_SELECTOR,"input[type='text']#subject-name[name='subject_name'][required]")
#         sname.send_keys("Hindi2")
#         
        
          









#4



# from datetime import datetime
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/login'

#     def tearDown(self):
#         self.driver.quit()
        
#     def test_01_login_page(self):

#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)
#         username=driver.find_element(By.CSS_SELECTOR,"input#username-input[name='username']")
#         username.send_keys("admin")
#         password=driver.find_element(By.CSS_SELECTOR,"input[type='password']#password-input[name='password']")
#         password.send_keys("admin")
#         time.sleep(2)
#         submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         submit.click()
#         time.sleep(2)
#         redirect=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/add_class/']")
#         redirect.click()
#         time.sleep(2)
#         Addclass=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='class_name'][required]")
#         Addclass.send_keys("8")
#         time.sleep(2) 
#         submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         submit.click()
#         time.sleep(2)
        
        
        
        
        
#5



from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/login'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):

        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        username=driver.find_element(By.CSS_SELECTOR,"input#username-input[name='username']")
        username.send_keys("admin")
        password=driver.find_element(By.CSS_SELECTOR,"input[type='password']#password-input[name='password']")
        password.send_keys("admin")
        time.sleep(2)
        submit=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        submit.click()
        time.sleep(2)
        redirect=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/manage_feedback_questions/']")
        redirect.click()
        time.sleep(2)
        Addclass=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='question_text'][required]")
        Addclass.send_keys("Is it available all facilities ?")        
        
        
        
        
        
        
        
        
        
        
    