import logging
import os
from subprocess import check_output
import random
import string
import time
from difflib import SequenceMatcher
from pynput.keyboard import Key, Controller

import platform


from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException, NoSuchElementException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# support.common.keys import Keys

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)
keyboard = Controller()
name=open('FLname.txt','r')
listname=name.readlines()
listnamelen=len(listname)
amnFlist=random.randint(1,listnamelen)
amnLlist = random.randint(1,listnamelen) != amnFlist
firstNam = listname[amnFlist]
lastNam = listname[amnLlist]
def url_parse(url):
    if url is None or url == '' or url.count('.') == 0 or 'facebook.com' not in url:
        return None
    if url.count('/') == 0:
        return 'https://www.facebook.com/'
    return 'https://www.facebook.com/' + url[url.find('.com/') + len('.com/')::]


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


class Bot:
    """continfa = False
    countryCode = ["US", "JP", "NL"]
    counCode="""
    def __init__(self, headless=False):
        """os.system("protonvpn-cli d")
        os.system("protonvpn-cli c -f -p tcp")
        time.sleep(6)
        #os.system("protonvpn-cli s")
        statusVpn=check_output("protonvpn-cli s | grep -n 'Country:'",shell=True)
        print(statusVpn.decode())
        strstatus=statusVpn.decode()
        print(strstatus.split(':')[2].split(' ')[2])
        print(type(strstatus))
        print(type(statusVpn))
        print(strstatus.split(':')[2].split(' ')[2].find('Netherlands'))
        if strstatus.split(':')[2].split(' ')[2].find('Netherlands') > -1:
            self.counCode="NL"
        elif strstatus.split(':')[2].split(' ')[2].find('Japan')>-1:
            self.counCode="JP"
        else:
            self.counCode="US"

        print(self.counCode)
        #print(len(splVpn))
        #print(splVpn)"""
        self.options = webdriver.ChromeOptions()

        self.options.add_argument('disable-infobars')
        self.options.add_argument('disable-notifications')

        self.driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser",
                                       options=self.options)

        self.driver.implicitly_wait('5')
        self.driver.delete_all_cookies()

        self.logged_in = False

    def __del__(self):
        if self.driver.service.process is not None:
            self.driver.quit()

    def check_browser_state(self):
        try:
            x = self.driver.current_url
        except InvalidSessionIdException and WebDriverException:
            self.driver.quit()
            self.__init__(self.options.headless)
            print('Restarting browser..')

    def doLogin(self, username, password,country):
       if not self.logged_in:
            bol=False
            try:
                time.sleep(3)
                self.driver.get('https://www.facebook.com/')
                time.sleep(2)
            except WebDriverException as e:
                logging.error(e)
                self.doLogin(username, password,country)
            try:
                bol = self.driver.find_element('xpath', '//*[@title="Decline optional cookies"]').is_displayed()
                print(bol)

            except:
                print(bol)
            if bol == True:
                allowbtn = self.driver.find_element('xpath', '//*[@title="Decline optional cookies"]')
                allowbtn.click()
                time.sleep(5)
            print(self.counCode+" "+country)

            print(self.counCode == str(country))
            if self.counCode == country:
                print("same country")
                try:
                    user_box = self.driver.find_element('xpath', '//input[@name="email"]')
                    user_box.send_keys(username)
                    time.sleep(2)
                    password_box = self.driver.find_element('xpath', '//input[@name="pass"]')
                    password_box.send_keys(password)
                    time.sleep(5)
                    login_btn = self.driver.find_element('xpath', '//button[@name="login"]')
                    login_btn.click()
                    time.sleep(2)
                    print(self.driver.title)
                    login=False

                    try:
                        disagreebtn=self.driver.find_element('xpath','/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div')
                        login=disagreebtn.is_displayed()
                    except:
                        self.logout()
                    if self.driver.title == "Facebook":
                        self.logged_in = True
                        time.sleep(20)
                        x=self.search()
                        time.sleep(5)
                        #self.reportPostUrl("https://www.facebook.com/fdremoe")
                        y=self.reportPostUrl("https://www.facebook.com/PMAbiyAhmedAli")
                        time.sleep(5)
                        self.commentPostUrl("https://www.facebook.com/PMAbiyAhmedAli")
                        time.sleep(5)
                        self.resharePostUrl("https://www.facebook.com/fdremoe")
                        time.sleep(4)
                        self.logout()
                        return 'Successful'
                    else:
                        return 'Failed to login'
                except NoSuchElementException as e:
                    self.logout()
                    logging.error(e)
                return 'Already logged in'
    def typeString(self,string):
        for char in string:
            keyboard.type(char)
            delay = random.uniform(1,3)
            time.sleep(delay)
        return ''
    def gurellaEmail(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get("https://www.guerrillamail.com/inbox")
        time.sleep(9)

        # if self.driver.find_element('xpath','/html/body/center[1]').is_displayed():
        #   self.driver.get("https://getnada.com/")
        #  emaGu = self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/p/span[1]/a/button').text
        # copybtn = self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/p/span[2]')
        # copybtn.click()

        userBtn = self.driver.find_element('xpath', '//*[@id="inbox-id"]')
        userBtn.click()
        time.sleep(3)
        username = ''.join(random.sample(string.ascii_letters, 9))

        self.typeString(username)

        dayse = Select(self.driver.find_element('xpath', '//*[@id="gm-host-select"]'))
        dayse.select_by_value("guerrillamail.com")

        setbtn = self.driver.find_element('xpath',
                                          '/html/body/div[4]/div/div[2]/div/span[1]/span/button[1][@class="save button small"]')
        setbtn.click()
        time.sleep(7)
        checkBtn = self.driver.find_element('xpath', '/html/body/div[4]/div/div[2]/div/span[4]/input[@id="use-alias"]')
        checkBtn.click()
        time.sleep(5)
        emaGu = self.driver.find_element('xpath', '/html/body/div[4]/div/div[2]/div/span[2]').text

        return emaGu

    def newEmail(self):

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(
            "https://account.proton.me/signup?plan=free&billing=12&ref=prctbl&minimumCycle=12&currency=EUR&product=mail&language=en")

        time.sleep(22)


        x = random.randint(112, 998)
        username = firstNam+ str(x)
        print("protonuser "+username)
        passowrd = ''.join(random.sample(string.ascii_letters + string.ascii_uppercase + string.digits, 15))
        print("password: " + passowrd)


        self.typeString(username)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(6)
        self.typeString(passowrd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        self.typeString(passowrd)
        time.sleep(3)

        # creteBtn=self.driver.find_element('xpath','/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button[@class="button w100 button-large button-solid-norm mt1-5"]')
        # creteBtn.click()
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(8)
        gurEmail = self.gurellaEmail()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

        emailbtn = self.driver.find_element('xpath', '//*[@id="label_1"]')
        print(emailbtn.text)
        if emailbtn.text == "Email":
            emailbtn.click()
            self.typeString(gurEmail)


        else:
            emailbtn0 = self.driver.find_element('xpath', '//*[@id="label_0"]')
            print(emailbtn0.text)
            if emailbtn0.text == "Email":
                emailbtn0.click()
                inEmail = self.driver.find_element('xpath', '//*[@id="email"]')
                inEmail.click()
                self.typeString(gurEmail)

            else:
                exit()

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[2])

        time.sleep(30)
        self.driver.refresh()
        time.sleep(5)

        dayse = Select(self.driver.find_element('xpath', '//*[@id="gm-host-select"]'))
        dayse.select_by_value("guerrillamail.com")
        """if self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr/td[2]/a').is_displayed() :

            hrefclic=self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr/td[2]/a')
            hrefclic.click()
            time.sleep(5)
           #iframe=self.driver.find_element('xpath','//*[@id="the_message_iframe"]')
            #self.driver.switch_to.frame(self,iframe)
            verCode=self.driver.find_element('xpath','/html/body/p/code').text
            self.driver.switch_to.default_content()
        else:"""
        pin = self.driver.find_element('xpath',
                                       '/html/body/div[4]/div/div[3]/div[2]/form/table/tbody/tr[1]/td[3]/span').text
        verCode = pin.split(':')[1]
        print("verification: " + verCode)
        self.driver.switch_to.window((self.driver.window_handles[1]))
        time.sleep(2)
        self.typeString(verCode)

        verBtn = self.driver.find_element('xpath', '/html/body/div[1]/div[4]/div/div/main/div[2]/button[1]')
        verBtn.click()
        time.sleep(20)

        enxtbtn = self.driver.find_element('xpath', '/html/body/div[1]/div[4]/div/div/main/div[2]/form/button')
        enxtbtn.click()
        time.sleep(10)

        savebtn = self.driver.find_element('xpath', '/html/body/div[1]/div[4]/div/div/main/div[2]/form/button[2]')
        savebtn.click()
        time.sleep(12)

        confrbtn = self.driver.find_element('xpath', '/html/body/div[4]/dialog/div/div[3]/div/button[1]')
        confrbtn.click()
        time.sleep(22)

        #keyboard.press(Key.tab)
        #keyboard.release(Key.tab)
        #keyboard.press(Key.enter)
        #keyboard.release(Key.enter)

        # WebDriverWait(self.driver,timeout=10).until(self.driver.find_element('xpath','/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button'))
        time.sleep(5)
        nxtBtn = self.driver.find_element('xpath', '/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button')
        nxtBtn.click()
        time.sleep(8)
        nxtBtnl = self.driver.find_element('xpath', '/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button[2]')
        nxtBtnl.click()
        time.sleep(3)
        getstartbtn = self.driver.find_element('xpath',
                                               '/html/body/div[4]/dialog/div/div/div[3]/div/div/footer/button[2]')
        getstartbtn.click()
        time.sleep(25)
        f=open("saveProto.txt",'a')
        f.write('\n'+username + '@proton.me,'+passowrd)
        userProto=username + '@proton.me'
        print(userProto)
        #self.doCreate(self)
        return username + '@proton.me'
    #def loginProton(self,protonAcc):


    def doCreate(self,num):
        #f=open("saveProto.txt",'a')
        reenter=False
        try:
            self.driver.get("https://facebook.com")
            p = ''.join(random.sample(string.digits, 8))
            phone = "+251" + p

            bol = False
            #self.driver.execute_script("window.open('');")
            #self.driver.switch_to.window(self.driver.window_handles[3])
            # subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --profile-directory=Default --app-id=kippjfofjhjlffjecoapiogbkgbpmgej --app-url=https://www.facebook.com/?ref=homescreenpwa --app-launch-source=4")
            #self.driver.get('https://www.facebook.com/')
            try:
                bol = self.driver.find_element('xpath', '//*[@title="Decline optional cookies"]').is_displayed()
                print(bol)

            except:
                print(bol)
            if (bol == True):
                allowbtn = self.driver.find_element('xpath', '//*[@title="Decline optional cookies"]')
                allowbtn.click()
                time.sleep(5)

            newEamil = self.newEmail()
            self.driver.switch_to.window((self.driver.window_handles[0]))
            time.sleep(1)
            create_btn = self.driver.find_element('xpath',
                                                  '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]')
            create_btn.click()


            time.sleep(3)


            #firstInput=self.driver.find_element('xpath','')
            self.typeString(firstNam)

            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

            self.typeString(lastNam)
            time.sleep(5)

            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

            if num==0:
                self.typeString(newEamil)
                time.sleep(5)

                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

                reenter = self.driver.find_element('xpath','/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input').is_displayed()
                print(reenter)
                self.typeString(newEamil)
                time.sleep(4)
            else:
                self.typeString(phone)
                time.sleep(5)

            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

            passW = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 14))
            print("password Facebook: " + passW)
            self.typeString(passW)
            time.sleep(4)

            # yearSe=Select(self.driver.find_element('xpath','//select[@aria-label="Year"]'))
            # time.sleep(6)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            dayse = Select(self.driver.find_element('xpath', '//select[@aria-label="Day"]'))
            dayse.select_by_index(random.randint(1, 28))
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            monse = Select(self.driver.find_element('xpath', '//select[@aria-label="Month"]'))
            monse.select_by_index(random.randint(1, 11))
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            yearSe = Select(self.driver.find_element('xpath', '//select[@aria-label="Year"]'))
            yearSe.select_by_index(random.randint(15, 40))
            time.sleep(6)

            gendeL = self.driver.find_element('xpath',
                                              '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1][@class="_5k_2 _5dba"]')
            gendeL.click()

            signUp = self.driver.find_element('xpath', '//button[@name="websubmit"]')
            signUp.click()
            time.sleep(25)

            try:
                continfa=self.driver.find_element('xpath','/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/span').is_displayed()
                if continfa==True:
                    self.logout()
                    self.doCreate(1)
            except:
                file = open("savefbAcc", 'a')
                file.write('\n' + newEamil + ',' + passW+','+self.counCode+',')
                print("normal")
            try:

                if (reenter==False):
                    updateCont = self.driver.find_element('xpath',
                                                          '/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/a')
                    updateCont.click()
                    time.sleep(4)

                    newEmil = self.driver.find_element('xpath', '//*[@aria-label="New email or mobile number"]')
                    newEmil.click()
                    self.typeString(newEamil)
                    print("Protonmail " + newEamil)
                    time.sleep(5)

                    addnBtn = self.driver.find_element('xpath',
                                                       '//*[@class="_42ft _4jy0 layerConfirm _8n28 _8n2a _9l2j uiOverlayButton _4jy3 _4jy1 selected _51sy"]')
                    addnBtn.click()
                    time.sleep(6)
            except:
                print("no need for update")

            self.driver.switch_to.window((self.driver.window_handles[1]))
            time.sleep(30)
            self.driver.refresh()
            time.sleep(6)

            """keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)"""

            opEmail = self.driver.find_element('xpath',
                                               '/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/main/div/div/div/div[2]/div[1]/div[@style="--index: 0;"]')

            opEmail.click()
            time.sleep(4)

            code = self.driver.find_element('xpath',
                                            '/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/main/section/div/div[3]/div/header/div/h1/span').text
            codeS = code.split(' ')
            print(codeS[0])
            codeM = codeS[0].split('-')
            print(code)

             # DatabaseWrapper.add_user(newEamil, passW)
            self.driver.switch_to.window((self.driver.window_handles[0]))
            inputFBver = self.driver.find_element('xpath', '//*[@id="code_in_cliff"]')
            inputFBver.click()
            self.typeString(codeM[1])
            time.sleep(3)

            try:
                rembtnC = self.driver.find_element('xpath', '//*[@id="link_"' + phone + ']').is_displayed()
                if rembtnC==True:
                    rembtn = self.driver.find_element('xpath', '//*[@id="link_"' + phone + ']')
                    rembtn.click()
                    time.sleep(2)
            except:
                print('notphone')
            cntbtn = self.driver.find_element('xpath',
                                              '//*[@class="_42ft mls _4jy0 _8iu3 _8iu6 _4jy4 _4jy1 selected _51sy"]')
            cntbtn.click()
            time.sleep(6)
            okbtn = self.driver.find_element('xpath', '/html/body/div[4]/div[2]/div/div/div/div[3]/div/a')
            okbtn.click()
            time.sleep(13)
            try:
                dec=self.driver.find_element('xpath','/html/body/div/div/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div')
                dec.click()
            except:
                print('not netherland')

            time.sleep(9)
            self.likePostUrl()
            time.sleep(3)
            self.postToUrl()
            time.sleep(4)
            self.resharePostUrl()
            time.sleep(5)
            self.commentPostUrl()


        except NoSuchElementException as e:
            logging.error(e)




    def search(self):
        try:
            searchdispla = self.driver.find_element('xpath',
                                                '//input[@aria-label="Search Facebook"]').is_displayed()
            if(searchdispla==True):
                searchbtn = self.driver.find_element('xpath',
                                                    '//input[@aria-label="Search Facebook"]')
                searchbtn.send_keys("Ministry of Education Ethiopia")
                searchbtn.send_keys(Keys.ENTER)
                time.sleep(10)
                searchrslt = self.driver.find_element('xpath', '//a[@href="https://www.facebook.com/fdremoe"]')
                print(searchrslt);
                searchrslt.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            logging.error(e)
            return "failed"

    def postToUrl(self, media_path='', url='https://www.facebook.com/'):
        url = url_parse(url)
        if url is None:
            return 'Bad url'
        try:
            self.driver.get(url)

            filePo=open('postsSave.txt','r')
            savePost=filePo.readlines()

            message = savePost[random.randint(1,len(savePost))]
            postbtn = self.driver.find_element('xpath',
                                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[2]')
            postbtn.click()
            time.sleep(2)
            publicpo=self.driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div')
            publicpo.click()
            donePrivacy=self.driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]')
            donePrivacy.click()
            time.sleep(3)
            textbox = self.driver.find_element('xpath',
                                                   '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate"]')
            textbox.send_keys(message)

            if media_path is not None and media_path != '' and media_path != 'None':
                current_os = platform.system()
                if current_os == 'Windows':
                    media_path = media_path.replace('/', '\\')
                upload_photo = self.driver.find_element('xpath', '//input[@name="view_photo"]')
                upload_photo.click()
                upload_photo = self.driver.find_element('xpath', '//input[@name="file1"]')
                upload_photo.send_keys(media_path)
                upload_photo = self.driver.find_element('xpath', '//input[@name="add_photo_done"]')
                upload_photo.click()

            if media_path != '' or message != '':
                mainbtn = self.driver.find_element('xpath',
                                                   '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[2]')
                mainbtn.click()
                return 'Posted to :' + url
        except NoSuchElementException and WebDriverException as e:
            logging.error(e)
            return 'Failed to post to :' + url

    def likePostUrl(self):
        try:
            #self.driver.get(url)
            likebtndispl=self.driver.find_element('xpath',
                                               '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1][@aria-label="Like"]').is_displayed()

            if(likebtndispl==True):
                likebtn = self.driver.find_element('xpath',
                                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1][@aria-label="Like"]')
                self.driver.execute_script("arguments[0].scrollIntoView();",likebtn)
                time.sleep(2)
                likebtn.click()
                return 'like post'
        except NoSuchElementException and WebDriverException as e:
            logging.error(e)
            return 'Failed to like post at :'

    def commentPostUrl(self, url):
        try:
            self.driver.get(url)
              # if(self.driver.find_element('xpath','//h4[@id="jsc_c_6u"]')):
            cmedis=self.driver.find_element('xpath',
                                                  '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz"]').is_displayed()
            if(cmedis==True):
                commentbtn = self.driver.find_element('xpath',
                                                      '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz"]')
                commentbtn.click()
                time.sleep(3)
                textbox = self.driver.find_element('xpath',
                                                   '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')
                textbox.send_keys("cool")
                formbtn = self.driver.find_element('xpath',
                                                   '//form[@class="x1ed109x x1n2onr6 xmjcpbm x1tlxs6b x1g8br2z x1gn5b1j x230xth x972fbf xcfux6l x1qhh985 xm0m39n x78zum5 x1iyjqo2 x13a6bvl x1a02dak"]')
                textbox.send_keys(Keys.ENTER)
                return 'comment done'
        except NoSuchElementException and WebDriverException as e:
            logging.error(e)
            return 'Failed to like post at :' + url

    def resharePostUrl(self, url):
        try:
            self.driver.get(url)
            # if(self.driver.find_element('xpath','//h4[@id="jsc_c_6u"]')):
            sharedisplay= self.driver.find_element('xpath',
                                                '//div[@aria-label="Send this to friends or post it on your Timeline."]').is_displayed()
            if(sharedisplay==True):
                sharebtn = self.driver.find_element('xpath',
                                                    '//div[@aria-label="Send this to friends or post it on your Timeline."]')
                sharebtn.click()
                time.sleep(3)
                shareNbtn = self.driver.find_element('xpath',
                                                     '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]')
                shareNbtn.click()
                return 'share  post'
        except NoSuchElementException and WebDriverException as e:
            logging.error(e)
            return 'Failed to like post at :' + url

    def reportPostUrl(self, url):
        try:
            self.driver.get(url)
            if (url == "https://www.facebook.com/"):
                time.sleep(4)
                dotbtn = self.driver.find_element('xpath',
                                                  '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[2]/div/div[3]/div/div[@class="x1i10hfl x1qjc9v5 xjqpnuy xa49m3k xqeqjp1 x2hbi6w x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x3nfvp2 xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x3ajldb x194ut8o x1vzenxt xd7ygy7 xt298gk x1xhcax0 x1s928wv x10pfhc2 x1j6awrg x1v53gu8 x1tfg27r xitxdhh"]')
                dotbtn.click()
                time.sleep(5)

                reportbtn = self.driver.find_element('xpath',
                                                     '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[8]/div[1]/img[@src="https://static.xx.fbcdn.net/rsrc.php/v3/y4/r/ZzfJKx3t9Ej.png"]')
                reportbtn.click()
                action = ActionChains(self.driver)

                action.key_down(Keys.ARROW_DOWN, reportbtn)

                time.sleep(5)
                falseinfobtn = self.driver.find_element('xpath',
                                                        '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[6]/div/div/div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]')
                falseinfobtn.click()
                time.sleep(4)
                polticsbtn = self.driver.find_element('xpath',
                                                      '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[2]/div/div/div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]')
                polticsbtn.click()
                time.sleep(3)
                subbtn = self.driver.find_element('xpath',
                                                  '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3"]')
                subbtn.click()
            else:
                time.sleep(5)
                dotbtn = self.driver.find_element('xpath',
                                                  '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[2]/div/div[3]/div/div[@class="x1i10hfl x1qjc9v5 xjqpnuy xa49m3k xqeqjp1 x2hbi6w x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x3nfvp2 xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x3ajldb x194ut8o x1vzenxt xd7ygy7 xt298gk x1xhcax0 x1s928wv x10pfhc2 x1j6awrg x1v53gu8 x1tfg27r xitxdhh"]')
                dotbtn.click()
                time.sleep(3)
                reportbtn = self.driver.find_element('xpath',
                                                     '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[7]/div[3][@class="x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1wpzbip"]')
                reportbtn.send_keys(Keys.ENTER)
                # dotbtn.send_keys(Keys.ARROW_DOWN)
                # dotbtn.send_keys(Keys.ARROW_DOWN)
                # dotbtn.send_keys(Keys.ENTER)
                time.sleep(6)
                falseinfobtn = self.driver.find_element('xpath',
                                                        '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[5]/div/div/div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]')
                falseinfobtn.click()
                time.sleep(2)
                polticsbtn = self.driver.find_element('xpath',
                                                      '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[2]/div/div/div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]')
                polticsbtn.click()
                time.sleep(1)
                subbtn = self.driver.find_element('xpath',
                                                  '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3"]')
                subbtn.click()
        except NoSuchElementException and WebDriverException as e:
            logging.error(e)
            return 'Failed to like post at :' + url

    def groupScraper(self, url):
        if 'groups' not in url:
            return 'Not a group url'

        url = url_parse(url)
        if url is None:
            return 'Bad url'
        try:
            self.driver.get(url + '?')
            members_btn = self.driver.find_element_by_xpath('//a[text()="Members"]')
            members_btn.click()
            members_btn = self.driver.find_element_by_xpath('//a[contains(@href,"list_nonfriend_nonadmin")]')
            members_btn.click()
            data = ''
            while True:
                members = self.driver.find_elements_by_tag_name('a')
                members.remove(self.driver.find_element_by_xpath('//a[text()="Go to Home"]'))
                for member in members:
                    if similar(member.get_attribute('href'), member.text) > 0.1 and member.text != 'See More':
                        data += member.text + ' ' + member.get_attribute('href') + '\n'
                try:
                    see_more = self.driver.find_element_by_xpath('//span[text()="See More"]')
                    see_more.click()
                except Exception:
                    break
            return data
        except NoSuchElementException and WebDriverException as e:
            logging.warning(e)
            return ''

    def logout(self):
        try:
            self.logged_in = False
            self.driver.delete_all_cookies()
            self.driver.get('https://www.facebook.com/')
            return 'Logged out successfully'
        except WebDriverException as e:
            logging.error(e)
            return 'Failed to logout'
