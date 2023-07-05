def age_converter(age) -> str:
    if age < 0:
        raise Exception
    if age >= 0 and age < 35:
        return 'young'
    elif age >= 35 and age < 50:
        return 'middle_aged'
    else:
        return 'old'
