
# Add or remove device on a group
def get_device_modification_details():
    group_id = input('Enter ID group: ')
    op = input('Which operation (add/remove): ')
    if op == "2" or "rm":
        op = "remove"
    path = input("Path ('/components' = 1, '/devices' = 2 or '/groups' = 3):")
    if path == "1":
        path = "/components"
    elif path == "2":
        path = "/devices"
    else:
        path = "/groups"

    values = input("Values (id1,id2,..):").split(',') 
    return group_id, op, path, values

# Get groups by IDs
def get_groups_by_id():
    id = input("Groups IDs (1;2;3): ")
    return (id)

# For create a group
def set_group_details():
    label = input("Group name: ")
    description = input("Description (option): ")
    color = input("Color (option): ")
    comments = input("Comments (option): ")
    componentIds = input("Component ID (1;2;3..): ").split(';')
    criticalness = int(input("Criticalness (option): ") or 0)
    deviceIds = input("Device IDs: ").split(',')
    groupIds = input("Group IDs: ").split(',')
    locked = input("Is locked (Default true): ").lower() in ('true', 'yes', '1')
    parentId = input("Group parent ID (if exist): ")
    userProperties = input("User properties: ")

    return (label, description, color, comments, componentIds, criticalness, deviceIds, groupIds, locked, parentId, userProperties)


def get_devices_details():
    from_int = input("From int: ")
    to_int = input("To int: ")
    page = input("Page: ")
    size = input("Size: ")
    vulnerabilities = input("With vulnerabilities ? (Default false) ")
    return from_int, to_int, page, size, vulnerabilities


def get_device():
    id = input("Device ID: ")
    return id


def add_device_group_with_csv():
    group = input("Group ID: ")
    csv = input(f"Path to .csv file:")
    columnID = input("Column UUID Device (Default 0): ")
    return group, csv, columnID

def export_list():
    pass

def find_device():
    print("Enter one or more IP addresses (example : 192.168.1.1,192.168.1.2) ")
    input_ips = input("> ")
    ip_addresses = [ip.strip() for ip in input_ips.split(",")]
    return ip_addresses
