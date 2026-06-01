import os       # Used to scan folders and check file names
import shutil   # Used to move files from one folder to another

# ─── Configuration ─────────────────────────────────────────────────────────────

# The folder where your .jpg files currently are
# Change this to the path of your source folder
SOURCE_FOLDER = "source_folder"

# The folder where all .jpg files will be moved
# This folder will be created automatically if it doesn't exist
DESTINATION_FOLDER = "jpg_images"

# ─── Create Destination Folder ─────────────────────────────────────────────────

# Check if the destination folder exists; if not, create it
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)  # Creates the folder (and any parent folders)
    print(f"📁 Created folder: '{DESTINATION_FOLDER}'")
else:
    print(f"📁 Folder already exists: '{DESTINATION_FOLDER}'")

# ─── Move .jpg Files ───────────────────────────────────────────────────────────

# Counter to track how many files were moved
moved_count = 0

# Loop through every file in the source folder
for filename in os.listdir(SOURCE_FOLDER):

    # Check if the file ends with .jpg or .JPG (case-insensitive)
    if filename.lower().endswith(".jpg"):

        # Build full file paths for source and destination
        source_path = os.path.join(SOURCE_FOLDER, filename)
        destination_path = os.path.join(DESTINATION_FOLDER, filename)

        # Move the file from source to destination
        shutil.move(source_path, destination_path)

        # Log which file was moved
        print(f"  ✅ Moved: {filename}")

        # Increment the counter
        moved_count += 1

# ─── Summary ───────────────────────────────────────────────────────────────────

# Print final result after all files are processed
if moved_count == 0:
    print("\n⚠️  No .jpg files found in the source folder.")
else:
    print(f"\n🎉 Done! {moved_count} .jpg file(s) moved to '{DESTINATION_FOLDER}'")