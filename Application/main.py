"""
Author: Arne Röskens
Date: 21.05.2024
"""
import serial
import VolumeHandler
import threading
from IconHandler import IconHandler
import IoHandler

class Main:
    num_sliders = 5
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

    def exit(self):
        self.running = False
        self.icon_handler.stop()

    def refresh_tray(self):
        print("\t-- Refreshing... --")
        self.sliders = IoHandler.load_saved_sliders(num_sliders=self.num_sliders)
        self.icon_handler.update_menu(sliders=self.sliders)
        print("\t-- Refreshed AudinoMix --")

    def start(self):
        while self.running:
            try:
                line = self.ser.readline()
                decoded = line.decode('utf-8')
                data = decoded.strip()
                values = data.split('|')
                
                if not self.started:
                    self.sliders = IoHandler.load_saved_sliders(num_sliders=self.num_sliders)
                    self.icon = self.icon_handler.init_icon(sliders=self.sliders, exit=self.exit, update=self.refresh_tray)
                    self.icon_thread = threading.Thread(target=self.icon.run)
                    self.icon_thread.start()
                    self.started = True
                    print("\t-- Started AudinoMix --")
                    continue
                
                for i in range(len(self.sliders)):
                    if values[i] == '':
                        continue
                    VolumeHandler.set_volume(float(values[i]), self.sliders[i])
                    
            except KeyboardInterrupt:
                break
        self.ser.close()

main = Main()
main.start()