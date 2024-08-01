from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.window import Window

from home import Home
from plans import Plans
from emoji import Emoji
from game import Game
from analytics import Analytics

Window.size = (340, 630)
class MainPage(MDApp):
    def build(self):
        ScMa = ScreenManager(transition = WipeTransition())
        ScMa.add_widget(Home())
        ScMa.add_widget(Plans())
        ScMa.add_widget(Emoji())
        ScMa.add_widget(Game())
        ScMa.add_widget(Analytics())
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_light_hue = "A700"
        return ScMa 
    
if __name__=="__main__":
    MainPage().run()
