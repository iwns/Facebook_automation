from datetime import datetime as dt

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog

from Modules.Bot import Bot
from Modules.TaskExecuteThread import Task, TaskExecuteThread
from UI.Post_Ui_Dialog import Post_Ui_Dialog

#from UI.Users_Ui_Dialog import Users_Ui_Dialog


def now_str():
    return dt.now().strftime("%d/%m/%Y %H:%M:%S")

fileAcc = open('savefbAcc', 'r')
user=fileAcc.readlines()
postsave = open('postsSave.txt','r')
post=postsave.readlines()

class Ui_MainWindow(object):

    def __init__(self):
        self.bot = None
        #self.db_wrap = DatabaseWrapper()
        self.task_execute = TaskExecuteThread()
        self.media_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.posts_label = QtWidgets.QLabel(self.centralwidget)
        self.users_label = QtWidgets.QLabel(self.centralwidget)
        self.users_label.setObjectName("users_label")
        self.verticalLayout_4.addWidget(self.users_label)
        self.users_listwidget = QtWidgets.QListWidget(self.centralwidget)#.setSelectionMode(self,)
        self.users_listwidget.setObjectName("users_listwidget")
        self.verticalLayout_4.addWidget(self.users_listwidget)
        #self.users_listwidget.setSelectionMode(self,3)

        self.delete_userl_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_userl_btn.setObjectName("delete_userl_btn")
        self.verticalLayout_4.addWidget(self.delete_userl_btn)
        self.posts_label.setObjectName("posts_label")
        self.verticalLayout_4.addWidget(self.posts_label)
        self.posts_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.posts_listwidget.setObjectName("posts_listwidget")
        self.verticalLayout_4.addWidget(self.posts_listwidget)
        self.delete_post_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_post_btn.setObjectName("delete_post_btn")
        self.verticalLayout_4.addWidget(self.delete_post_btn)
        self.add_new_post_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_post_btn.setObjectName("add_new_post_btn")
        self.verticalLayout_4.addWidget(self.add_new_post_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.headless_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.headless_checkBox.setObjectName("headless_checkBox")
        self.horizontalLayout_3.addWidget(self.headless_checkBox)
        """self.load_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_file_btn.setObjectName("load_file_btn")
        self.horizontalLayout_3.addWidget(self.load_file_btn)"""
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_3.addWidget(self.login_btn)
        self.Create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Create_btn.setObjectName("Create_btn")
        self.horizontalLayout_3.addWidget(self.Create_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setObjectName("output_label")
        self.verticalLayout_5.addWidget(self.output_label)
        self.output_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.output_textedit.setMinimumSize(QtCore.QSize(256, 0))
        self.output_textedit.setReadOnly(True)
        self.output_textedit.setObjectName("output_textedit")
        self.verticalLayout_5.addWidget(self.output_textedit)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.init_users_combobox()
       # self.get_user_data()
       # self.users_combobox.currentTextChanged.connect(self.get_user_data)
        self.delete_userl_btn.clicked.connect(self.delete_user)
        self.add_new_post_btn.clicked.connect(self.add_post)
        #self.edit_post_btn.clicked.connect(self.edit_post)
        self.delete_post_btn.clicked.connect(self.delete_post)
        self.login_btn.clicked.connect(self.on_login)
        self.Create_btn.clicked.connect(self.Create)
        self.task_execute.task_added_signal.connect(self.task_added)
        self.task_execute.task_removed_signal.connect(self.task_removed)
        self.task_execute.stopped_signal.connect(self.task_execute_stopped)
        self.task_execute.task_not_found_signal.connect(self.task_not_found)
        self.task_execute.task_timeout_signal.connect(self.task_timeout)
        self.task_execute.task_completed_signal.connect(self.task_completed)
        self.task_execute.started_signal.connect(self.task_execute_started)
       # self.load_file_btn.clicked.connect(self.load_data_from_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Facebook-Bot"))

        self.users_label.setText(_translate("MainWindow", "Existing Users:"))
        #self.edit_userl_btn.setText(_translate("MainWindow", "Edit User"))
        self.delete_userl_btn.setText(_translate("MainWindow", "Delete User"))
        #self.add_new_user_btn.setText(_translate("MainWindow", "Add User"))
        self.posts_label.setText(_translate("MainWindow", "Posts:"))
        #self.edit_post_btn.setText(_translate("MainWindow", "Edit Post"))
        self.delete_post_btn.setText(_translate("MainWindow", "Delete Post"))
        self.add_new_post_btn.setText(_translate("MainWindow", "Add post"))

        self.headless_checkBox.setText(_translate("MainWindow", "Hide Browser"))
       # self.load_file_btn.setText(_translate("MainWindow", "Load File"))
        self.login_btn.setText(_translate("MainWindow", "Login"))

        self.Create_btn.setText(_translate("MainWindow", "Create"))
        self.output_label.setText(_translate("MainWindow", "Output:"))

    def init_users_combobox(self):

        userLen=len(user)
        print(userLen)
        postlen = len(post)

        print(postlen)

        self.users_listwidget.clear()
        self.users_listwidget.addItems({"{}".format(user[x].split(',')[0]) for x in range(userLen)})
        self.posts_listwidget.clear()
        self.posts_listwidget.addItems({"{}".format(post[posts]) for posts in range(postlen)})
        print({"{}:{}".format(user[x].split(',')[0], user[x].split(',')[1]) for x in range(userLen)})



    def get_current_user_id(self):
        user_id =self.users_listwidget.currentItem()

        print(user_id.text())
        return user_id.text() if user_id.text() != '' else None

    def delete_user(self):
        userselected = self.users_listwidget.currentItem()
        print(userselected)
        if userselected is None:
            self.output_textedit.insertPlainText(f"[{now_str()}] Select post to delete, aborting...\n")
            return

        msg = userselected.text()
        print(msg)
        # media_path = post.text().split(' | ')[1]
        # if media_path == "None":
        #   media_path = None
        if msg:

            print(user)
            usrlen = len(user)
            print(usrlen)

            for x in range(usrlen):
                print(user[x].split(','))
                if user[x].split(',')[0] == msg:
                    print(user[x])
                    msgrmv=user[x]
                    user.remove(msgrmv)
                    break
            print(user)
            print(len(user))
            usrEdit = open('savefbAcc', 'w')
            usrEdit.write(''.join(user))
            self.init_users_combobox()
            self.output_textedit.insertPlainText(f"[{now_str()}] user was deleted successfully.\n")
            # self.get_user_data()
        else:
            self.output_textedit.insertPlainText(f"[{now_str()}] Failed to delete post.\n")


    def delete_post(self):
        postselected = self.posts_listwidget.currentItem()
        print(postselected)
        if post is None:
            self.output_textedit.insertPlainText(f"[{now_str()}] Select post to delete, aborting...\n")
            return

        msg = postselected.text()
        print(msg)
        #media_path = post.text().split(' | ')[1]
        #if media_path == "None":
         #   media_path = None
        if msg:

            print(post)
            post.remove(msg)
            postlen=len(post)
            print(postlen)
            postEdit = open('postsSave.txt', 'w')
            postEdit.write(''.join(post))
            self.init_users_combobox()
            self.output_textedit.insertPlainText(f"[{now_str()}] Post was deleted successfully.\n")
            #self.get_user_data()
        else:
            self.output_textedit.insertPlainText(f"[{now_str()}] Failed to delete post.\n")


    def add_post(self):
        def accepted():
            msg = dialog.ui.post_content_text_edit.toPlainText()
            media = self.media_path
            if not msg and not media:
                self.output_textedit.insertPlainText(f"[{now_str()}] invalid post values, aborting...\n")
                return
            if msg:
                print(msg)
                postadd = open('postsSave.txt','a')
                postadd.write('\n'+msg)
                self.output_textedit.insertPlainText(f"[{now_str()}] post was added successfully.\n")
            else:
                self.output_textedit.insertPlainText(f"[{now_str()}] Failed to add new post.\n")

        def rejected():
            self.output_textedit.insertPlainText(f"[{now_str()}] post addition was canceled.\n")

        dialog = QDialog()
        dialog.ui = Post_Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.ui.browse_media_button.clicked.connect(self.openImageDialog)
        dialog.ui.buttonBox.accepted.connect(accepted)
        dialog.ui.buttonBox.rejected.connect(rejected)
        dialog.exec_()
        self.media_path = None



    def Create (self):
        if not self.bot:
            self.bot = Bot(self.headless_checkBox.isChecked())
        else:
            self.bot.check_browser_state()
        self.output_textedit.insertPlainText(f'[{now_str()}]{self.bot.doCreate(0)}\n')

    def comment(self):
        self.output_textedit.insertPlainText(
            f'[{now_str()}] {self.bot.commentPostUrl(url="https://www.facebook.com/")}.\n')

    def task_added(self, task_name):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task with task name: {task_name} has been added.\n')

    def task_removed(self, task_name):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task with task name: {task_name} has been removed.\n')

    def task_execute_started(self):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task executor started.\n')

    def task_execute_stopped(self):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task executor stopped.\n')

    def task_not_found(self):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task not found.\n')

    def task_timeout(self, task_name):
        self.output_textedit.insertPlainText(f'[{now_str()}] Task timeout with task name: {task_name}\n')

    def task_completed(self, task_name):
        self.output_textedit.insertPlainText(
            f'[{now_str()}] Task with task name: {task_name} completed successfully \n')

    def openImageDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose media file", "",
                                                  "Mobile Video(*.3g2);;Mobile Video(*.3gp);;Mobile Video(*.3gpp);;Windows Media Video(*.asf);;AVI(*.avi);;MPEG Video(*.dat);;DIVX Video(*.divx);;DV Video(*.dv);;Flash Video(*.f4v);;Flash Video(*.flv);;Graphics Interchange Format(*.gif);;M2TS Video(*.m2ts);;MPEG-4 Video(*.m4v);;Matroska Format(*.mkv);;MOD Video(*.mod);;QuickTime Movie(*.mov);;MPEG-4 Video(*.mp4);;MPEG Video(*.mpe);;MPEG Video(*.mpeg);;MPEG-4 Video(*.mpeg4);;MPEG Video(*.mpg);;AVCHD Video(*.mts);;Nullsoft Video(*.nsv);;Ogg Media Format(*.ogm);;Ogg Video Format(*.ogv);;QuickTime Movie(*.qt);;TOD Video(*.tod);;MPEG Transport Stream(*.ts);;DVD Video(*.vob);;Windows Media Video(*.wmv);;BMP(*.bmp);;DIB(*.dib);;HEIC(*.heic);;HEIF(*.heif);;IFF(*.iff);;JFIF(*.jfif);;JP2(*.jp2);;JPE(*.jpe);;JPEG(*.jpeg);;JPG(*.jpg);;PNG(*.png);;PSD(*.psd);;TIF(*.tif);;TIFF(*.tiff);;WBMP(*.wbmp);;WEBP(*.webp);;XBM(*.xbm)",
                                                  options=options)
        if fileName:
            self.media_path = fileName

    def on_logout(self):
        self.output_textedit.insertPlainText(f'[{now_str()}] {self.bot.logout()}\n')
        #self.users_combobox.setEnabled(True)
        #self.edit_user_btn.setEnabled(True)
        #self.delete_user_btn.setEnabled(True)

    def on_login(self):
        #user_id = self.get_current_user_id()
        """for user in self.db_wrap.get_users():
            user_id = user[0] #self.get_current_user_id()
            if user_id is None:
                return
            current_user = self.db_wrap.get_user_by_id(user_id)
            user_val = current_user[1]
            print(user_val)
            pass_val = current_user[2]
            print(pass_val)
            if not self.bot:
                self.bot = Bot(self.headless_checkBox.isChecked())
            else:
                self.bot.check_browser_state()"""
        fileAccl=open("savefbAcc","r")
        user = fileAccl.readlines()
        userLen = len(user)
        print(userLen)

        for x in range(userLen):
            print("reach here")
            user_val=user[x].split(',')[0]
            print(user_val)
            pass_val=user[x].split(',')[1]
            print(pass_val)
            country=user[x].split(',')[2]
            print(country)
            if not self.bot:
                self.bot = Bot(self.headless_checkBox.isChecked())
            else:
                self.bot.check_browser_state()

            self.output_textedit.insertPlainText(f'[{now_str()}] {self.bot.doLogin( user_val , pass_val,country)}\n')

    def on_report(self):
        if not self.bot:
            self.bot = Bot(self.headless_checkBox.isChecked())
        else:
            self.bot.check_browser_state()
        self.output_textedit.insertPlainText(f'[{now_str()}]{self.bot.reportPostUrl(url="https://www.facebook.com/")}\n')

    def on_post(self):
        if self.bot is None or not self.bot.logged_in:
            self.output_textedit.insertPlainText(f'[{now_str()}] You need to log in first.\n')
            return
        post = self.posts_listwidget.currentItem()

        if post is None:
            self.output_textedit.insertPlainText(f'[{now_str()}] You need Image or Message to post.\n')
            return
        media = post.text().split(' | ')[1]
        msg = post.text().split(' | ')[0]
        self.output_textedit.insertPlainText(
            f'[{now_str()}] {self.bot.postToUrl(url="https://www.facebook.com/", media_path=media, message=msg)}.\n')
        """"targets ='https://www.facebook.com/'
        if len(targets) == 0:
            self.output_textedit.insertPlainText(f'[{now_str()}] You need url to post.\n')
            return
       
        if len(targets) == 1:
            target = targets.pop().text()
            
        else:
            for target in targets:
                self.output_textedit.insertPlainText(
                    f'[{now_str()}] {self.bot.postToUrl(url=target.text(), media_path=media, message=msg)}.\n')"""

    def load_data_from_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose a file", options=options)
        if fileName:
            if self.db_wrap.load_data(file_path=fileName, owner_id=self.get_current_user_id()) == 'SUCCESS':
                self.output_textedit.insertPlainText(f'[{now_str()}] Successfully loaded the file.\n')
            else:
                self.output_textedit.insertPlainText(
                    f'[{now_str()}] Something went wrong while trying to load the file.\n')
            self.get_user_data()
