from Slider import Slider, SliderType, Item
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
master_volume = cast(interface, POINTER(IAudioEndpointVolume))

def set_volume(value: float, slider: Slider):
    if not has_value_changed(slider.value, value, 1.0): 
        return
    slider.value = value
    volume = value / 1023
    if slider.slider_items[0].checked:
        master_volume.SetMasterVolumeLevelScalar(volume, None)
    sessions = get_current_sessions()
    for session in sessions:
        for item in slider.slider_items:
            if session.Process and item.checked and session.Process.name() == item.application:
                application_volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                application_volume.SetMasterVolume(volume, None)

def has_value_changed(old_value: float, new_value: float, range: float = 0.0) -> bool:
    difference = abs(old_value - new_value)
    return difference > range

def get_current_sessions() -> list:
    return AudioUtilities.GetAllSessions()