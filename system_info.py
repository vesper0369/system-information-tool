import platform
import socket
import psutil
from datetime import datetime


computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.release()
cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
cpu_usage = psutil.cpu_percent()
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

ip_address = s.getsockname()[0]

s.close()

print("\n=== System Information ===")
print(f"Computer Name : {computer_name}")
print(f"Operating System : {operating_system}")
print(f"OS Version : {os_version}\n")

print("\n=== CPU Information ===")
print(f"Physical Cores : {cpu_cores}")
print(f"Logical Cores : {cpu_threads}")
print(f"CPU Usage : {cpu_usage}%")

print("\n=== Memory Information ===")
print(f"Total Memory : {memory.total / (1024 ** 3):.2f} GB")
print(f"Used Memory : {memory.used / (1024 ** 3):.2f} GB")
print(f"Available Memory : {memory.available / (1024 ** 3):.2f} GB")
print(f"Memory Usage : {memory.percent}%")

print("\n=== Disk Information ===")
print(f"Total Disk : {disk.total / (1024 ** 3):.2f} GB")
print(f"Used Disk : {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk : {disk.free / (1024 ** 3):.2f} GB")
print(f"Disk Usage : {disk.percent}%")

print("\n=== Network Information ===")
print(f"Local IP Address : {ip_address}")

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

with open("system_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport saved successfully!")