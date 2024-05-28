"""
Author: Arne Röskens
Date: 28.05.2024
"""
import signal
import serial
import keyboard
import VolumeHandler
import threading
from IconHandler import IconHandler
import IoHandler

class Main:
    num_sliders = 2
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )

    started = False
    sliders = []

    icon_thread: threading.Thread

    icon_handler = IconHandler()

    running = True

    icon = None

    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def signal_handler(self, signal_received, frame):
        self.exit()

    def exit(self):
        self.running = False
        self.icon_handler.stop()

    def refresh_tray(self):
        print("\t-- Refreshing... --")
        self.sliders = IoHandler.load_saved_sliders(num_sliders=self.num_sliders)
        self.icon_handler.update_menu(sliders=self.sliders)
        print("\t-- Refreshed AudinoMix --")

    def button_pressed(self):
        keyboard.press('ctrl')
        keyboard.press('shift')
        keyboard.press('m')
        keyboard.release('m')
        keyboard.release('shift')
        keyboard.release('ctrl')

    def start_application(self):
        self.sliders = IoHandler.load_saved_sliders(num_sliders=self.num_sliders)
        self.icon = self.icon_handler.init_icon(sliders=self.sliders, exit=self.exit, update=self.refresh_tray)
        self.icon_thread = threading.Thread(target=self.icon.run)
        self.icon_thread.start()
        self.started = True
        print("\t-- Started AudinoMix --")

    def start(self):
        while self.running:
            try:
                line = self.ser.readline()
                decoded = line.decode('utf-8')
                data = decoded.strip()
                if data == 'Button':
                    self.button_pressed()
                    continue
                values = data.split('|')
                
                if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
                    return

                if not self.started:
                    self.start_application()
                    continue
                
                for i in range(len(self.sliders)):
                    if values[i] == '':
                        continue
                    VolumeHandler.set_volume(float(values[i]), self.sliders[i])
                    
            except KeyboardInterrupt:
                break
            except serial.SerialException as e:
                print(f"Serial error: {e}")
                break
            except Exception as e:
                print(f"Error: {e}")
                break
        self.ser.close()

main = Main()
main.start()