"""
Test get_edid helper
"""
from pyedid.helpers.edid_helper import EdidHelper
from . import data

class TestEdidHelper:
    """Test EdidHelper class"""

#    def test_hex_to_bytes(self):
#        """Test converting edid hex to byte string"""
#        assert EdidHelper.hex2bytes(data.BASE_HEX_EDID) == data.BASE_BYTE_EDID
#        assert EdidHelper.hex2bytes(data.EXTENTED_HEX_EDID) == data.EXTENTED_BYTE_EDID

    def test_interface_name(self):
        """Test parsing card number and interface name"""
        for i, interface_path in enumerate(data.INTERFACES_PATH):
            assert EdidHelper.get_interface_name(interface_path) == \
                    data.INTERFACES_NAME[i]
