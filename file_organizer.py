import os
import shutil

print("=" * 40)
print("       JPG FILE ORGANIZER")
print("=" * 40)

source_folder = input("Enter the folder path containing JPG images: ").strip().strip('"')

if not os.path.isdir(source_folder):
    print("Error: The folder does not exist. Please check the path.")
else:
    destination_folder = os.path.join(source_folder, "JPG_Images")
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path) and filename.lower().endswith((".jpg", ".jpeg")):
            destination_path = os.path.join(destination_folder, filename)

            if os.path.exists(destination_path):
                print("Skipped:", filename, "- already exists.")
                continue

            try:
                shutil.move(source_path, destination_path)
                print("Moved:", filename)
                moved_count += 1
            except OSError as error:
                print("Error moving", filename, ":", error)

    print("\nTask completed!")
    print("Total images moved:", moved_count)
    print("Destination folder:", destination_folder)