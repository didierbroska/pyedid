"""
EDID helper
"""

#from subprocess import CalledProcessError, check_output
#from typing import ByteString, List
from glob import glob
import re

__all__ = ["EdidHelper"]


class EdidHelper:
    """Class for working with EDID data"""

#    @staticmethod
#    def hex2bytes(hex_data: str) -> ByteString:
#        """Convert hex EDID string to bytes
#
#        Args:
#            hex_data (str): hex edid string
#
#        Returns:
#            ByteString: edid byte string
#        """
#        # delete edid 1.3 additional block
#        if len(hex_data) > 256:
#            hex_data = hex_data[:256]
#
#        numbers = []
#        for i in range(0, len(hex_data), 2):
#            pair = hex_data[i:i+2]
#            numbers.append(int(pair, 16))
#        return bytes(numbers)

    @classmethod
    def get_interface_name(cls, path):
        """Get interface name where edid was reading.

        :path: string path where monitor is connected 

        :returns: Tupple(no card, interface named in sysfs drm)
        """
        _RE_NAME = (
                r"card(?P<ncard>[0-9]+)-"
                r"(?P<interface_name>[a-zA-Z]+\-[A|B]?\-?[0-9]+)"
            )
        name = re.search(_RE_NAME, path)

        return int(name.group("ncard")), name.group("interface_name")

    @classmethod
    def get_edids(cls):
        """Get edids from sysfs

        Returns:
            List[ByteString]: list with edids

        """
        edids_path = glob("/sys/class/drm/*/edid")

        edids = []
        for edid_path in edids_path:
            with open(edid_path, 'rb') as raw:
                edid = raw.read()
                if edid == b'':
                    continue
                edids.append(edid)

        return edids

#    @classmethod
#    def get_edids(cls) -> List[ByteString]:
#        """Get edids from xrandr
#
#        Raises:
#            `RuntimeError`: if error with retrieving xrandr util data
#
#        Returns:
#            List[ByteString]: list with edids
#        """
#        try:
#            output = check_output(["xrandr", "--verbose"])
#        except (CalledProcessError, FileNotFoundError) as err:
#            cls.
#            raise RuntimeError("Error retrieving xrandr util data: {}".format(err)) from None
#
#        edids = []
#        lines = output.splitlines()
#        for i, line in enumerate(lines):
#            line = line.decode().strip()
#            if line.startswith("EDID:"):
#                selection = lines[i+1:i+9]
#                selection = list(s.decode().strip() for s in selection)
#                selection = "".join(selection)
#                bytes_section = cls.hex2bytes(selection)
#                edids.append(bytes_section)
#        return edids
