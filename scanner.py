import socket
import datetime
import os

print("=" * 50)
print("PORT SCANNER")
print("=" * 50)

target = input("Enter an IP address or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\nInvalid hostname or IP address.")
    exit()

start_port = int(input("Starting port: "))
end_port = int(input("Ending port: "))

print("\nScanning...")
print("-" * 50)

start_time = datetime.datetime.now()

open_ports = []

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    scanner.close()

end_time = datetime.datetime.now()

os.makedirs("reports", exist_ok=True)

with open("reports/scan_report.txt", "w") as report:

    report.write("PORT SCAN REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Target: {target}\n")
    report.write(f"IP Address: {target_ip}\n")
    report.write(f"Scan Started: {start_time}\n")
    report.write(f"Scan Finished: {end_time}\n\n")

    report.write("Open Ports\n")
    report.write("-" * 20 + "\n")

    if open_ports:
        for port in open_ports:
            report.write(f"{port}\n")
    else:
        report.write("No open ports found.\n")

print("\n" + "=" * 50)
print("Scan Complete")
print("=" * 50)
print(f"Open Ports Found: {len(open_ports)}")
print("Report saved to reports/scan_report.txt")