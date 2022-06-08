from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
        pass

class BMIScreen(Screen,FloatLayout):
        def __init__(self,**kwargs):
            super(BMIScreen, self).__init__(**kwargs)
        def calc(self,m,s):
                if m != "" and s != "":
                                try:
                                        return str(round((float(s)/(float(m)**2)),2))
                                except Exception:
                                        return "Error"
                else:
                        return ""
        def weight(self,a):
                if a == "":
                        return ""       
                else:
                        try:
                                if  float(a)<= 18.5:
                                        return "Underweight"
                                elif  float(a)<= 25:
                                        return "Normal"
                                elif  float(a)<= 30:
                                        return "Overweight"
                                elif  float(a)<= 35:
                                        return "Obese"
                                else:
                                        return "Extremely obese"
                        except Exception:
                                return "Error"
class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("file.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
        MainApp().run()
