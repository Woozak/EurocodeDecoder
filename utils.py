from re import fullmatch, IGNORECASE


def is_eurocode_correct(eurocode: str) -> bool:
    pattern = r'[0-9A-Z]{4}[ABCDEFHMLRT][A-Z]{2}[0-9A-Z]{,8}'
    result = fullmatch(pattern, eurocode, flags=IGNORECASE)
    return bool(result)

