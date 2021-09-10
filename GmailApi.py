from UserAgent import random_useragent
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import os
import zipfile
import time
import requests
import json
import random
from faker import Faker
from discord_webhook import DiscordWebhook, DiscordEmbed, webhook


def gmailapi(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, recovery_email,country_code, sms_active, webhook_url, webhook_username):
    try:
        useragent = random_useragent()
        a=random.uniform(0.1,0.6)
        def send_delayed_keys(element, text, delay=a):
            for c in text:
                endtime = time.time() + delay
                element.send_keys(c)
                time.sleep(abs(endtime - time.time()))
        
        print('Start\n')
        fake = Faker()
        fake_recoveryemail = recovery_email
        fake_firstname = str(fake.first_name())
        fake_lastname = str(fake.last_name())
        fake_username = str(fake_firstname+fake_lastname+str(random.randint(1000000,9999999))).lower()
        mail_provider = random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"])
        fake_email = fake_username+mail_provider
        alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]<>,.')
        fake_password = ''
        for i in range(random.randint(15,20)):
            fake_password += random.choice(alph)
        months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        # months_list = ["01","02","03","04","05","06","07","08","09","10","11","12"]
        fake_month = random.choice(months_list)
        day_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
        fake_day = random.choice(day_list)
        fake_year = str(random.randint(1930, 2010))
        fake_dob = fake_month+"-"+fake_day+"-"+fake_year
        gender_list = ["Male", "Female"]
        fake_gender = random.choice(gender_list)
        # proxy = "190.112.193.59:1212"
        locations_list = ["Egypt", "Morocco","South Africa", "Canada", "United States","Australia","Hong Kong","India","Indonesia","Japan",
                        "Malaysia","New Zealand","Philippines","Singapore","Vietnam","Austria","Belgium","Bulgaria","Croatia","Czech Republic","Denmark",
                        "Finland","Hungary","Ireland","Israel","Luxembourg","Netherlands","Norway","Portugal","Romania","Slovakia","Slovenia","Sweden","Switzerland","United Kingdom","Saudi Arabia",
                        "United Arab Emirates"]
        fake_location = random.choice(locations_list)
        url = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&dsh=S185420504%3A1582184558776735&gmb=exp&biz=true&flowName=GlifWebSignIn&flowEntry=SignUp&hl=en-GB"
        symbol = "+"

        print("Username: ", fake_username)
        print("Password:", fake_password + '\n')
        print("proxy: ", PROXY_HOST)


        # ###############USING CHROME DRIVER WITH PROXY####################################
        # manifest_json = """
        # {
        #     "version": "1.0.0",
        #     "manifest_version": 2,
        #     "name": "Chrome Proxy",
        #     "permissions": [
        #         "proxy",
        #         "tabs",
        #         "unlimitedStorage",
        #         "storage",
        #         "<all_urls>",
        #         "webRequest",
        #         "webRequestBlocking"
        #     ],
        #     "background": {
        #         "scripts": ["background.js"]
        #     },
        #     "minimum_chrome_version":"22.0.0"
        # }
        # """

        # background_js = """
        # var config = {
        #         mode: "fixed_servers",
        #         rules: {
        #         singleProxy: {
        #             scheme: "http",
        #             host: "%s",
        #             port: parseInt(%s)
        #         },
        #         bypassList: ["localhost"]
        #         }
        #     };

        # chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        # function callbackFn(details) {
        #     return {
        #         authCredentials: {
        #             username: "%s",
        #             password: "%s"
        #         }
        #     };
        # }

        # chrome.webRequest.onAuthRequired.addListener(
        #             callbackFn,
        #             {urls: ["<all_urls>"]},
        #             ['blocking']
        # );
        # """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

        # def get_chromedriver(use_proxy=False, user_agent=None):
        #     path = os.path.dirname(os.path.abspath(__file__))
        #     chrome_options = webdriver.ChromeOptions()
        #     pluginfile = 'proxy_auth_plugin.zip'

        #     with zipfile.ZipFile(pluginfile, 'w') as zp:
        #         zp.writestr("manifest.json", manifest_json)
        #         zp.writestr("background.js", background_js)
        #     chrome_options.add_extension(pluginfile)
        #     chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        #     chrome_options.add_argument("window-size=1280,800")
        #     chrome_options.add_argument(f"user-agent={user_agent}")
        #     print(f"The user-agent used is {useragent}")
        #     driver = webdriver.Chrome("./chromedriver",
        #         chrome_options=chrome_options)
        #     return driver
        

        # driver = get_chromedriver(use_proxy=True, user_agent=useragent)
        # print("DRIVER LOADED SUCCESSFUL")

        # #Remove navigator.webdriver Flag using JavaScript
        # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # ####################################################################################


        
        ###############USING CHROME DRIVER WITHOUT PROXY####################################
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("window-size=1280,800")
        chrome_options.add_argument(f"user-agent={useragent}")
        driver = webdriver.Chrome("./chromedriver", options=chrome_options)
        ####################################################################################


        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(url)

        #keep refreshing the page till the page loads
        refresh_time = 0
        while refresh_time <1:
            try:
                driver.find_element(By.ID, "accountDetailsNext")
                break
            except:
                driver.refresh()
        print("Page load successful")

        time.sleep(2)

        print("Inputing user details on the registration page")

        firstName = driver.find_element_by_id('firstName')
        send_delayed_keys(firstName, fake_firstname)

        lastName = driver.find_element_by_id('lastName')
        send_delayed_keys(lastName, fake_lastname)

        username = driver.find_element_by_id('username')
        send_delayed_keys(username, fake_username)

        time.sleep(1)
        Passwd = driver.find_element_by_name('Passwd')
        send_delayed_keys(Passwd, fake_password)

        time.sleep(1)
        ConfirmPasswd = driver.find_element_by_name('ConfirmPasswd')
        send_delayed_keys(ConfirmPasswd, fake_password)

        time.sleep(1)
        driver.find_element(By.ID, "accountDetailsNext").click()

        ########################################################### API #########################
        print("Verify Your Phone number!!")
        time.sleep(1)

        api_key = sms_active

        country = country_code
        operator = 'any'
        service = 'go'
        ref = '613879'
        forward = '0'

        status_ready = '1'
        status_complete = '6'
        status_ban = '8'

        ######## Change of activation status

        access_ready = 'ACCESS_READY'  # number readiness confirmed
        access_ready_get = 'ACCESS_RETRY_GET'  # waiting for a new sms
        access_activation = 'ACCESS_ACTIVATION'  # service successfully activated
        access_cancel = 'ACCESS_CANCEL'  # activation canceled

        ######## Get activation status:

        status_wait = 'STATUS_WAIT_CODE'  # waiting for sms
        status_wait_retry = "STATUS_WAIT_RETRY"  # waiting for code clarification
        status_wait_resend = 'STATUS_WAIT_RESEND'  # waiting for re-sending SMS *
        status_cancel = 'STATUS_CANCEL'  # activation canceled
        status_ok = "STATUS_OK"  # code received

        # POSSIBLE MISTAKES: (ERROR)
        error_sql = 'ERROR_SQL'  # SQL-server error
        no_activation = 'NO_ACTIVATION'  # activation id does not exist
        bad_service = 'BAD_SERVICE'  # incorrect service name
        bad_status = 'BAD_STATUS'  # incorrect status
        bad_key = 'BAD_KEY'  # Invalid API key
        bad_action = 'BAD_ACTION'  # incorrect action

        #the number of times to wait for sms
        # stop_number = 0

        # Balance
        balance = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=getBalance')
        info = balance.text
        b1, b2 = info.split(":")
        print("Balance: ", b2)

        # number of available phones
        find_numbers = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=getNumbersStatus&country=' + country + '&operator=' + operator)
        num_numbers = json.loads(find_numbers.text)

        a = num_numbers['go_0']
        if a == '0':
            print('sorry no number available')
            driver.quit()
            sys.exit()
        else:
            print('Available phone numbers: ', a)

            # Order Number
            order_number = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=getNumber&service=' + service + '&forward=' + forward + '&operator=' + operator + '&ref=' + ref + '&country=' + country)
            print('buy TEXT: ', order_number.text)
            info = order_number.text
            a, id, phone_number = info.split(":")
            print('Id: ', id)
            print('Phone Number: ', phone_number)

            time.sleep(5)
            phonenumber = driver.find_element_by_id('phoneNumberId')
            send_delayed_keys(phonenumber, symbol + phone_number)
            time.sleep(1)
            # driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
            driver.find_element(By.XPATH, "//*[text()='Next']").click()

            # Activation status
            time.sleep(5)
            ch_activation_status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=setStatus&status=' + status_ready + '&id=' + id + '&forward=' + forward)
            if ch_activation_status.text in access_ready:
                print("number readiness confirmed\n")

                # SMS status
                time.sleep(3)
                get_sms = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=getStatus&id=' + id)
                code = get_sms.text
                

                wait_time = 180
                while status_wait in code or status_ok in code or status_cancel in code or status_wait_resend in code or status_wait_retry in code:
                    if code in status_wait:
                        if wait_time > 0:
                            tic = time.perf_counter()
                            print("wait sometime for SMS")
                            time.sleep(20)
                            get_sms = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=getStatus&id=' + id)
                            code = get_sms.text
                            toc = time.perf_counter()
                            tictoc = toc-tic
                            wait_time = wait_time-tictoc
                            print(f"Wait_time is {round(wait_time)} seconds.")
                        else:
                            print("sorry this number has some issues")
                            driver.quit()
                            sys.exit()
                        
                    elif status_ok in code:
                        tex, m_code = code.split(':')
                        print("Your SMS code: ", m_code)
                        time.sleep(2)
                        codenumber = driver.find_element_by_id('code')
                        send_delayed_keys(codenumber, m_code)
                        time.sleep(2)
                        # driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
                        driver.find_element(By.XPATH, "//*[text()='Verify']").click()
                        # complete_status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key='+api_key+'&action=setStatus&status='+status_complete+'&id='+id+'&forward='+forward)
                        # print("PVA complete")
                        break
                    else:
                        ch_activation_status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=setStatus&status=' + status_ban + '&id=' + id + '&forward=' + forward)
                        print("Cancel the activation")
                        print("sorry this number has some issues")
                        driver.quit()
                        sys.exit()

            else:
                ch_activation_status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key=' + api_key + '&action=setStatus&status=' + status_ban + '&id=' + id + '&forward=' + forward)
                print("Cancel the activation")
                print("sorry this number has some issues")
                driver.quit()
                sys.exit()

        time.sleep(3)
        phone_url = "https://accounts.google.com/signup/v2/webgradsidvphone"
        veryfi_url = "https://accounts.google.com/signup/v2/webgradsidvverify"
        main_url = "https://accounts.google.com/signup/v2/webpersonaldetails"
        a = driver.current_url
        while veryfi_url in a or phone_url in a or main_url in a:
            if main_url in a:
                break
            else:
                time.sleep(2)
                print("This is not correct page\nplz wait some time")
                a = driver.current_url

        print("Inputing recovery email, age and gender")

        driver.find_element_by_id('phoneNumberId').clear()

        time.sleep(1)
        RecoveryEmail = driver.find_element_by_name('recoveryEmail')
        send_delayed_keys(RecoveryEmail, fake_recoveryemail)

        time.sleep(1)
        driver.find_element_by_xpath('//*[@aria-label="Day"]').send_keys(int(fake_day))

        time.sleep(1)
        element = driver.find_element_by_id('month')
        drp = Select(element)
        drp.select_by_visible_text(fake_month)

        time.sleep(1)
        driver.find_element_by_xpath('//*[@aria-label="Year"]').send_keys(int(fake_year))

        time.sleep(1)
        element = driver.find_element_by_id('gender')
        drp = Select(element)
        drp.select_by_visible_text(fake_gender)

        time.sleep(1)
        # driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
        driver.find_element(By.XPATH, "//*[text()='Next']").click()
        try:
            time.sleep(5)
            driver.find_element(By.XPATH, "//*[text()='Skip']").click()
        except:
            pass
        try:
            time.sleep(5)
            driver.find_element(By.XPATH, "//*[text()='Next']").click()
        except:
            pass

        time.sleep(5)
        current_Url = driver.current_url
        du_Url = 'https://accounts.google.com/signup/v2/webtermsofservice'
        if du_Url in current_Url:
            # time.sleep(2)
            #driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            #time.sleep(2)
            #driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            #time.sleep(2)
            #driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            #time.sleep(10)

            # driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
            # driver.find_element(By.XPATH, "//*[text()='I agree']").click()
            driver.find_element(By.XPATH, "//*[text()='I agree']").click()

            time.sleep(10)
            cur_url = driver.current_url
            fail_url = 'https://accounts.google.com/'
            if fail_url in cur_url:
                print("This account take some time")
                print("Plz Cut this browser yourself\n")
                time.sleep(3)

            else:
                pass
        else:
            # time.sleep(2)
            # driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@class="Ce1Y1c"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@class="RveJvd snByac"]').click()

            time.sleep(10)
            cur_url = driver.current_url
            fail_url = 'https://accounts.google.com/'
            if fail_url in cur_url:
                print("This account take some time")
                print("Plz Cut this browser yourself")
                time.sleep(3)

            else:
                time.sleep(3)
                pass
        complete = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key='+api_key+'&action=setStatus&status='+ status_complete +'&id='+id+'&forward='+forward)
        print("Now, this account is completed.\n")
        time.sleep(2)
        driver.quit()
        print("Sending the details to the discord server")
        discord_content = f"GMAIL ACCOUNT {fake_username}@gmail.com:{fake_password}"
        webhook = DiscordWebhook(url=webhook_url, username=webhook_username, content=discord_content)
        embed = DiscordEmbed(title="**GMAIL ACCOUNT GENERATOR**", color = 242424)
        embed.set_author(name="Bot")
        webhook.add_embed(embed)
        response = webhook.execute()
        return fake_username, fake_password


    #IF THE ABOVE CODE DOES NOT RUN, THEN THE PROXY ADDRESS PROVIDED BY THE USER IS NOT VALID
    except:
        return "INVALID PROXY"