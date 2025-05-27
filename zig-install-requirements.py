"""
zig-install-requirements.py

Downloads prebuilt Zig executables listed in 'requirements-zig.txt'.

Each line should be a full URL like:
https://github.com/denisecase/zig-bill-utils/raw/refs/heads/main/zig-out/x86_64-windows/clean_bill.exe

Each file is downloaded to a matching local path:
zig-out/x86_64-windows/clean_bill.exe
"""

import os
import requests

def install_zig_requirements(requirements_file='requirements-zig.txt'):
    if not os.path.exists(requirements_file):
        print(f"ERROR: {requirements_file} does not exist.")
        return

    with open(requirements_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    for url in urls:
        try:
            # Extract subpath from URL after 'zig-out/'
            parts = url.split('/zig-out/')
            if len(parts) != 2:
                print(f"Skipping malformed URL: {url}")
                continue

            subpath = parts[1]  # e.g. x86_64-windows/clean_bill.exe
            out_path = os.path.join("zig-out", *subpath.split('/'))

            # Ensure output directory exists
            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            print(f"Downloading: {url}")
            response = requests.get(url)
            response.raise_for_status()

            with open(out_path, 'wb') as f:
                f.write(response.content)

            print(f"Saved to: {out_path}")
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

if __name__ == "__main__":
    install_zig_requirements()
