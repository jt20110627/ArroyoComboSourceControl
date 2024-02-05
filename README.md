# ArroyoComboSourceControl
This is a modified arroyo library to control laser and TEC by slowly ramping between tec temperatures and laser currents to avoid shocking the lasers. It also contains necessary code to control rigol DG1032z function generator. Both will be used in combination. Use at your own risk.

This was developed in pycharm, with the following packages:

datetime
libusb
python-usbtmc
pyusb
pyserial

serial_interface.py needs to be added to ~/python/python312/lib/

To connect with the RIGOL function generators via python-usbtmc, it may be necessary to run the below tool to ensure the proper drivers for usbtmc are running.
https://sourceforge.net/projects/libusb-win32/files/libusb-win32-snapshots/20211113/libusb-win32-devel-filter-1.2.7.3.exe/download
