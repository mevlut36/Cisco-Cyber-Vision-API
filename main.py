from cybervision.api import add_machines_to_group, get_details_of_multiple_groups, get_groups

from scripts.add_device_group import modify_device_group
from scripts.create_group import create_new_group
from scripts.search_device import search_device
from scripts.get_device_by_id import get_device_by_id
from scripts.get_list_devices import get_all_devices
from scripts.get_vulnerabilities_by_device_id import get_vulnerabilities_device_by_id

from utils.inputs import add_device_group_with_csv, export_list, find_device, get_device, get_device_modification_details, get_devices_details, get_groups_by_id, set_group_details

def menu():
    menu_items = [
        "Add a device to a group",
        "Create a group",
        "Get list of groups",
        "Get details of multiple groups",
        "Get all devices",
        "Get device by ID",
        "Get vulnerabilites device",
        "Add device to a group with .csv",
        "Export (Not work)",
        "Find devices by IP",
        "Quit"
    ]

    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")
    
    choice = input("Choose an option: ")
    return choice


def main():
    while True:
        choice = menu()
        
        if choice == "1":
            info = get_device_modification_details()
            modify_device_group(info)
            
        elif choice == "2":
            group_details = set_group_details()
            create_new_group(*group_details)
            
        elif choice == "3":
            # No parameters required for get list groups
            get_groups()
        
        elif choice == "4":
            grp = get_groups_by_id()
            get_details_of_multiple_groups(grp)
        
        elif choice == "5":
            devices = get_devices_details()
            get_all_devices(devices)

        elif choice == "6":
            device = get_device()
            get_device_by_id(device)
        
        elif choice == "7":
            device = get_device()
            get_vulnerabilities_device_by_id(device)
        
        elif choice == "8":
            info = add_device_group_with_csv()
            add_machines_to_group(info)
        
        elif choice == "9":
            info = export_list()
            pass

        elif choice == "10":
            device = find_device()
            search_device(device)

        elif choice == "Quit":
            print("Bye.")
            break
            
        else:
            print("Input not valid.")

if __name__ == "__main__":
    main()
