from rest_framework.serializers import ValidationError
import string


class PasswordValidator:
    def __call__(self, password):
        result = []
        errors = {
            'long': {
                'found': False,
                'string': 'Your password is too long.'
            },
            'short': {
                'found': False,
                'string': 'Your password is too short.'
            },
            'no_upper': {
                'found': True,
                'string': 'Your password must have at least 1 uppercase letter.'
            },
            'no_lower': {
                'found': True,
                'string': 'Your password must have at least 1 lowercase letter.'
            },
            'no_digit': {
                'found': True,
                'string': 'Your password must have at least 1 digit.'
            },
            'no_special': {
                'found': True,
                'string': 'Your password must have at least 1 special character.'
            },
            'space': {
                'found': False,
                'string': "Your password must not have any spaces."
            }
        }

        for letter in password:
            if letter in string.ascii_uppercase:
                errors['no_upper']['found'] = False
            elif letter in string.ascii_lowercase:
                errors['no_lower']['found'] = False
            elif letter.isdigit():
                errors['no_digit']['found'] = False
            elif letter.isspace():
                errors['space']['found'] = True
            else:
                errors['no_special']['found'] = False

        if len(password) < 8:
            errors['short']['found'] = True
        elif len(password) > 20:
            errors['long']['found'] = True

        for error in errors.values():
            if error['found']:
                result.append(error['string'])

        if len(result):
            raise ValidationError('.'.join(result))
