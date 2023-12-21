import os
import xml.etree.ElementTree as ET

def parse_xml(file_name, tag_name):
    # Parse XML file
    tree = ET.parse(file_name)

    # Get the root element
    root = tree.getroot()

    # Print all elements in the XML file
    for elem in root.iter():
        tag = elem.tag.split('}')[-1]  # This will remove the namespace
        if tag == tag_name:
            print(f'- {tag}: {elem.text}')

def parse_all_xml(directory, tag_name):
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            print(f'{filename}')
            parse_xml(os.path.join(directory, filename), tag_name)

if __name__ == "__main__":
    parse_all_xml('data', 'TotalTaxAmt')
