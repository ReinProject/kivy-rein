from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import requests

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

        self.screen_setup()

    	return self.sm

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

    def load_widgets(self):
        widgets = ['CustomLabel', 'CustomButton', 'CustomInput', 
            'CustomHeader', 'CustomBackground', 
            'SignInScreen', 'MainScreen', 'JobScreen']
        for widget in widgets:
            Builder.load_file('views/{}.kv'.format(widget))

    def screen_setup(self):
        self.load_widgets()

        self.sm = ScreenManager()
        self.sm.add_widget(SignInScreen(name='SignInScreen'))        
        self.sm.add_widget(MainScreen(name='MainScreen'))
        self.sm.add_widget(JobScreen(name='JobScreen'))

        self.sm.current = 'SignInScreen'
        if Setting.read('delprivkey'):
            self.sm.current = 'MainScreen'
            set_user_job_data(self.sm)

        #self.set_status_bar_colour()
        self.available_servers_feedback()

    def available_servers_feedback(self):
        server_available = False
        for server in KNOWN_SERVERS:
            try:
                response = requests.get('http://{}'.format(server), timeout=1)
                server_available = True

            except:
                pass
        
        if not server_available:
            current_screen = self.sm.get_screen(self.sm.current)
            current_screen.ids['alertHeader'].text = 'No server is currently reachable'

    def set_status_bar_colour(self):
        """Dysfunctional due to https://github.com/kivy/pyjnius/issues/278"""

        try:
            # Turn status bar green
            from jnius import autoclass
            from jnius.jnius import JavaException

            #try:
            LayoutParams = autoclass('android.view.WindowManager$LayoutParams')
            R = autoclass('android.R')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            window = activity.getWindow()
            LayoutParams = window.getAttributes()
            window.clearFlags(LayoutParams.FLAG_TRANSLUCENT_STATUS)
            window.addFlags(LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
            window.setStatusBarColor(activity.getResources().getColor(R.color.holo_green_light))

           #except JavaException as ex:
                # Insufficient SDK version
                #pass

        except ImportError:
            # Not on Android
            pass

if __name__ == '__main__':
    ReinAndroidApp().run()
