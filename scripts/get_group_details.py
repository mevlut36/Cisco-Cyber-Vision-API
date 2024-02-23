from cybervision.api import get_details_of_multiple_groups

def get_details_groups(*group_ids):
    response = get_details_of_multiple_groups(*group_ids)
    
    if response.status_code in [200, 201]:
        print("Success:", response.json())
    else:
        print(f"Error in get_details_of_multiple_groups: {response.status_code}, {response.text}")
