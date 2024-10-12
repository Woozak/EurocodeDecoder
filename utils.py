import exceptions
from glass_schemas import Windshield, RearWindow, SideWindow


def get_glass_info(eurocode: str) -> dict:
    if eurocode[4] in 'ACD':
        glass = Windshield(eurocode)
    elif eurocode[4] in 'BE':
        glass = RearWindow(eurocode)
    elif eurocode[4] in 'FHLMRT':
        glass = SideWindow(eurocode)
    else:
        raise exceptions.InvalidEurocodeError
    glass_info = glass.__dict__
    del glass_info['data']
    return glass_info
