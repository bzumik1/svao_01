import functools

__TABLE = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z")


def encode(message, key):
    """Encodes message with Cesar cipher so that every letter in message is exchanged with one which is before of after
    it in alphabet based on key. Key has to be between -1000 and 1000. All letters are converted to small letters before
    encoding."""
    return __process(message, key)


def decode(message, key):
    """Decodes message with Cesar cipher so that every letter in message is exchanged with one which is before of after
    it in alphabet based on key. Key has to be between -1000 and 1000. All letters are converted to small letters before
    decoding."""
    return __process(message, -key)


def __process(message, key):
    __validate_key(key)
    __validate_message(message)
    return "".join(
        [index_or_letter if (type(index_or_letter) is str) else __TABLE[(index_or_letter + key) % len(__TABLE)]
            for index_or_letter in
                [__TABLE.index(letter) if letter in __TABLE else letter for letter in message.lower()]]
    )


def __validate_key(key):
    if type(key) is not int:
        raise TypeError("key can be only integer")
    if not (-1000 <= key <= 1000):
        raise ValueError("key should be in between -1000 and 1000")


def __validate_message(message):
    if type(message) is not str:
        raise TypeError("message has to be string")
