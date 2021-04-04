from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.theming import ThemeManager

Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDLabel kivymd.label.MDLabel
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton


<AddFilm@Screen>

    BoxLayout:
        
        orientation: 'vertical'
        MDToolbar:
            title: 'Добавить фильм'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            pos_hint: {'center_x': .5, 'center_y': .5}
            elevation: 10 
            left_action_items: [['arrow-left', lambda x: root.back_to_previous_screen()]]  
            
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(5)
            padding: dp(100)
            Screen:
                
                MDTextField:
                    pos_hint: {'center_x': .5, 'center_y': .9}
                    id: name_film
                    hint_text: 'Название фильма'
                MDRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .2}
                    text: 'Сохранить этот фильм'

''')

def back_to_menu(self):
    App.get_running_app().scr_mngr.current = "menu"


class InputApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Добавить фильм"
    main_widget = None

    def build(self):
        return Factory.AddFilm()


InputApp().run()