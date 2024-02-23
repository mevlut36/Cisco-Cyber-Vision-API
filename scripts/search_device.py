from cybervision.api import find_device_by_ip, find_devices_by_ips

def search_device(ip_address):
    device = find_device_by_ip(ip_address)
    if device:
        print(f"Device found : {device}")
    else:
        print("Device not found")


# ip_addresses = ["192.168.1.1", "192.168.1.2"]
def search_devices(ip_addresses):
    devices = find_devices_by_ips(ip_addresses)
    if devices:
        print("Devices found :")
    for device in devices:
        print(device)
    else:
        print("No device found with these values")
