"""
Author: Arne Röskens
Date: 21.05.2024
"""
from PIL import Image
from pystray import Icon, Menu, MenuItem
from VolumeHandler import get_current_sessions
from Slider import Slider, Item
import IoHandler

class IconHandler:
    slider_list = []
    menu = []
    exit = None
    update = None
    running = False
    icon = None

    def init_icon(self, sliders: list, exit, update, name="AudinoMix"):
        self.slider_list = sliders
        self.exit = exit
        self.update = update
        image = Image.open("icon.png")
        self.menu = self.get_menu()
        self.running = True
        self.icon = Icon(name, image, name, menu = self.menu)
        return self.icon

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
        print("Toggled " + item.text + " at " + menu_item.text)
        IoHandler.save_sliders(self.slider_list)
    
    def does_slider_contain_item(self, slider: Slider, application_name: str, process_id: int) -> True:
        if not slider.slider_items:
            slider.slider_items = [Item(application='master', checked=False)]
            return False
        for i in range(len(slider.slider_items)):
            if slider.slider_items[i].application == application_name and slider.slider_items[i].process_id == process_id:
                return i
        return False
    
    def toggle_item_containing_in_slider(self, slider: Slider, application_text: str) -> True:
        name_id = remove_after_backslash(application_text)
        application_text = name_id[0]
        process_id = int(remove_brackets(name_id[1]))
        for slider_item in slider.slider_items:
            if slider_item.application == application_text and slider_item.process_id == process_id:
                slider_item.checked = not slider_item.checked

    def create_menu_for_slider(self, slider: Slider = None):
        sessions = get_current_sessions()
        slider_menu_items = []
        slider_menu_items.append(MenuItem('master\x08[0]', action=self.on_clicked, checked=lambda item: slider.slider_items[0].checked))
        for session in sessions:
            if session.Process:
                index = self.does_slider_contain_item(slider, session.Process.name(), session.ProcessId)
                if not index:
                    slider.slider_items.append(Item(application=session.Process.name(), checked=False, process_id=session.ProcessId))
                slider_menu_items.append(MenuItem(f"{session.Process.name()}\b[{session.ProcessId}]", self.on_clicked, checked=lambda item, i=index: slider.slider_items[i].checked))
        return Menu(*slider_menu_items)
    
    def stop(self):
        if self.running:
            self.icon.stop()
            self.running = False

    def update_menu(self, sliders: list):
        if self.icon is not None:
            self.slider_list = sliders
            self.menu = self.get_menu()
            self.icon.menu = self.menu
    

def remove_after_backslash(s):
    return s.split('\x08')

def remove_brackets(s):
    return s.replace('[', '').replace(']', '')

def get_clicked_menu_item(icon, item):
    for parent_item in icon.menu:
        if isinstance(parent_item, MenuItem):
            for submenu_item in parent_item.submenu.items:
                if submenu_item == item:
                    return parent_item

