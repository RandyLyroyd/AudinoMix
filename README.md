# AudinoMix

AudinoMix is a versatile and user-friendly project that allows you to control the audio of individual applications on your computer using potentiometers connected to an Arduino Nano. Whether you want to adjust the volume of your favorite music app, mute your microphone, or fine-tune the master volume, AudinoMix gives you the tactile control you need.

## Features

- **Control Application Volumes**: Adjust the volume of individual applications using potentiometers.
- **Customizable Potentiometers**: Connect as many potentiometers to the Arduino as you need.
- **Master Volume Control**: Use a potentiometer to control the overall system volume.
- **Tray Icon for Easy Configuration**: Quickly assign which application each potentiometer controls via a tray icon interface.
- **Future Enhancements**: Plans to add buttons for muting the microphone or application audio, and more.

## Hardware Requirements

- Arduino Nano (or any Arduino compatible with COM port communication)
- Linear Potentiometers for precise volume control
- Connecting Wires to link potentiometers to the Arduino

## Software Requirements

- Python must be installed on your system.

## Installation and Setup

1. **Arduino Setup**:
   - Upload the provided script to your Arduino. This script will handle sending potentiometer values over the COM port to your computer.
   
2. **Python Script**:
   - Clone this repository to your local machine.
   - Ensure Python is installed.
   ```bash
   python
   ```
   - Also ensure that you have serial, comtypes, pycaw, pystray and pyserial installed.
   ```
   pip install serial comtypes pycaw pystray pyserial
   ```
   - Ensure that you are in the right directory:
     ```bash
     cd .\Application\
     ```
   - Run the main Python script to start the application.
     ```bash
     python main.py
     ```

## How It Works

1. **Connecting Potentiometers**:
   - Refer to the included schematic for connecting potentiometers to your Arduino Nano.

2. **Running the Application**:
   - Start the main Python script. The application will initialize and communicate with the Arduino via the COM port.
   - Use the tray icon to assign specific applications to each potentiometer. This allows you to quickly and easily decide which application's volume each potentiometer will control.

3. **Adjusting Volumes**:
   - Turn the potentiometers to adjust the volume of the assigned applications in real-time.

## Screenshots

- **Tray Icon and Functions**:
   ![TrayIcon](https://github.com/RandyLyroyd/AudinoMix/assets/51125549/605f57e8-ac22-435b-b555-f9f151fc5698)

- **Connection Schematic**:
  TODO: Add schematic

## Future Plans

- **Add Button Support**: Integrate buttons for muting the microphone or application audio.

## Contributing

We welcome contributions to AudinoMix! Please follow these guidelines:

1. **Fork the repository**: Create your own fork of the repository.
2. **Create a new branch**: Use `git checkout -b feature-name` to create a new branch for your feature or bugfix.
3. **Commit your changes**: Make sure your changes are well-documented and clean.
4. **Push to your branch**: Use `git push origin feature-name`.
5. **Create a Pull Request**: Go to the original repository and create a pull request. Provide a clear description of your changes and why they are necessary.

All contributions must be made via pull requests. Direct commits to the `main` branch are not allowed.

## License

This project is licensed under the MIT License - see the LICENCE file for more details.
