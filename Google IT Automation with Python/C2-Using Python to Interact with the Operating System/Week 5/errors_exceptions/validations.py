def validate_user(username, minlenght):
    assert type(username) == str, 'Username must be a string'
    if minlenght < 1:
        raise ValueError('Minum Lenght must be at least 1')
    if len(username) < minlenght:
        return False
    if not username.isalnum():
        return False
    return True