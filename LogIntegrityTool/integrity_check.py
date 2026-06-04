import hashlib
import json
import os
import argparse

HASH_FILE = "hashes.json"


# Calculate SHA-256 hash
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# Load saved hashes
def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)

    return {}


# Save hashes
def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


# Get files from a directory or single file
def get_files(path):
    files = []

    if os.path.isfile(path):
        files.append(path)

    elif os.path.isdir(path):

        for root, dirs, filenames in os.walk(path):

            for filename in filenames:
                files.append(os.path.join(root, filename))

    return files


# Initialize hashes
def init_hashes(path):

    hashes = {}

    files = get_files(path)

    for file in files:
        hashes[file] = calculate_hash(file)

    save_hashes(hashes)

    print("Hashes stored successfully.")


# Check integrity
def check_hashes(path):

    saved_hashes = load_hashes()

    if not saved_hashes:
        print("No hashes found. Run init first.")
        return

    files = get_files(path)

    for file in files:

        current_hash = calculate_hash(file)

        if file not in saved_hashes:

            print(f"{file} : NEW FILE")
            continue

        if current_hash == saved_hashes[file]:

            print(f"{file} : Unmodified")

        else:

            print(f"{file} : Modified (Hash mismatch)")


# Update hash after legitimate change
def update_hash(file_path):

    hashes = load_hashes()

    if not os.path.isfile(file_path):
        print("File not found.")
        return

    hashes[file_path] = calculate_hash(file_path)

    save_hashes(hashes)

    print("Hash updated successfully.")


# Main program
parser = argparse.ArgumentParser(
    description="Log File Integrity Monitoring Tool"
)

parser.add_argument(
    "command",
    choices=["init", "check", "update"]
)

parser.add_argument(
    "path"
)

args = parser.parse_args()

if args.command == "init":
    init_hashes(args.path)

elif args.command == "check":
    check_hashes(args.path)

elif args.command == "update":
    update_hash(args.path)
