import subprocess

target = input("Target IP: ").strip()

commands = {
    "Port Scan": [
        "nmap",
        "-sV",
        "-p",
        "139,445",
        target
    ],
    "OS Discovery": [
        "nmap",
        "--script",
        "smb-os-discovery",
        "-p445",
        target
    ],
    "Share Enumeration": [
        "nmap",
        "--script",
        "smb-enum-shares",
        "-p445",
        target
    ],
    "Protocol Enumeration": [
        "nmap",
        "--script",
        "smb-protocols",
        "-p445",
        target
    ]
}

for title, cmd in commands.items():
    print(f"\n{'=' * 60}")
    print(title)
    print('=' * 60)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    print(result.stdout)