import re


class SignupValidator():
    USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    PASS_RE = re.compile(r'^.{3,20}$')
    EMAIL_RE = re.compile(r'^[\S]+@[\S]+.[\S]+$')
