from cybervision.api import get_vulnerabilities_device

def get_vulnerabilities_device_by_id(id):
    response = get_vulnerabilities_device(id)
    
    if response.status_code in [200, 201]:
        print(response.json())
    else:
        print(f"Error in list_devices: {response.status_code}, {response.text}")
