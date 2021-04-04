from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.cards import MDCardPost
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string("""
#:import MDToolbar kivymd.toolbar.MDToolbar


<ExampleCardPost@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color


    ScrollView:
        id: scroll
        size_hint: 1, 1
        do_scroll_x: False

        GridLayout:
            id: grid_card
            cols: 1
            spacing: dp(5)
            padding: dp(5)
            size_hint_y: None
            height: self.minimum_height
            Button:
                text:'frf'
                on_press: app.CreateCard()
                height:100
""")



class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    cards_created = False
    global p
    p=[]
    def CreateCard(self):

        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                print(str(instance), str(value))
                instance_grid_card.remove_widget(MDCardPost())
                toast('Delete post %s' % str(instance))
        instance_grid_card = self.screen.ids.grid_card
        instance_grid_card.add_widget(
            MDCardPost(
                path_to_avatar='film.png',
                name_data=' ', swipe=True,
                text_post='Card with a button to open the menu MDDropDown',
                callback=callback, id='1', likes_stars=True))

        print('llllllll')
        global p,f

        l='Card with a button to open the menu MDDropDown'
        p.append(l)
        f = open('text.txt', 'w')
        for i in p:
            f.write(i + '\n')

        f.close()




    def build(self):
        self.screen = Factory.ExampleCardPost()
        return self.screen

    def on_start(self):
        def callback_for_menu_items(text_item):
            toast(text_item)

        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                print(str(instance), str(value))
                instance_grid_card.remove_widget(MDCardPost())
                toast('Delete post %s' % str(instance))

        instance_grid_card = self.screen.ids.grid_card
        buttons = ['facebook', 'vk', 'twitter']
        menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': callback_for_menu_items}
            for i in range(2)
        ]

        if not self.cards_created:
            self.cards_created = True
            global f
            f = open('text.txt', 'r')

            global c
            c = f.read()
            if not (c == ''):
                c=c.split('\n')
                print(c)
                f.close()
                for i in range(len(c)-1):
                    self.CreateCard()
            else:
                c=[]





Example().run()