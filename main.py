from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button


Window.size = (270, 585)

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class S3Window(Screen):
    pass
class S4Window(Screen):
    pass
class S5Window(Screen):
    pass                
class S6Window(Screen):
    pass
class S7Window(Screen):
    pass
class S8Window(Screen):
    pass
class S9Window(Screen):
    pass
class S10Window(Screen):
    pass
class S11Window(Screen):
    pass
class S12Window(Screen):
    pass
class S13Window(Screen):
    pass
class S14Window(Screen):
    pass
class S15Window(Screen):
    pass
class S16Window(Screen):
    pass
class S17Window(Screen):
    pass
class S18Window(Screen):
    pass
class S19Window(Screen):
    pass
class S20Window(Screen):
    pass
class S21Window(Screen):
    pass
class S22Window(Screen):
    pass
class S23Window(Screen):
    pass
class S24Window(Screen):
    pass
class S25Window(Screen):
    pass
class S26Window(Screen):
    pass
class S27Window(Screen):
    pass
class S28Window(Screen):
    pass
class S29Window(Screen):
    pass
class S30Window(Screen):
    pass
class S31Window(Screen):
    pass
class S32Window(Screen):
    pass
class S33Window(Screen):
    pass
class S34Window(Screen):
    pass
class S35Window(Screen):
    pass
class S36Window(Screen):
    pass
class S38Window(Screen):
    pass
class S39Window(Screen):
    pass
class S40Window(Screen):
    pass
class S41Window(Screen):
    pass
class S42Window(Screen):
    pass                                                                                                                                               
class WindowScreen(ScreenManager):
    pass

kv = Builder.load_file('screens.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return kv
if __name__ == '__main__':
    MyApp().run()            

