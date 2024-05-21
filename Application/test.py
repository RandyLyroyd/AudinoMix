from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

state = False

def on_clicked(icon, item):
    global state
    state = not item.checked

icon('test', Image.open("icon.png"), menu=menu(
    item(
        'Checkable',
        on_clicked,
        checked=lambda item: state))).run()