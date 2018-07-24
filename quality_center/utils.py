"""qc utils module"""
from xml.etree import ElementTree
import json
from functools import wraps
import qc_exceptions


def ResetSession(func):
    """Ensures user is logged in"""

    @wraps(func)
    def inner(self, *args, **kwargs):
        """wrapped inner function"""
        try:
            return func(self, *args, **kwargs)
        except qc_exceptions.QCAuthenticationError:
            request = self.session.post(self.baseUrl + 'rest/is-authenticated')  # check if session is active
            if request.status_code == 401:
                self.Login()
            elif request.status_code == 503:
                raise qc_exceptions.QCError("Could not connect to Quality Center. {0}".format(request.reason))
            return func(self, *args, **kwargs)
    return inner


def DictToXml(data, dataType):
    """Convert a dictionary to a

    :param data: dictionary to be converted to XML
    :type data: dict
    :param dataType: type of data being converted. e.g. run, test-instance...
    :type dataType: str
    :return: string representation of xml data
    :rtype: str
    """
    root = ElementTree.Element('Entity', Type=dataType)
    child = ElementTree.SubElement(root, 'Fields')

    for name, value in data.iteritems():
        if value:
            field = ElementTree.SubElement(child, 'Field', Name=name)
            values = value if isinstance(value, list) else [value]  # support list of values
            for listVal in values:
                val = ElementTree.SubElement(field, 'Value')
                val.text = str(listVal)
    return ElementTree.tostring(root)


def DictToClass(classDict, classInstance):
    """
    Convert dict to class

    :param classDict: dict representing a class to convert to class
    :type classDict: dict
    :param classInstance: empty class instance to get the dict attributes
    :type classInstance: class
    :return: class
    """
    customNamesReversed = dict((v, k) for k, v in classInstance.customNames.iteritems())
    for name, value in classDict.iteritems():
        if value is not None:
            # add user-# fields with their real names to the class
            if name.startswith("user-") and hasattr(classInstance, customNamesReversed.get(name, name)):
                name = customNamesReversed.get(name, name)
            name = "".join([s if not i else s.title() for i, s in enumerate(name.split("-"))])
            if hasattr(classInstance, name):
                setattr(classInstance, name, value)
    return classInstance

def ConvertJsonToDict(content):
    """Convert qc json format to regular dict format for usability

    :param content: json content received from HTTP request
    :type content: dict or str
    :return: usable dict
    :rtype: dict
    """
    data = []
    if isinstance(content, basestring):
        content = json.loads(content)
    content = content['entities'] if 'entities' in content else [content]

    for obj in content:
        item = {}
        for field in obj['Fields']:
            if field['values'] and field['values'][0]:
                values = [val['value'] for val in field['values']]
                item[field['Name']] = values[0] if len(values) == 1 else values
            else:
                item[field['Name']] = None
        data.append(item)
    return data
