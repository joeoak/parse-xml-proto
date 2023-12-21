import xml.etree.ElementTree as ET

def parse_xml(file_name):
    # Parse XML file
    tree = ET.parse(file_name)

    # Get the root element
    root = tree.getroot()

    # Print all elements in the XML file
    for elem in root.iter():
        print(f'Element: {elem.tag}, Value: {elem.text}')

if __name__ == "__main__":
    parse_xml('file.xml')