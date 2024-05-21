import pickle
from Slider import Slider, SliderType

def load_saved_sliders(num_sliders: int) -> list:
    loaded_sliders = []
    with open('sliders.pkl', 'rb') as f:
        while len(loaded_sliders) < num_sliders:
            try:
                loaded_sliders.append(pickle.load(f))
            except EOFError:
                break
    while len(loaded_sliders) < num_sliders:
        loaded_sliders.append(Slider())
    return loaded_sliders

def save_sliders(sliders: list):
    with open('sliders.pkl', 'wb') as f:
        for slider in sliders:
            pickle.dump(slider, f)
