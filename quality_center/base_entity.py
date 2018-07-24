"""base entity"""
from xml.etree import ElementTree
import re


class BaseEntity(object):
    """BaseEntity class"""

    def __init__(self):
        """ init for BaseEntity

        :Parameters: none
        :return: self
        """
        self.customNames = {}  # store map of custom names to meaningful names

    def ToXml(self):
        """Convert object to xml

        :Parameters: none
        :return: xml representation of object
        :rtype: str
        """
        root = ElementTree.Element('Entity', Type=re.sub('([a-z])([A-Z0-9])', r'\1-\2', type(self).__name__).lower())
        child = ElementTree.SubElement(root, 'Fields')

        for name, value in self.__dict__.iteritems():
            if name == 'customNames':  # Dont export this to xml
                continue
            if value is not None:
                if name in self.customNames:  # replace custom name
                    name = self.customNames[name]
                name = re.sub('([a-z])([A-Z0-9])', r'\1-\2', name).lower()  # convert from variableName to variable-name
                field = ElementTree.SubElement(child, 'Field', Name=name)
                values = value if isinstance(value, list) else [value]
                for listVal in values:
                    val = ElementTree.SubElement(field, 'Value')
                    val.text = str(listVal)
        return ElementTree.tostring(root)


if __name__ == "__main__":
    b = BaseEntity()
    b.name = 'Test Name'  # pylint: disable=attribute-defined-outside-init
    b.age = 15  # pylint: disable=attribute-defined-outside-init
    b.nums = [1, 2, 3, 4, 5]  # pylint: disable=attribute-defined-outside-init
    print b.ToXml()
