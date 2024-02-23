from cybervision.api import add_device_on_group

def modify_device_group(group_id, op, path, values):
    response = add_device_on_group(group_id, op, path, values)
    if response.status_code in [200, 201]:
        print(f"Device added successfully on {group_id} id.")
    else:
        print(f"Error in add_device_on_group: {response.status_code}, {response.text}")

    return response
