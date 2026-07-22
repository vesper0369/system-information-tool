import platform
import socket
import psutil


computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.release()
cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
cpu_usage = psutil.cpu_percent()
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

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

