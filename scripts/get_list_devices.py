from cybervision.api import get_devices

def get_all_devices(from_int, to_int, page, size, vulnerabilities=False):
    response = get_devices(from_int, to_int, page, size, vulnerabilities=False)
    
    if response.status_code in [200, 201]:
        print(response.json())
    else:
        print(f"Error in list_devices: {response.status_code}, {response.text}")
