#AudinoMix

AudinoMix is a versatile and user-friendly project that allows you to control the audio of individual applications on your computer using potentiometers connected to an Arduino Nano. Whether you want to adjust the volume of a specific app or fine-tune the master volume, AudinoMix gives you the tactile control you need.
##Features

    Control Application Volumes: Adjust the volume of individual applications using potentiometers.
    Customizable Potentiometers: Connect as many potentiometers to the Arduino as you need.
    Master Volume Control: Use a potentiometer to control the overall system volume.
    Tray Icon for Easy Configuration: Quickly assign which application each potentiometer controls via a tray icon interface.
    Future Enhancements: Plans to add buttons for muting the microphone or application audio, and more.

##Hardware Requirements

    Arduino Nano (or any Arduino compatible with COM port communication)
    Linear Potentiometers for precise volume control
    Connecting Wires to link potentiometers to the Arduino

##Software Requirements

    Python must be installed on your system.

##Installation and Setup

    Arduino Setup:
        Upload the provided script to your Arduino. This script will handle sending potentiometer values over the COM port to your computer.
    Python Script:
        Clone this repository to your local machine.
        Ensure Python is installed.
        Run the main Python script to start the application.

##How It Works

    Connecting Potentiometers:
        Refer to the included schematic for connecting potentiometers to your Arduino Nano.

    Running the Application:
        Start the main Python script. The application will initialize and communicate with the Arduino via the COM port.
        Use the tray icon to assign specific applications to each potentiometer. This allows you to quickly and easily decide which application's volume each potentiometer will control.

    Adjusting Volumes:
        Turn the potentiometers to adjust the volume of the assigned applications in real-time.

##Screenshots

    Tray Icon and Functions:

    Connection Schematic:

##Future Plans

    Add Button Support: Integrate buttons for muting the microphone or application audio.
    Multi-Application Control: Allow a single potentiometer to control multiple applications.

## Contributing

Contributions to AudinoMix are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
