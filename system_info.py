import platform
import socket
import psutil


computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.release()
cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
cpu_usage = psutil.cpu_percent()

print("\n=== System Information ===")
print(f"Computer Name : {computer_name}")
print(f"Operating System : {operating_system}")
print(f"OS Version : {os_version}\n")

print("\n=== CPU Information ===")
print(f"Physical Cores : {cpu_cores}")
print(f"Logical Cores : {cpu_threads}")
print(f"CPU Usage : {cpu_usage}%")