from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests
from firebase import firebase
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button

help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    DataScreen:
    HistoryScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    Image:
        source:'green.png'
        allow_stretch: True
        keep_ratio: False



    MDRaisedButton:
        text:' Login '
        pos_hint : {'center_x':0.3,'center_y':0.2}
        size_hint: (0.13,0.0)
        md_bg_color: (0,0,0,1)
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.7,'center_y':0.2}
        size_hint: (0.13,0.0)
        md_bg_color: (0,0,0,1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        color: 1, 1, 1, 1
        helper_text:'Required'
        color: 1, 1, 1, 1
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        password: True
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        color: 1, 1, 1, 1
        helper_text:'Required'
        color: 1, 1, 1, 1
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"

    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        md_bg_color: (0,0,0,1)
        on_press:
            app.login()
            app.username_changer()



    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'




<SignupScreen>:
    name:'signupscreen'

    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        md_bg_color: (0,0,0,1)
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()

    MDTextButton:
        text: 'Already have an account?'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'




<MainScreen>:
    name: 'mainscreen'
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H3'
        halign:'center'

    MDRaisedButton:
        text:'View My Data'
        background_color: 0,0,0,1
        size_hint: (0.13,0.07)
        md_bg_color: (0,0,0,1)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:

            root.manager.current = 'datascreen'
            root.manager.transition.direction = 'left'
    MDTextButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'

<DataScreen>:

    name: 'datascreen'
    on_enter:app.info()
    MDTextButton:
        text: 'History'
        pos_hint: {'center_x':0.9,'center_y':0.9}
        on_press:
            root.manager.current = 'historyscreen'
            root.manager.transition.direction = 'left'

    MDTextButton:
        text: 'Back'
        pos_hint: {'center_x':0.1,'center_y':0.9}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'right'






<HistoryScreen>:
    name: 'historyscreen'
    id: historyscreen
    on_enter:app.his()

    MDTextButton:
        text: 'Back'
        pos_hint: {'center_x':0.1,'center_y':0.9}
        on_press:
            root.manager.current = 'datascreen'
            root.manager.transition.direction = 'right'














'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class DataScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(DataScreen(name='datascreen'))
sm.add_widget(HistoryScreen(name='historyscreen'))


class SmartEnergyMeterApp(MDApp):
    Window.size = (400, 600)

    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://iotelectricity-4e14d-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print(to_database)
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'vXIAO1PxN9AmZf1oTaMsQVmlJeOVJN7qLME2qUfM'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text
        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"Welcome {self.username}"

    def info(self):
        screen = Screen()
        fb_app = firebase.FirebaseApplication('https://iotelectricity-4e14d-default-rtdb.firebaseio.com/', None)

        refresh_button = Button(text='Refresh', size_hint=(0.2, 0.07), pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                background_color=[0, 0, 0, 1])
        refresh_button.bind(on_release=self.refresh)
        self.strng.get_screen('datascreen').add_widget(refresh_button)

        result = str(fb_app.get('/Current', None)) + " Watts"
        result1 = str(fb_app.get('/Power', None)) + " Amps"
        result2 = str(fb_app.get('/Energy', None)) + " Joules"
        result4 = "Php " + str(fb_app.get('/Bill', None))

        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.9, 0.6), rows_num=7,
                            column_data=[
                                ("Data", dp(30)),

                                ('Readings', dp(30))
                            ],
                            row_data=[
                                ("Current", result),
                                ("Power", result1),
                                ("Energy", result2),
                                ("Bill", result4)])

        self.strng.get_screen('datascreen').add_widget(table)
        return screen

    def refresh(self, instance):
        # Refresh the data in the table
        self.info()

    def his(self):
        screen: Screen = Screen()
        fb_app = firebase.FirebaseApplication('https://iotelectricity-4e14d-default-rtdb.firebaseio.com/', None)

        result4 = fb_app.get('/History Bill', None)
        filtered_data = filter(lambda x: 'Php' in x, result4.values())
        filtered_data_list = list(filtered_data)
        latest = str(fb_app.get('Php' + '/Bill', None))

        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.9, 0.6), rows_num=30,
                            column_data=[("Recent Bill", dp(30)), ('      ', dp(10)), ('      ', dp(30))],
                            row_data=[(f"Previous {i + 1}", " ", filtered_data_list[i])
                                      for i in range(-1, -len(filtered_data_list), -1)])

        refresh_btn = Button(text='Refresh', size_hint=(0.2, 0.07), pos_hint={'center_x': 0.5, 'center_y': 0.1},
                             background_color=[0, 0, 0, 1])
        refresh_btn.bind(on_press=self.refresh_data)
        self.strng.get_screen('historyscreen').add_widget(table)
        self.strng.get_screen('historyscreen').add_widget(refresh_btn)
        return screen

    def refresh_data(self, instance):
        # code to refresh the data in the table
        self.his()


SmartEnergyMeterApp().run()
