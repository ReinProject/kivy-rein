from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from functionality.Database import Database
from functionality.Setting import Setting
from functionality.main_screen import set_user_job_data
from functionality.queries import KNOWN_SERVERS

class MainScreen(Screen):
    pass

class SignInScreen(Screen):
    pass

class JobScreen(Screen):
    pass

class ReinAndroidApp(App):
    def build(self):
        Database()

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

        self.sm.current = 'SignInScreen'
        if Setting.read('delprivkey'):
            self.sm.current = 'MainScreen'
            set_user_job_data(self.sm)

        server_available = False
        for server in KNOWN_SERVERS:
            try:
                response = requests.get('http://{}'.format(server))
                server_available = True

            except:
                pass
        
        if not server_available:
            current_screen = self.sm.get_screen(self.sm.current)
            print(current_screen)
            print(current_screen.ids)
            current_screen.ids['alertHeader'].text = 'No server is currently reachable'

    	return self.sm

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

if __name__ == '__main__':
    ReinAndroidApp().run()
