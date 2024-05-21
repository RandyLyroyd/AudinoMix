"""
Author: Arne Röskens
Date: 21.05.2024
"""
from enum import Enum

class SliderType(Enum):
    Application = 1
    Master = 2

class Slider:
    def __init__(self, value: int = -1, slider_items: list = None) -> None:
        self.value = value
        self.slider_items = slider_items
    value: int
    slider_items: list

class Item:
    def __init__(self, application, checked):
        self.application = application
        self.checked = checked
    application: str
    checked: bool = False