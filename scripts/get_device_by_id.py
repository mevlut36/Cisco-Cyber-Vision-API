from cybervision.api import get_device

def get_device_by_id(id):
    response = get_device(id)
    
    if response.status_code in [200, 201]:
        print(response.json())
    else:
        print(f"Error in list_devices: {response.status_code}, {response.text}")
