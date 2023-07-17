def age_converter(age: int) -> str:
    if not isinstance(age, int):
        raise Exception("Age must be a numerical value")
    if age < 0:
        raise Exception("Age must be greater than or equal to 0")
    if age >= 0 and age < 35:
        return 'young'
    elif age >= 35 and age < 50:
        return 'middle_aged'
    else:
        return 'old'
