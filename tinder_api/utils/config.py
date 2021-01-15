from pathlib import Path
from typing import Dict


def _read_token_from_file(path=None) -> str:
    try:
        path = path or Path(__file__).parent.parent.parent / "token.txt"
        with open(path, "rt") as f:
            tinder_token = f.read()
        return tinder_token
    except FileNotFoundError:
        pass


tinder_token = _read_token_from_file()
host = 'https://api.gotinder.com'

def set_tinder_token(val:str) -> None:
    global tinder_token
    tinder_token = val


def headers() -> Dict[str, str]:
    if not tinder_token:
        raise ValueError("`tinder_token` is not yet assigned. Please call `set_tinder_token`.")

    return {
        'app_version': '6.9.4',
        'platform': 'ios',
        'content-type': 'application/json',
        'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
        'X-Auth-Token': tinder_token,
    }
