outline = "[Dev] v6.0-20250427.1"
number = "6.0"
build_number = "20250427.1"
channel = "Dev"
programming_language = "Python"
def version_outline():
    return outline
def version_detail():
    return number, build_number, channel, programming_language
def version_channel():
    return channel
def version_programming_language():
    return programming_language