from PIL import Image
from pystray import Icon, Menu, MenuItem
from VolumeHandler import get_current_sessions
from Slider import Slider, SliderType, Item
import IoHandler

class IconHandler:
    slider_list = []
    menu = []
    exit = None
    update = None
    def init_icon(self, sliders: list, exit, update):
        self.slider_list = sliders
        self.exit = exit
        self.update = update
        image = Image.open("icon.png")
        self.menu = self.get_menu()
        return Icon("Icon", image, "VolumeControl", menu = self.menu)

    def get_menu(self):
        menu = []
        for i in range(len(self.slider_list)):
            menu_item = MenuItem('Slider ' + str(i), self.create_menu_for_slider(self.slider_list[i]))
            menu.append(menu_item)
        menu.append(MenuItem('Refresh', self.update))
        menu.append(MenuItem('Exit', self.exit))
        return menu

    def get_slider_by_name(self, name) -> Slider:
        index = int(name[len(name) - 1])
        return self.slider_list[index]
    
    def on_clicked(self, icon, item):
        menu_item = get_clicked_menu_item(icon, item)
        if not menu_item:
            return
        slider: Slider = self.get_slider_by_name(menu_item.text)
        self.toggle_item_containing_in_slider(slider, item.text)
        IoHandler.save_sliders(self.slider_list)
    
    def does_slider_contain_item(self, slider: Slider, application_name: str) -> True:
        if not slider.slider_items:
            slider.slider_items = [Item(application='master', checked=False)]
            return False
        for i in range(len(slider.slider_items)):
            if slider.slider_items[i].application == application_name:
                return i
        return False
    
    def toggle_item_containing_in_slider(self, slider: Slider, application_name: str) -> True:
        for slider_item in slider.slider_items:
            if slider_item.application == application_name:
                slider_item.checked = not slider_item.checked

    def create_menu_for_slider(self, slider: Slider = None):
        sessions = get_current_sessions()
        slider_menu_items = []
        slider_menu_items.append(MenuItem('master', action=self.on_clicked, checked=lambda item: slider.slider_items[0].checked))
        for session in sessions:
            if session.Process:
                index = self.does_slider_contain_item(slider, session.Process.name())
                if not index:
                    slider.slider_items.append(Item(application=session.Process.name(), checked=False))
                slider_menu_items.append(MenuItem(session.Process.name(), self.on_clicked, checked=lambda item, i=index: slider.slider_items[i].checked))
        return Menu(*slider_menu_items)
    



def get_clicked_menu_item(icon, item):
    for parent_item in icon.menu:
        if isinstance(parent_item, MenuItem):
            for submenu_item in parent_item.submenu.items:
                if submenu_item == item:
                    return parent_item

