from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.cards import MDCardPost
from kivymd.toast import toast



Builder.load_string("""
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDLabel kivymd.label.MDLabel
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton


<MenuScreen>:
    ScreenManager:
        id: scr_mngr
        transition: NoTransition()
        Screen:
            name: 'menu'
            spacing:10
            orientation: 'vertical'
            Screen:
                
                MDRaisedButton:
                    text: 'Добавить в список'
                    elevation_normal: 2
                    pos_hint: {'center_x':0.5,  'center_y': 0.60}
                    height:45
                    on_release: root.ids.scr_mngr.current = 'addfilm'
        
        
        
        
                MDRaisedButton:
                    height:45
                    text: 'Список'
                    elevation_normal: 2
                    pos_hint: {'center_x':0.5,  'center_y': 0.40}
                    on_release: root.go_spisok()

        Screen:
            name:'addfilm'
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: 'Добавить фильм'
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    elevation: 10 
                    left_action_items: [['arrow-left', lambda x: root.back_to_menu()]]  
                    
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(60)
                    Screen:
                        MDTextField:
                            pos_hint: {'center_x': .5, 'center_y': .9}
                            id: name_film
                            hint_text: 'Название фильма'
                        MDRoundFlatButton:
                            pos_hint: {'center_x': .5, 'center_y': .05}
                            text: 'Сохранить этот фильм'
                            on_release:root.save_film()
                            
        Screen:
            name:'spisok'
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(5)
            
                MDToolbar:
                    title:'Список'
                    id: toolbar
                    left_action_items: [['arrow-left', lambda x: root.back_to_menu()]]  
                    elevation: 10
                    md_bg_color: app.theme_cls.primary_color
            
            
                ScrollView:
                    id: scroll
                    size_hint: 1,1
                    do_scroll_x: False
            
                    GridLayout:
                        id: grid_card
                        cols: 1
                        spacing: dp(5)
                        padding: dp(5)
                        size_hint_y: None
                        height: self.minimum_height


""")

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        f = open('text.txt', 'r')
        c = f.read()
        f.close()
        if not (c == ''):
            c = c.split('\n')
            for i in range(len(c)-1):
                self.CreateCard(self, c[i])


        else:
            c = []






    global files
    files=[]
    def back_to_menu(self):
        self.ids.scr_mngr.current = "menu"


    def save_film(self):
        namefilm = self.ids.name_film.text
        if not (namefilm == '') and not (namefilm == ' '):
            self.ids.name_film.text=''
            self.ids.name_film.text_validate_unfocus=True
            self.CreateCard(self,namefilm)

            self.ids.scr_mngr.current="spisok"

    def go_spisok(self):
        self.ids.scr_mngr.current = "spisok"

    def DeleteCard(self,name):
        if (files.count(name)>=1):
            files.remove(name)
            f = open('text.txt', 'w')
            for i in files:
                f.write(i+'\n')
            f.close()

    def CreateCard(self,instance,namefilm):
        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                toast('Удален фильм: %s' % str(namefilm))
                self.ids.grid_card.remove_widget(Card)
                self.DeleteCard(namefilm)


        instance_grid_card = self.ids.grid_card
        global l
        Card=MDCardPost(
                path_to_avatar='film.png',
                name_data='Нужно посмотреть этот фильм: ', swipe=True,
                text_post=namefilm,
                callback=callback)
        instance_grid_card.add_widget(Card)



        global files
        files.append(namefilm)
        f = open('text.txt', 'w')
        for i in files:
            f.write(i + '\n')
        f.close()


    def upgrade_sp(list):
        print(list)





class YFilmApp(App):
    def __init__(self, **kw):
        super(YFilmApp, self).__init__(**kw)
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    md_app_bar = None

    def build(self):

        return Factory.MenuScreen()



if __name__ == "__main__":
	YFilmApp().run()