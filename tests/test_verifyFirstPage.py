from playwright.sync_api import sync_playwright
import pytest, time, sys, os
from models.FirstPage import FirstPage

URL_web = "https://demoqa.com/automation-practice-form"
def test_gotowebsite():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL_web, wait_until="domcontentloaded", timeout=90_000)
        first_page = FirstPage(page)
        first_page.verify_FirstPage_display()
        first_page.fill_text_FirstName('Cao')
        first_page.fill_text_LastName('Minh')
        first_page.fill_text_Email('caovonhatminh09091999@gmail.com')
        first_page.select_gender()
        first_page.fill_text_Mobile('0782519132')
        first_page.Date_Of_Birth()
        first_page.select_Hobby()
        first_page.upload_Picture()
        first_page.fill_text_CurrentAddress('Nha Trang - Khanh Hoa')
        first_page.select_State_and_City()
        first_page.verify_submit_form_display()



