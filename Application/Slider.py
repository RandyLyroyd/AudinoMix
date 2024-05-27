"""
Author: Arne Röskens
Date: 27.05.2024
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
    def __init__(self, application, checked, identifier="", process_id=0):
        self.application = application
        self.checked = checked
        self.process_id = process_id
        self.identifier = identifier
    application: str
    process_id: int
    identifier: str
    checked: bool = False