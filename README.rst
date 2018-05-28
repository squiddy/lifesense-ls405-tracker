lifesense-ls405-tracker aka "Max Buzz"
======================================

An attempt to write an interface to the fitness tracker "Max Buzz" that I was
given as part of the Virgin Pulse Global Challenge.

This is just for fun, to see how far I can get and to learn something along
the way.

Device (WIP)
------------

The "Max Buzz" is a BLE (Bluetooth Low Energy) device and is compatible with
the Generic Attribute Profile (GATT). Therefore some information is easy to
retrieve by using one of the various Bluetooth explorer tools (I've had good
success with the LightBlue® Explorer app for Android).

* Manufacturer **lifesense**
* Model Number **LS-405**
* Hardware Revision **B202**
* Firmware Revision **V031**

Development
-----------

I'm working with linux, but tools like ``gatttool`` consistently failed to
connect to the device, so I couldn't get any information about services &
attributes.
So right now I'm handcrafting bluetooth packets according to bluetooth packet
logs from my android phone.

**DISCLAIMER - USE AT YOUR OWN RISK**