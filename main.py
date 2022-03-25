
from ast import Return
from itertools import count
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.metrics import dp, sp
# import requests

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from kivymd.uix.list import ThreeLineListItem
# from kivymd.uix.label import MDLabel
# from kivymd.uix.menu import MDDropdownMenu
# from kivymd.uix.picker import MDDatePicker
# from kivymd.uix.list import TwoLineIconListItem,TwoLineListItem
from kivymd.uix.card import MDCard
# from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.core.window import Window
w=Window.size = 360,600










class WelcomeScreen(Screen):
    pass


class MainPage(Screen):
    pass

class ProductsPage(Screen):

    pass


class AboutPage(Screen):
    pass


class ProfilePage(Screen):
    pass


sm = ScreenManager()

sm.add_widget(WelcomeScreen(name='WelcomeScreen'))
sm.add_widget(MainPage(name='MainPage'))
sm.add_widget(AboutPage(name='AboutPage'))
sm.add_widget(ProfilePage(name='ProfilePage'))
sm.add_widget(ProductsPage(name='ProductsPage'))



class Main(MDApp):
    path_to_kv_file='kv_file.kv'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackKey)


    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.theme_style = "Dark"


        self.screen_list = []

        self.custom_name = 'Company Name'


        text_file = open('hotreloader.kv','r')
        KV= text_file.read()
        self.builder = Builder.load_string(KV)
        
        self.builder = Builder.load_file('kv_file.kv')

        
        
        
        return self.builder

    def update_kv_files(self,text):
        
        with open(self.path_to_kv_file,"w+") as kv_file:
            kv_file.write(text)

    def change_screen(self,screen,animation):
        if not self.builder.ids.screen_manager.current in self.screen_list:
            self.screen_list.append(self.builder.ids.screen_manager.current)
        
        self.builder.ids.screen_manager.current = screen
        self.builder.ids.screen_manager.transition.direction=animation
        print(self.screen_list)

    def onBackKey(self,window,key,*args):
        back_count = 0
        if key ==27 and self.screen_list ==[]:
            
            return False

            
        elif key ==27:
            self.builder.ids.screen_manager.current = self.screen_list.pop()
            return True
    def toggle_nav(self):
            self.root.ids.nav_drawer.set_state('toggle')


    def show_dialog(self, title, text):
        title = title
        text = text
        cancel_btn_username_dialouge = MDFlatButton(
            text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title=text, text=text, size_hint=(
            0.7, 0.2), buttons=[cancel_btn_username_dialouge])
        self.dialog.open()

    def close_dialog(self, obj):
            self.dialog.dismiss()
        
if __name__=='__main__':
    Main().run()