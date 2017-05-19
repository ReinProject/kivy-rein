from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from functionality.Database import Database
from functionality.Setting import Setting

class MainScreen(Screen):
    pass

class SignInScreen(Screen):
    pass

class ReinAndroidApp(App):
    def build(self):
    	Database()

        Builder.load_file('views\SignInScreen.kv')
        Builder.load_file('views\MainScreen.kv')

        self.sm = ScreenManager()
        self.sm.add_widget(SignInScreen(name='SignInScreen'))        
        self.sm.add_widget(MainScreen(name='MainScreen'))

        if Setting.read('delprivkey'):
            self.sm.current = 'MainScreen'

    	return self.sm

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

if __name__ == '__main__':
    ReinAndroidApp().run()
