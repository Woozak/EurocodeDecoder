from re import fullmatch, IGNORECASE

import exceptions


def is_eurocode_correct(eurocode: str) -> bool:
    pattern = r'[0-9A-Z]{4}[ABCDEFHMLRT][A-Z]{2}[0-9A-Z]{,8}'
    result = fullmatch(pattern, eurocode, flags=IGNORECASE)
    return bool(result)


def decode_eurocode(eurocode: str):
    if not is_eurocode_correct(eurocode):
        raise exceptions.InvalidEurocodeError
