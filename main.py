from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from functionality.Database import Database
from functionality.Setting import Setting
from functionality.main_screen import set_user_job_data

class MainScreen(Screen):
    pass

class SignInScreen(Screen):
    pass

class JobScreen(Screen):
    pass

class ReinAndroidApp(App):
    def build(self):
        Builder.load_file('views/CustomLabel.kv')
        Builder.load_file('views/CustomButton.kv')
        Builder.load_file('views/CustomInput.kv')
        Builder.load_file('views/CustomHeader.kv')
        Builder.load_file('views/CustomBackground.kv')
        Builder.load_file('views/SignInScreen.kv')
        Builder.load_file('views/MainScreen.kv')
        Builder.load_file('views/JobScreen.kv')

        self.sm = ScreenManager()
        self.sm.add_widget(SignInScreen(name='SignInScreen'))        
        self.sm.add_widget(MainScreen(name='MainScreen'))
        self.sm.add_widget(JobScreen(name='JobScreen'))

        if Setting.read('delprivkey'):
            self.sm.current = 'MainScreen'
            set_user_job_data(self.sm)

    	return self.sm

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

if __name__ == '__main__':
    ReinAndroidApp().run()
