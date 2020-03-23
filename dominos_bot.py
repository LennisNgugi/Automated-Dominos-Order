from selenium import webdriver
from time import sleep

from OrderInfo import postcode, fullname, contact, emailaddress, DriverInstructions

class Dominos():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def visit(self):
        self.driver.get('https://www.dominos.co.uk/')

        sleep(2)

         #1 person Pizza Deal is selected
        picksinglepersonpizza_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section[1]/a[1]/div/div[1]')
        picksinglepersonpizza_btn.click()
        print('Pizza Deal selected')

        #Postcode is pulled from OrderInfo.py file
        postcode_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/section/form/div/div/div/input')
        postcode_in.send_keys(postcode)

        print('PostCode')

        sleep(2)

         #Search give postcode
        SearchPostCode_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/section/form/button[1]')
        SearchPostCode_btn.click()
        print('Local Dominos Store is searched for using PostCode')

        sleep(5)

         #Pizza deal order - selected again lol
        pickdeal_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/section/div[2]/div/article[3]/footer/div[1]/a')
        pickdeal_btn.click()
        print('Deal is picked')

        #Medium pizza
        pizza1_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[1]/header/i[1]')
        pizza1_btn.click()
        print('Medium pizza picked')

        #Picked my favourite Pizza ;D
        pizzamedium_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[1]/section/section/section[1]/section/section/section[2]/section/article[6]/footer/div[2]/button')
        pizzamedium_btn.click()
        print('Pizza Type picked')

         #Picked Side order
        side_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[2]/header/i[1]')
        side_btn.click() 

        #Ordered side order
        pizzabreadside_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[2]/section/section/section[1]/section/section/section/section/article[2]/footer/div/button[1]')
        pizzabreadside_btn.click()
        print('Side Order - Pizza Bread')

         #Picked Drink that comes with order
        drink_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[3]/header/i[1]')
        drink_btn.click()

         #Confirmed drink
        pickingdrink_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[1]/section[3]/section/section/section[1]/section/section/section/section/article[4]/footer/div/button[1]')
        pickingdrink_btn.click()
        print('Drink Type')

         #confirmed checkouted again ;D
        checkout_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/div/section[2]/footer/button')
        checkout_btn.click()
        print('Deal check out')

        sleep(5)

        #redirected to basketdetails 
        self.driver.get('https://www.dominos.co.uk/basketdetails/show')

        #confirmed order for the third time, I mean Dominos loves confirming it's orders right. 
        thirdcheckout_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/article/div[6]/div[3]/button[2]')
        thirdcheckout_btn.click()
        print('Order Confirmed')

        #Entered Full name 
        fullname_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/div[2]/div[1]/input')
        fullname_in.send_keys(fullname)
        print('Full Name Entered')

        #Entered phone number 
        contact_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/div[2]/div[2]/input')
        contact_in.send_keys(contact)
        print('Contact Detail Entered')

         #Entered email address
        emailaddress_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/div[2]/div[3]/input')
        emailaddress_in.send_keys(emailaddress)
        print('Email Address Entered')

        #picked address from dropdown list
        PickAddress_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/div[2]/div[5]/select/option[3]')
        PickAddress_btn.click()
        print('Address Selected From Dropdown List')

        #Intruction given to driver
        driverinstruction_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/div[2]/div[7]/input[2]')
        driverinstruction_in.send_keys(DriverInstructions)
        print('Driving Instruction')

         #Payment Option
        cash_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/section/form/footer/div[2]/button[2]')
        cash_btn.click()
        print('Cash Option Selected')

        #Order Successful
        print('Successful order check your email for order number :D')


print('Dominos Pizza Script has started')

bot = Dominos()
bot.visit()
