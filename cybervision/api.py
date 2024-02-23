import csv
import json
import requests
from .auth import get_headers
from .config import BASE_URL

# https://www.postman.com/ciscodevnet/workspace/cisco-devnet-s-public-workspace/collection/3224967-f145f298-a3d1-4d99-80ea-6f2330758830

def add_device_on_group(group_id, op, path, values):
    """
    Add or remove device on a group
    
    :param group_id: Group ID
    :param op: op for Operation (Can be 'add' or'remove').
    :param path: Can be '/components', '/devices' or '/groups'
    :param values: Many component ids are allowed
    """
    url = f"{BASE_URL}/groups/{group_id}"
    data = json.dumps([
        {
            "op": op,
            "path": path,
            "value": values
        }
    ])
    headers = get_headers()
    response = requests.patch(url, json=data, headers=headers)
    return response


def create_group(label, description="", color="string", comments="string", componentIds=None, criticalness=0, deviceIds=None, groupIds=None, locked=True, parentId="string", userProperties=None):
    """Create a group with detailed parameters."""
    url = f"{BASE_URL}/groups"
    data = {
        "color": color,
        "comments": comments,
        "componentIds": componentIds if componentIds is not None else [],
        "criticalness": criticalness,
        "description": description,
        "deviceIds": deviceIds if deviceIds is not None else [],
        "groupIds": groupIds if groupIds is not None else [],
        "label": label,
        "locked": locked,
        "parentId": parentId,
        "userProperties": userProperties if userProperties is not None else []
    }
    headers = get_headers()
    response = requests.post(url, json=data, headers=headers)
    return response


def get_groups():
    """Get list groups"""
    url = f"{BASE_URL}/groups"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response


def get_details_of_multiple_groups(*group_ids):
    """Get details of one or many groups.
    :param group_ids: list of groups id"""
    joined_ids = ";".join(map(str, group_ids))
    url = f"{BASE_URL}groups/{joined_ids}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response


def get_devices(from_int, to_int, page, size, vulnerabilities=False):
    """
    Get list of all devices
    :param fromt_int: last_update start date/time
    :param to_int: end date/time
    :param page: page number
    :param size: records per page
    """
    url = f"{BASE_URL}/devices?from={from_int}&to={to_int}&page={page}&size={size}&vulnerabilities={vulnerabilities}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response


def get_devices_only_id(page, size):
    """
    NOT SURE, TO TEST
    """
    url = f"{BASE_URL}devices?page={page}&size={size}&fields=id,label"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    
    if response.status_code ==  200:
        devices = response.json().get('devices', [])
        return [(device['id'], device['label']) for device in devices]
    else:
        raise Exception(f"Failed to retrieve devices: {response.content}")

    #if response.status_code ==   200:
    #    devices = response.json().get('devices', [])
    #    return [(device['id'], device['label']) for device in devices]
    #else:
    #    raise Exception(f"Failed to retrieve devices: {response.content}")


def get_device(id):
    """Get information for specific device"""
    url = f"{BASE_URL}/devices/{id}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response


def get_vulnerabilities_device(id):
    """Get vulnerabilities of a device"""
    url = f"{BASE_URL}/devices/{id}/vulnerabilities"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response


def add_machines_to_group(group_id, csv_file_path, columnUUID=0):
    """
    Add a machine in a existant group
    :param group_id: ID Group
    :param csv_file_path: Path to .csv file
    :param columnUUID: UUID is a id for the computer, on the .csv file,
    the UUID should be the first column
    """
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            device_id = row[columnUUID] # Column UUID devices
            data = {
                "op": "add",
                "path": "/devices",
                "value": [device_id]
            }
            # This should work, but I don't know at the moment how to retrieve the uuid of the devices and export them in csv format.
            response = requests.patch(f"{BASE_URL}/groups/{group_id}".format(group_id=group_id), json=data, headers=get_headers)
            if response.status_code == 200:
                print(f"Machine {device_id} added to group {group_id}.")
            else:
                print(f"Error adding machine {device_id} to group {group_id}: {response.text}")

def export_devices_list():
    """Export a list of devices on .csv file"""
    url = f"{BASE_URL}/devices/{id}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    # To do
    return response


def find_device_by_ip(ip_address):
    headers = get_headers()
    page = 1
    size = 10
    while True:
        response = requests.get(f"{BASE_URL}/api/3.0/devices?page={page}&size={size}", headers=headers)
        if response.status_code != 200:
            print("Error")
            break
        devices = response.json()
        if not devices:
            print("No device found with this value")
            break
        for device in devices:
            if ip_address in device.get("ip", []):
                return device
        page += 1
    return None


def find_devices_by_ips(ip_addresses):
    headers = get_headers()
    devices_found = []
    page = 1
    size = 10

    while True:
        response = requests.get(f"{BASE_URL}?page={page}&size={size}", headers=headers)
        if response.status_code != 200:
            print("Error")
            break
        devices = response.json()
        if not devices:
            break
        for device in devices:
            if set(ip_addresses) & set(device.get("ip", [])):
                devices_found.append(device)
        page += 1
    
    return devices_found
