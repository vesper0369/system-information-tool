import platform
import socket


computer_name = socket.gethostname()
operating_system = platform.system()
os_version = platform.release()

print("\n=== System Information ===")
print(f"Computer Name : {computer_name}")
print(f"Operating System : {operating_system}")
print(f"OS Version : {os_version}\n")