import arabic_reshaper
import pyperclip


def reshape(text):
    new_text = ''
    buffer = ''
    for char in text:
        if '0' <= char <= '9' or 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '۰' <= char <= '۹' or char == ' ':
            buffer += char
        else:
            if buffer:
                new_text += buffer[::-1]
                buffer = ''
            new_text += char
    if buffer:
        new_text += buffer[::-1]
    rs_text = arabic_reshaper.reshape(new_text)[::-1]
    pyperclip.copy(rs_text)
