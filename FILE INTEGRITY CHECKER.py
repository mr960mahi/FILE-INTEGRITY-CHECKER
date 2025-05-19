import hashlib
import os
import json

HASH_FILE = "file_hashes.json"

def get_hash(path):
    h = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None

def hash_folder(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for name in files:
            full_path = os.path.join(root, name)
            hash_val = get_hash(full_path)
            if hash_val:
                hashes[full_path] = hash_val
    return hashes

def load_saved():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_now(hashes):
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)

def compare(old, new):
    added = [f for f in new if f not in old]
    removed = [f for f in old if f not in new]
    changed = [f for f in new if f in old and new[f] != old[f]]
    return added, removed, changed

def main():
    folder = input("Enter the folder path: ").strip()

    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    print("\nScanning files and calculating hashes...\n")

    new_data = hash_folder(folder)
    old_data = load_saved()

    for path, h in new_data.items():
        print(f"File: {path}")
        print(f"Hash: {h}\n")

    added, removed, changed = compare(old_data, new_data)

    if added:
        print("🆕 New files:")
        for f in added:
            print(f)

    if removed:
        print("\n❌ Deleted files:")
        for f in removed:
            print(f)

    if changed:
        print("\n✏️ Modified files:")
        for f in changed:
            print(f)

    if not (added or removed or changed):
        print("\n✅ No changes detected.")

    save_now(new_data)
    print("\nHashes saved.")

if __name__ == "__main__":
    main()
