import platform
import socket
import psutil
from datetime import datetime

def get_system_info():
    computer_name = socket.gethostname()
    operating_system = platform.system()
    os_version = platform.release()

    return computer_name, operating_system, os_version

def get_cpu_info():
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent()

    return cpu_cores, cpu_threads, cpu_usage

def get_memory_info():
    memory = psutil.virtual_memory()

    return memory

def get_disk_info():
    disk = psutil.disk_usage("/")

    return disk

def get_ip_address():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address

def create_report():
    computer_name, operating_system, os_version = get_system_info()

    cpu_cores, cpu_threads, cpu_usage = get_cpu_info()

    memory = get_memory_info()

    disk = get_disk_info()

    ip_address = get_ip_address()

    report = f"""
    ===== System Information Report =====

    Computer Name : {computer_name}
    Operating System : {operating_system}
    OS Version : {os_version}

    CPU
    ----------------
    Physical Cores : {cpu_cores}
    Logical Cores : {cpu_threads}
    CPU Usage : {cpu_usage}%

    Memory
    ----------------
    Total Memory : {memory.total / (1024 ** 3):.2f} GB
    Used Memory : {memory.used / (1024 ** 3):.2f} GB
    Available Memory : {memory.available / (1024 ** 3):.2f} GB
    Memory Usage : {memory.percent}%

    Disk
    ----------------
    Total Disk : {disk.total / (1024 ** 3):.2f} GB
    Used Disk : {disk.used / (1024 ** 3):.2f} GB
    Free Disk : {disk.free / (1024 ** 3):.2f} GB
    Disk Usage : {disk.percent}%

    Network
    ----------------
    Local IP Address : {ip_address}

    Generated Time : {datetime.now()}
    """
    return report

report = create_report()
print(report)


with open("system_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport saved successfully!")