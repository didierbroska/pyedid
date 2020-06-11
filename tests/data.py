"""
Test data
"""
from glob import glob
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

# from xrandr --verbose
BASE_HEX_EDID = ("00ffffffffffff000469982401010101"
                 "1e1b01031e351e78ea9265a655559f28"
                 "0d5054bfef00714f818081409500a940"
                 "b300d1c00101023a801871382d40582c"
                 "4500132b2100001e000000fd00324c1e"
                 "5311000a202020202020000000fc0056"
                 "533234380a20202020202020000000ff"
                 "0048374c4d51533132323136310a0000"
                )
BASE_BYTE_EDID = (b"\x00\xff\xff\xff\xff\xff\xff\x00"
                  b"\x04i\x98$\x01\x01\x01\x01\x1e\x1b"
                  b"\x01\x03\x1e5\x1ex\xea\x92e\xa6UU\x9f(\rPT"
                  b"\xbf\xef\x00qO\x81\x80\x81@\x95\x00\xa9@\xb3"
                  b"\x00\xd1\xc0\x01\x01\x02:\x80\x18q8-@X,E\x00"
                  b"\x13+!\x00\x00\x1e\x00\x00\x00\xfd\x002L\x1eS\x11\x00\n      "
                  b"\x00\x00\x00\xfc\x00VS248\n       \x00\x00\x00"
                  b"\xff\x00H7LMQS122161\n\x00\x00"
                 )

EXTENTED_HEX_EDID = ("00ffffffffffff000469982401010101"
                     "1e1b010380351e78ea9265a655559f28"
                     "0d5054bfef00714f818081409500a940"
                     "b300d1c00101023a801871382d40582c"
                     "4500132b2100001e000000fd00324c1e"
                     "5311000a202020202020000000fc0056"
                     "533234380a20202020202020000000ff"
                     "0048374c4d51533134373438350a018d"
                     "02031ef14b900504030201111213141f"
                     "230907078301000065030c0010001a36"
                     "80a070381e4030203500132b2100001a"
                     "662156aa51001e30468f3300132b2100"
                     "001e011d007251d01e206e285500132b"
                     "2100001e8c0ad08a20e02d10103e9600"
                     "132b21000018011d8018711c1620582c"
                     "2500132b2100009f0000000000000039"
                    )

EXTENTED_BYTE_EDID = (b"\x00\xff\xff\xff\xff\xff\xff\x00"
                      b"\x04i\x98$\x01\x01\x01\x01\x1e\x1b"
                      b"\x01\x03\x805\x1ex\xea\x92e\xa6UU"
                      b"\x9f(\rPT\xbf\xef\x00qO\x81\x80\x81@"
                      b"\x95\x00\xa9@\xb3\x00\xd1\xc0\x01\x01"
                      b"\x02:\x80\x18q8-@X,E\x00\x13+!\x00\x00"
                      b"\x1e\x00\x00\x00\xfd\x002L\x1eS\x11\x00\n      "
                      b"\x00\x00\x00\xfc\x00VS248\n       \x00\x00"
                      b"\x00\xff\x00H7LMQS147485\n\x01\x8d"
                     )

PNP_ID = "ACI"

COMPANY_NAME = "Ancor Communications Inc"

COMPANY_RAW = 1129

# from ls /sys/class/drm/*/edid
INTERFACES_PATH = (
    "/sys/class/drm/card0-DP-1/edid",
    "/sys/class/drm/card1-DP-2/edid",
    "/sys/class/drm/card0-HDMI-A-1/edid",
    "/sys/class/drm/card0-HDMI-B-2/edid",
    "/sys/class/drm/card0-eDP-1/edid"
)

INTERFACES_NAME = (
        (0, "DP-1"),        # 0
        (1, "DP-2"),        # 1
        (0, "HDMI-A-1"),    # 2
        (0, "HDMI-B-2"),    # 3
        (0, "eDP-1")        # 4
        )

BYTES_EDID_HDMI_A_1 = b'\x00\xff\xff\xff\xff\xff\xff\x00A\x0c\xbe\x08"\x0b\x00\x00$\x18\x01\x03\x80/\x1ex*x\xf1\xa6UH\x9b&\x12PT\xbdK\x00\xb3\x00\x95\x00\x95\x0f\x81\x80\x81\xc0\x01\x01\x01\x01\x01\x01|.\x90\xa0`\x1a\x1e@0 6\x00\xda(\x11\x00\x00\x1a\x00\x00\x00\xff\x00AU51436002850\x00\x00\x00\xfc\x00220S4L\n      \x00\x00\x00\xfd\x008L\x1eS\x11\x00\n      \x00\x92'

BYTES_EDID_eDP_1 = b'\x00\xff\xff\xff\xff\xff\xff\x00(\x89\x00\x00\x00\x00\x00\x00\x00\x1b\x01\x04\xa5\x1f\x11x\x03\x8d\xe0\xa5S5\xb8&\x0ePT\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xc0_\x00\xa0\xa0\xa0>P0 6\x005\xae\x10\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x00JDI          \x00\x00\x00\xfe\x00LPM140M420   \x00\xb7'

BYTES_EDID_HDMI_A_2 = b''
BYTES_EDID_DP_1 = b''
BYTES_EDID_DP_2 = b''

BYTES_EDIDS = (
        BYTES_EDID_DP_1,
        BYTES_EDID_DP_2,
        BYTES_EDID_HDMI_A_1,
        BYTES_EDID_HDMI_A_2,
        BYTES_EDID_eDP_1
        )

INTERFACES_NAME_EDID = (
        ((0, "HDMI-A-1"), BYTES_EDID_HDMI_A_1),
        ((0, "eDP-1"), BYTES_EDID_eDP_1)
        )

EDID_FILES = glob(BASE_DIR + "/data_files/*.edid")
EDID_FILES.sort()
