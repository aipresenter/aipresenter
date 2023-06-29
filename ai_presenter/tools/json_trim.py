

def json_trim(input_string: str) -> str:
    input_string = input_string.strip()
    begin = input_string.find('{')
    if begin == -1:
        return '{}'
    end = input_string.rfind('}')
    if end == -1:
        return '{}'

    return input_string[begin:end+1]
