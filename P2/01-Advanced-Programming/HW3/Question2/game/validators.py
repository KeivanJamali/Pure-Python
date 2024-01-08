from django.core.exceptions import ValidationError
import string


def validate_username(value):
    if type(value) == str:
        if len(value) < 5 or len(value) > 20:
            raise ValidationError("invalid username")
        n = False
        for char in value:
            if char not in string.ascii_letters and char not in string.digits and char not in "_":
                raise ValidationError("invalid username")
            if char.isalpha():
                n = True

        if not n:
            raise ValidationError("invalid username")

        return
    raise ValidationError("invalid username")


def validate_password(value):
    if type(value) != str:
        raise ValidationError("invalid password")
    if len(value) < 8 or len(value) > 50:
        raise ValidationError("invalid password")
    for char in value:
        if char in string.whitespace:
            raise ValidationError("invalid password")
    if sum(int(char) for char in value if char.isdigit()) % 6 == 0:
        raise ValidationError("invalid password")


def validate_score(value):
    if value < 0 or value >= 1000000000:
        raise ValidationError("invalid score")


def validate_age(value):
    if value < 18:
        raise ValidationError("invalid age")
