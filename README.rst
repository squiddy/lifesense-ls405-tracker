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

Services & Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

All definitions use the short UUID of BLE.

::

    Service 00001800
    
    Characteristic 00002a00 rw Device Name (defaults to "Max Buzz")
    Characteristic 00002a01 ro
    Characteristic 00002a04 ro
    
    Service 0000180a
    
    Characteristic 00002a23 ro System ID (?)
    Characteristic 00002a24 ro Model Number
    Characteristic 00002a25 ro Serial Number
    Characteristic 00002a26 ro Firmware Revision
    Characteristic 00002a27 ro Hardware Revision
    Characteristic 00002a29 ro Manufacturer name
    
    Service 0000fee7
    
    Characteristic 0000fec7
    Characteristic 0000fec8
    Characteristic 0000fec9 ro Returns the Mac Address.
    
    Service 0000fcc0
    
    Characteristic 0000fcc6
    Characteristic 0000fcc7
    Characteristic 0000fcc8 ro Returns the Mac Address, a null byte and two
                               additional bytes that aren't constant.
    
    Service 0000a500
    
    Characteristic 0000a501
    Characteristic 0000a502
    Characteristic 0000a503
    
    Service 0000a520
    
    Characteristic 0000a523 ro Returns the same two bytes as 0000fcc8 at the end.

Development
-----------

I'm working with linux, but tools like ``gatttool`` consistently failed to
connect to the device, so I couldn't get any information about services &
attributes.
So right now I'm handcrafting bluetooth packets according to bluetooth packet
logs from my android phone.

**DISCLAIMER - USE AT YOUR OWN RISK**