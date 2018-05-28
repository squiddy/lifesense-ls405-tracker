from scapy.config import conf
from scapy.layers import bluetooth
from scapy.packet import Raw, RawVal
from scapy.utils import hexdump, raw


class Tracker:

    def __init__(self, debug=False):
        self.debug = debug
        self.socket = bluetooth.BluetoothUserSocket()
        self.connection_handle = None

    def _send(self, p):
        self.socket.send(p)
        if self.debug:
            print("Sending ...")
            hexdump(p)
            print()

    def connect(self, hwaddr):
        p = (
            bluetooth.HCI_Hdr()
            / bluetooth.HCI_Command_Hdr(opcode=0x200d)
            / bluetooth.HCI_Cmd_LE_Create_Connection(
                interval=96,
                window=48,
                filter=0,
                patype=1,
                paddr=hwaddr,
                atype=1,
                min_interval=24,
                max_interval=40,
                latency=0,
                timeout=500,
                min_ce=0,
                max_ce=0,
            )
        )
        self._send(p)
        while True:
            p = self.socket.recv()
            if self.debug:
                hexdump(p)

            if p.type == 4:
                if p.code == 0x3e and p.event == 1 and p.status == 0:
                    if self.debug:
                        print(f"Connected with handle {p.handle}")
                    self.connection_handle = p.handle
                    return

    def disconnect(self):
        p = (
            bluetooth.HCI_Hdr()
            / bluetooth.HCI_Command_Hdr(opcode=0x0406)
            / bluetooth.HCI_Cmd_Disconnect(handle=self.connection_handle)
        )
        self._send(p)
        while True:
            p = self.socket.recv()
            if p.type == 4:
                if p.code == 0x5:
                    return

    def read_attribute(self, gatt_handle):
        p = (
            bluetooth.HCI_Hdr(type=2)
            / bluetooth.HCI_ACL_Hdr(handle=self.connection_handle)
            / bluetooth.L2CAP_Hdr(cid=4)
            / bluetooth.ATT_Hdr()
            / bluetooth.ATT_Read_Request(gatt_handle=gatt_handle)
        )
        self._send(p)
        while True:
            p = self.socket.recv()
            if p.type == 2 and p.opcode == 0xb:
                return p.value


try:
    tracker = Tracker()
    tracker.connect("CD:0B:5E:7C:2E:2A")
    # manufacturer name
    hexdump(tracker.read_attribute(0x0024))
    # ???
    hexdump(tracker.read_attribute(0x0031))
    # macaddress and two additional bytes (same as 0x0031)
    hexdump(tracker.read_attribute(0x0018))
    # ???
    hexdump(tracker.read_attribute(0x0030))
    # ???
    hexdump(tracker.read_attribute(0x0017))
finally:
    tracker.disconnect()
