from django.core.exceptions import ValidationError


def validate_audio(value):
    value = str(value)
    ok = False
    ok |= value.endswith('.wav')
    ok |= value.endswith('.mp3')

    if not ok:
        raise ValidationError('only .wav/.mp3 files allowed')
    else:
        return value
