"""
Error classes and other helpful functions
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

class Error(Exception):
    """Base class for exceptions"""
    pass


class AlmaError(Error):
    """
    Base Exception class for Alma API calls
    """

    def __init__(self, message, response=None, url=None):
        super(AlmaError, self).__init__(message)
        self.message = message
        self.response = response
        self.url = url


class ArgError(Error):
    def __init__(self, message):
        super(ArgError, self).__init__(message)
        self.message = 'Invalid Argument: ' + message

class Formatter():
    def clean_xml(xml_string):
        # Remove invalid characters
        xml_string = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', xml_string)
        xml_string = re.sub(r'[^\x00-\x7F]+', '', xml_string)
        # Ensure proper XML formatting
        try:
            root = ET.fromstring(xml_string)
            return ET.tostring(root, encoding='unicode')
        except ET.ParseError:
            # Handle malformed XML by fixing common issues
            xml_string = xml_string.replace('><', '>\n<')
            xml_string = re.sub(r'<([^>]+?)\/>', r'<\1></\1>', xml_string)
            return xml_string
