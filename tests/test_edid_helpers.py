"""
Test get_edid helper
"""
from python_edid.helpers.edid_helper import EdidHelper
from . import data


class TestEdidHelper:
    """Test EdidHelper class"""

    def test_interface_name(self):
        """Test parsing card number and interface name"""
        for i, interface_path in enumerate(data.INTERFACES_PATH):
            assert EdidHelper.get_interface_name(interface_path) == \
                    data.INTERFACES_NAME[i]

    def test_get_edid(self):
        """Test reading edid from raw."""
        for i, edid_path in enumerate(data.EDID_FILES):
            assert EdidHelper.get_edid(edid_path) == data.BYTES_EDIDS[i]

    def test_get_interface_edid(self, monkeypatch):
        """Test reading interface name bundled with edid."""
        monkeypatch.setattr(
                EdidHelper, "edids_path", data.EDID_FILES)

        assert EdidHelper.edids_path == data.EDID_FILES
        assert EdidHelper.get_interface_edid() == data.INTERFACES_NAME_EDID
