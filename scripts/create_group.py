from cybervision.api import create_group

def create_new_group(label, description="", color="string", comments="string", componentIds=None, criticalness=0, deviceIds=None, groupIds=None, locked=True, parentId="string", userProperties=None):
    response = create_group(label, description, color, comments, componentIds, criticalness, deviceIds, groupIds, locked, parentId, userProperties)
    
    if response.status_code in [200, 201]:
        print("Group created successfully.")
    else:
        print(f"Error in create_group: {response.status_code}, {response.text}")
