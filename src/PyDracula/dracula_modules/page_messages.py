# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# DEFAULT PACKAGES
# ///////////////////////////////////////////////////////////////
import os
import random

from PySide6.QtCore import QTimer, QEasingCurve
# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
# from app.packages.widgets import * # Widgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

if __name__ == "__main__":
    from ui_page_messages import Ui_chat_page  # MainWindow
    from message import Message  # MainWindow
else:
    # GUI
    from dracula_modules.ui_page_messages import Ui_chat_page  # MainWindow
    from dracula_modules.message import Message  # MainWindow
    # from main import MainWindow


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class Chat(QWidget):
    def __init__(
            self,
            main_window,
            char_dict,
            chat_dict
    ):
        QWidget.__init__(self)

        self.page = Ui_chat_page()
        self.page.setupUi(self)
        self.mWindow = main_window

        self.char_info_dict = char_dict
        self.chat_info_dict = chat_dict  # for chat log

        bot_name = self.char_info_dict["character_name"]
        bot_description = self.char_info_dict["character_description"]
        bot_image = self.char_info_dict["character_image"]

        self.scroll_bar = None
        self.scroll_anim = None

        # profile image [bot, user, other]
        self.pf_img_dict: dict = {'bot': None, 'user': "mouse.png", 'other': "me.png"}
        try:
            # CROP BOT PROFILE IMAGE TO 40X40 SQAURE
            if bot_image is not None:
                # Load original profile image & set output path
                original_image = QImage(os.path.normpath(bot_image))
                image_directory = os.path.dirname(os.path.normpath(bot_image))
                output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                                           'cache',
                                           'gui')
                output_image_path = os.path.join(output_path, "profile_image_squared.png")
                # print(os.path.normpath(user_image))
                # print(output_image_path)

                # Determine the shorter side and longer side
                width = original_image.width()
                height = original_image.height()
                shorter_side = min(width, height)
                longer_side = max(width, height)

                # Calculate the coordinates for cropping
                margin = float(longer_side - shorter_side) / 2.0

                # TODO: test square image & width's longer iamge
                if width > height:
                    x = margin
                    y = 0
                else:
                    x = 0
                    y = margin

                # Create a square image by cropping the shorter side
                square_image = original_image.copy(x, y, shorter_side, shorter_side)

                # Resize the square image to 40x40 pixels
                resized_image = square_image.scaled(40, 40)

                # Save resized image to png
                resized_image.save(output_image_path)

                self.pf_img_dict['bot'] = output_image_path

                # UPDATE INFO
                self.page.user_image.setStyleSheet(
                    "#user_image { background-image: url(\"" + output_image_path.replace("\\", "/") + "\") }")
                # self.page.user_image.setPixmap(QPixmap(resized_image))

            else:
                raise Exception('no bot profile image set')
        except Exception as e:
            print("[GUI] ERROR: ", e)

        self.page.user_name.setText(bot_name)
        self.page.user_description.setText(bot_description)
        self.page.chat_log_filename.setText(self.chat_info_dict["chatlog_filename"])

        # PROFILE BUTTONS (TOP RIGHT)
        self.page.btn_open_folder.clicked.connect(self.buttonClick)
        self.page.btn_more_top.clicked.connect(self.buttonClick)

        # CHANGE PLACEHOLDER TEXT
        format_user_name = bot_name.replace(" ", "_").replace("-", "_")
        format_user_name = format_user_name.lower()
        self.page.line_edit_message.setPlaceholderText(f"Message #{str(format_user_name).lower()}")

        # ENTER / RETURN PRESSED
        self.page.line_edit_message.keyReleaseEvent = self.enter_return_release

        # ENTER / RETURN PRESSED
        self.page.btn_send_message.clicked.connect(self.send_message_entry)

        # LOAD CHAT LOG
        self.load_chat_log()

    # ENTER / RETURN SEND MESSAGE
    def enter_return_release(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.send_message_entry()

    # Send From Entry TextEdit
    def send_message_entry(self):
        entry_text = self.page.line_edit_message.text()
        if entry_text != "":
            self.send_by_user(entry_text, self.pf_img_dict['user'])
            # self.message = Message(self.page.line_edit_message.text(), 'user')
            self.page.chat_messages_layout.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
            self.page.line_edit_message.setText("")
            self.message.data_message.setText(self.char_info_dict["your_name"])

            self.generate_reply(entry_text)

    # SEND MESSAGE BY USER
    def send_by_user(self, text, pf_img=None):
        self.message = Message(text, 'user', pf_img)
        self.page.chat_messages_layout.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
        # self.page.line_edit_message.setText("")

    # SEND MESSAGE BY FRIEND
    def send_by_bot(self, text, pf_img=None):
        self.message = Message(text, 'bot', pf_img)
        self.page.chat_messages_layout.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
        # self.page.line_edit_message.setText("")

    def send_by_other(self, text, pf_img=None):
        self.message = Message(text, 'other', pf_img)
        self.page.chat_messages_layout.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
        # self.page.line_edit_message.setText("")

    def load_chat_log(self):
        chatlog_str = self.chat_info_dict["chatlog"]
        lines = chatlog_str.strip().splitlines()
        char_name = self.char_info_dict["character_name"]
        your_name = self.char_info_dict["your_name"]

        for line in lines:

            # prefix = line.split(":")[0].strip()
            # line = line.split(":")[1].strip()
            split_parts = line.split(":", 1)
            prefix = split_parts[0].strip()
            line = split_parts[1].strip()

            if prefix == char_name:
                # print(f"Bot said: {line}")
                self.send_by_bot(line, self.pf_img_dict['bot'])
            elif prefix == your_name:
                # print(f"You said: {line}")
                self.send_by_user(line, self.pf_img_dict['user'])
            else:  # Other character    # TODO: when other character spoken, display name & other profile_image
                # print(f"{prefix} said: {line}")
                self.send_by_other(line, self.pf_img_dict['other'])

            # ADD Name label under message label
            self.message.data_message.setText(prefix)

    #######################################################################################################
    # SCROLL METHODS
    #######################################################################################################
    # set
    def set_scroll_value(self, value):
        if self.scroll_bar is None:
            self.scroll_bar = self.page.chat_messages.verticalScrollBar()
        self.scroll_bar.setValue(value)

    def scroll_to_end(self):
        if self.scroll_bar is None:
            self.scroll_bar = self.page.chat_messages.verticalScrollBar()
        self.set_scroll_value(self.get_scroll_max_value())

    # get
    def get_scroll_value(self):
        if self.scroll_bar is None:
            self.scroll_bar = self.page.chat_messages.verticalScrollBar()
        return self.scroll_bar.value()

    def get_scroll_max_value(self):
        if self.scroll_bar is None:
            self.scroll_bar = self.page.chat_messages.verticalScrollBar()
        return self.scroll_bar.maximum()

    # EMULATE SCROLL ANIMATION
    # last_value = start_scroll_value, value = end_scrol_value, time = seconds_to_animation
    def scroll_to_animation(self, last_value=0, value=-1, time=1):
        try:
            if self.scroll_bar is None:
                self.scroll_bar = self.page.chat_messages.verticalScrollBar()

            if self.scroll_anim is None:
                self.scroll_anim = self.scroll_anim = QPropertyAnimation(self.scroll_bar, b"value")

            time = time * 1000  # time: 1 -> 1000ms
            self.scroll_anim.setDuration(time)
            self.scroll_anim.setStartValue(last_value)

            if value == -1:
                self.scroll_anim.setEndValue(self.get_scroll_max_value())
            else:
                self.scroll_anim.setEndValue(value)
            self.scroll_anim.setEasingCurve(QEasingCurve.OutQuad)
            self.scroll_anim.start()
        except Exception as e:
            print("\033[31m" + "Error [page_message.scroll_to_end_animation]: " + f"{e}" + "\033[0m")

    #######################################################################################################

    def generate_reply(self, text):
        from generate import Generator  # noqa

        # refresh other info (load max prompt/reply tokens)
        self.mWindow.load_prompt_info()
        self.mWindow.load_other_info()

        gen = Generator()
        # text_lang_code = language_detection(text)

        audio_info_dict = self.mWindow.audio_info_dict
        prompt_info_dict = self.mWindow.prompt_info_dict

        # setting_list = [None, self.char_info_dict, self.chat_info_dict]
        setting_list = [audio_info_dict, self.char_info_dict, prompt_info_dict, self.chat_info_dict]
        reply_txt = gen.generate(text, setting_list)

        # reply_txt = "test"

        if reply_txt is None or reply_txt == "":
            print("\033[31m" + "Error [GUI/page_messages]: failed to generate reply." + "\033[0m")
            self.mWindow.after_generate_reply(-1)
        else:
            self.mWindow.after_generate_reply()  # call method from main window [GUI]

            gen.speak_tts(reply_txt, setting_list)  # tts testing

    ####
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        widgets = self.page

        # SHOW HOME PAGE
        if btnName == "btn_open_folder":
            print(btnName)
            chatlog_path = self.mWindow.get_chatlog_path()
            # chatlog_path = os.path.dirname(chatlog_path)
            # os.startfile(chatlog_path)

            import subprocess
            try:
                subprocess.Popen(["explorer", "/select,", chatlog_path])
            except Exception as e:
                print("\033[31m" + "Error [page_messages.buttonClick]: Failed to Open Folder" + "\n\033[33m" + f"▲ {e}" + "\033[0m")


        # SHOW CHARACTER PAGE
        if btnName == "btn_more_top":
            print(btnName)

if __name__ == "__main__":
    print()
    output_image_url_test = "test"
    print("#user_image { background-image: url(\"" + output_image_url_test.replace("\\", "/") + "\") }")
    # C:\Users\HWcoms\Blessing-AI\cache\gui # dest folder
    # C:\Users\HWcoms\Blessing-AI\src\PyDracula
