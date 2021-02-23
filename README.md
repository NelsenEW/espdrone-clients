Forked from [crazyflie-clients-python (esp-drone branch)](https://github.com/leeebo/crazyflie-clients-python/tree/esp-drone)

The ESP-Drone PC client enables flashing and controlling the esp drone with crazyflie clients backend.
It implements the user interface and high-level control (for example gamepad handling).
The communication with espdrone and the implementation of the CRTP protocol to control the espdrone is handled by the [cflib](https://github.com/NelsenEW/espdrone-lib-python) project.

For more info see our [wiki](http://wiki.bitcraze.se/ "Bitcraze Wiki").

## Dependencies

The Crazyflie PC client has the following dependencies:

* Installed from system packages
  * Python 3.4+
  * PyQt5 == "5.13.2"
  * A pyusb backend: libusb 0.X/1.X
* Installed from PyPI using PIP:
  * cflib
  * PyUSB
  * PyQtGraph
  * ZMQ
  * appdirs
  * PyYAML

# Running from source

The espdrone client requires [cflib](https://github.com/NelsenEW/espdrone-lib-python).
If you want to develop with the lib too, follow the cflib readme to install it.

## Windows (7/8/10)

Running from source on Windows is tested using the official python build from [python.org](https://python.org). The client works with python version >= 3.5. The procedure is tested with 64bit python.

To run the client you should install python, make sure to check the "add to path" checkbox during install. You should also have git installed and in your path. Use git to clone the crazyflie client project.

Open a command line window and move to the espdrone clients folder (the exact command depends of where the project is cloned):
```
cd espdrone-clients-python
```

Install the client in development mode:
```
pip install -e .
```

You can now run the clients with the following commands:
```
cfclient
cfheadless
cfloader
cfzmq
```

## Mac OSX

### Using homebrew
**IMPORTANT NOTE**: The following will use
[Homebrew](http://brew.sh/) and its own Python distribution. If
you have a lot of other 3rd party python stuff already running on your system
they might or might not be affected by this.

1. Install homebrew

    See [the Homebrew site](https://brew.sh/)

1. Install the brew bottles needed
    ```
    brew install python3 sdl sdl2 sdl_image sdl_mixer sdl_ttf libusb portmidi
    ```

1. Install the client

    pip3 install -e .

1. You now have all the dependencies needed to run the client. The client can now be started from any location by:
    ```
    cfclient
    ```

## Linux

### Launching the GUI application

If you want to develop with the lib, install cflib from https://github.com/bitcraze/crazyflie-lib-python

Cfclient requires Python3, pip and pyqt5 to be installed using the system package manager. For example on Ubuntu/Debian:
```
sudo apt-get install python3 python3-pip python3-pyqt5 python3-pyqt5.qtsvg
```

Install cfclient to run it from source. From the source folder run (to install
for your user only you can add ```--user``` to the command):
```
pip3 install -e .
```
To launch the GUI application in the source folder type:
```python3 bin/cfclient```

To launch the GUI after a systemwide installation, execute ```cfclient```.
