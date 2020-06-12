"""
Entrypoint
"""

from python_edid.edid import Edid
from python_edid.helpers.edid_helper import EdidHelper
from python_edid.helpers.registry import Registry


def main():
    """Main func"""
    print("Loading registry from web...")
    registry = Registry.from_web()
    print("Done!\n")

    for raw in EdidHelper.get_edids():
        edid = Edid(raw, registry)
        print(edid)


if __name__ == "__main__":
    main()
