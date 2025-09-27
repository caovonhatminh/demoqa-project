from playwright.sync_api import expect, Page
from playwright.sync_api import sync_playwright
import time

class FirstPage:
    def __init__(self, page:Page):
        self.page = page
        self.text_Practice_Form = page.locator('//h1[@class="text-center" and text()="Practice Form"]')
        self.FirstName = page.locator('//input[@id="firstName"]')
        self.LastName = page.locator('//input[@id="lastName"]')
        self.Email = page.locator('//input[@id="userEmail"]')
        self.Male_Gender = page.locator("//input[@value='Male']")
        self.Female_Gender = page.locator("//input[@value='Female']")
        self.Other_Gender = page.locator("//input[@value='Other']")
        self.Mobile = page.locator('//input[@id="userNumber"]')
        self.DateOfBirth = page.locator('//input[@id="dateOfBirthInput"]')
        self.table_DateOfBirth = page.locator('//div[@class="react-datepicker__month-container"]')
        self.MonthOfBirth = page.locator('//select[@class="react-datepicker__month-select"]')
        self.YearOfBirth = page.locator('//select[@class="react-datepicker__year-select"]')
        self.table_DateOfBirth = page.locator('//div[@class="react-datepicker__month"]')
        self.select_Day9 = page.locator("(//div[text()='9'])[1]")
        self.Sports_Hobby = page.locator('//input[@id="hobbies-checkbox-1"]')
        self.Reading_Hobby = page.locator('//input[@id="hobbies-checkbox-2"]')
        self.Music_Hobby = page.locator('//input[@id="hobbies-checkbox-3"]')
        self.btnUploadPicture = page.locator('//input[@id="uploadPicture"]')
        self.CurrentAddress = page.locator('//textarea[@id="currentAddress"]')
        self.State = page.locator("//div[text()='Select State']")
        self.City = page.locator("//div[text()='Select City']")
        self.btnSubmit = page.locator("//div[@class='text-right col-md-2 col-sm-12']//button[@id='submit']")
        self.Submit_Form_Display = page.locator('//div[@class="modal-content"]')

        self.screenshot = page.screenshot
        
    def verify_FirstPage_display(self):
        expect(self.text_Practice_Form).to_be_visible()
        self.screenshot(path="/data/verify_Practice_Form.png", full_page=False)
    def fill_text_FirstName(self, text):
        expect(self.FirstName).to_be_visible()
        self.FirstName.fill('Cao')
        time.sleep(5)
    def fill_text_LastName(self, text):
        expect(self.LastName).to_be_visible()
        self.LastName.fill('Minh')
        time.sleep(5)
    def fill_text_Email(self, text):
        expect(self.Email).to_be_visible()
        self.Email.fill('caovonhatminh09091999@gmail.com')
        time.sleep(5)
    def select_gender(self):
        self.Male_Gender.wait_for(state="visible", timeout=5000)        
        self.Female_Gender.wait_for(state="visible")
        self.Other_Gender.wait_for(state="visible")
        self.Male_Gender.click(force=True)
        assert self.Male_Gender.is_checked()
        time.sleep(5)
    def fill_text_Mobile(self, text):
        expect(self.Mobile).to_be_visible()
        self.Mobile.fill('0782519132')
        time.sleep(5)
    def Date_Of_Birth(self):
        expect(self.DateOfBirth).to_be_visible()
        self.DateOfBirth.click()
        time.sleep(2)
        expect(self.table_DateOfBirth).to_be_visible()
        expect(self.YearOfBirth).to_be_visible()
        expect(self.MonthOfBirth).to_be_visible()
        self.YearOfBirth.select_option('1999')
        time.sleep(2)
        self.MonthOfBirth.select_option('September')
        time.sleep(2)
        self.select_Day9.wait_for(state="visible", timeout=10000) 
        self.select_Day9.click(force=True)
        time.sleep(2)
    def select_Hobby(self):
        self.Sports_Hobby.wait_for(state="visible", timeout=5000)        
        self.Reading_Hobby.wait_for(state="visible")
        self.Music_Hobby.wait_for(state="visible")
        self.Sports_Hobby.click(force=True)
        assert self.Sports_Hobby.is_checked()
        time.sleep(5)
    def upload_Picture(self):
        expect(self.btnUploadPicture).to_be_visible()
        #self.btnUploadPicture.click()
        #file_path = Path("C:/Users/YourUsername/Downloads/CCCD_CaoVoNhatMinh.pdf")
        #self.page.set_input_files('input[type="file"]', file_path)
        time.sleep(5)
    def fill_text_CurrentAddress(self, text):
        expect(self.CurrentAddress).to_be_visible()
        self.CurrentAddress.fill('Nha Trang - Khanh Hoa')
        time.sleep(5)
    def select_State_and_City(self):
        expect(self.State).to_be_visible()
        self.State.click()
        time.sleep(2)
        self.page.locator("//div[text()='NCR']").click()
        time.sleep(2)
        expect(self.City).to_be_visible()
        self.City.click()
        time.sleep(2)
        self.page.locator("//div[text()='Delhi']").click()
        time.sleep(5)
    def verify_submit_form_display(self):
        self.btnSubmit.scroll_into_view_if_needed()
        self.btnSubmit.wait_for(state="visible", timeout=50000)
        self.btnSubmit.click()
        time.sleep(5)
        expect(self.Submit_Form_Display).to_be_visible()
        self.screenshot(path="submit_form_display.png", full_page=False)
        expect(self.page.locator("//tr[td[text()='Student Name'] and td[text()='Cao Minh']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='Student Email'] and td[text()='caovonhatminh09091999@gmail.com']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='Mobile'] and td[text()='0782519132']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='Date of Birth'] and td[text()='26 September,2025']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='Hobbies'] and td[text()='Sports']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='Address'] and td[text()='Nha Trang - Khanh Hoa']]")).to_be_visible
        expect(self.page.locator("//tr[td[text()='State and City'] and td[text()='NCR Delhi']]")).to_be_visible

        
