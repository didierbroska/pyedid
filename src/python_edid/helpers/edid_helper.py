"""
EDID helper
"""

from glob import glob
import re

__all__ = ["EdidHelper"]


class EdidHelper:
    """Class for working with EDID data"""

    edids_path = glob("/sys/class/drm/*/edid")

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
    def get_edid(cls, path):
        """Get edid from sysfs
        an EDID.

        Returns:
            ByteString: edid in raw bytestring
        """

        with open(path, "rb") as raw:
            edid = raw.read()

        return edid

    @classmethod
    def get_interface_edid(cls):
        """Get interface name bundled with edid
        :returns: Tuple[Various]((no card, inter name), edid)

        """
        edids = []
        for edid_path in cls.edids_path:
            intname = cls.get_interface_name(edid_path)
            edid = cls.get_edid(edid_path)
            # skip edid void
            if edid == b"":
                continue
            edids.append((intname, edid))

        return tuple(edids)
