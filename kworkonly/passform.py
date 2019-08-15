import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
# Configure window by 300x300
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
# Class form of password
class MainLayout(BoxLayout):
    pass
class MainPassWidget(BoxLayout):
    pass
class PassFormApp(App):
    def build(self):
        passwj = MainLayout()
        return passwj
    
        
if __name__ == "__main__":
    PassFormApp().run()
