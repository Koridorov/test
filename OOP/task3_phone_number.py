def phone_number_check(number: str) -> bool:
    return (
        len(number) == 13 and
        number.startswith("+359") and
        number[1:].isdigit()
    )

print(phone_number_check("+359876409357"))