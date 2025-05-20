import xml.etree.ElementTree as ET

xml_data = """
<user>
    <person>
        <id>1</id>
        <first_name>John</first_name>
        <last_name>Doe</last_name>
        <age>30</age>
        <address>
            <street>Main Street 1</street>
            <city>New_York</city>
            <zip>1001</zip>
        </address>
    </person>
</user>
"""

root = ET.fromstring(xml_data.strip())
print(f"user ID:", (root.find('person/id').text))
print(f"'first_name':{(root.find('person/first_name').text)}")
print(f"'adress_street':{(root.find('person/address/street').text)}")



