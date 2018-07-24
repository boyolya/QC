"""
author: tehilad
"""


class QCError(Exception):
    """Represents exceptions raised by the Quality Center API"""
    def __init__(self, message):
        Exception.__init__(self, message)

class QCAuthenticationError(Exception):
    """Represents authentication error raised by the Quality Center API"""
    def __init__(self, message):
        Exception.__init__(self, message)
