import os
import time
import argparse
import shutil
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Function to find all file extensions in a directory
def Find_all_Extensions(Dirname):
    try:
        extensions = []
        flag = os.path.isabs(Dirname)
        if not flag:
            Dirname = os.path.abspath(Dirname)

        if os.path.exists(Dirname):
            for foldername, subfoldername, filename in os.walk(Dirname):
                for name in filename:
                    exte = os.path.splitext(name)[1]
                    if exte and exte not in extensions:  # skip files without extension
                        extensions.append(exte)
        return extensions
    except Exception as e:
        logging.error("Error at finding all extensions")
        logging.error(e)
        return []

# Main function that drives the sorting process
def Directory_sorter(Dirname, dry_run=False):
    try:
        exxt = Find_all_Extensions(Dirname)
        file_counter = 0
        flag = os.path.isabs(Dirname)
        if not flag:
            Dirname = os.path.abspath(Dirname)

        if os.path.exists(Dirname):
            for i in exxt:
                extension = i
                for foldername, subfoldername, filename in os.walk(Dirname):
                    # skip folders already named by extension
                    if os.path.basename(foldername) == extension.lstrip('.'):
                        continue

                    for name in filename:
                        if name.endswith(extension):
                            file_counter += 1
                            logging.info(f"Processing file {file_counter}: {name}")
                            new_Folder(foldername, extension, name, dry_run)
            logging.info(f"\nTotal files processed: {file_counter}")
    except Exception as obj:
        logging.error("Error at sorter")
        logging.error(obj)

# Function to create folder and move file
def new_Folder(foldername, extension, fname, dry_run=False):
    try:
        ext = extension.lstrip('.')  # clean folder name
        new_path = os.path.join(foldername, ext)

        src = os.path.join(foldername, fname)
        dest = os.path.join(new_path, fname)

        if dry_run:
            logging.info(f"[DRY RUN] Would move: {fname} → {ext}/\n")
        else:
            if not os.path.exists(new_path):
                os.makedirs(new_path, exist_ok=True)
            shutil.move(src, dest)
            logging.info(f"{fname} has been moved to folder '{ext}'\n")
    except Exception as obj:
        logging.error("Error moving file:")
        logging.error(obj)

# Argument parser
def parse_args():
    parser = argparse.ArgumentParser(description="Sort files into folders based on file extensions.")
    parser.add_argument("directory", help="Target directory path")
    parser.add_argument("--dry-run", action="store_true", help="Simulate actions without moving files")
    return parser.parse_args()

# Main entry point
def main():
    logging.info("----------- Directory Sorter Script -----------")
    args = parse_args()

    try:
        starttime = time.time()
        Directory_sorter(args.directory, dry_run=args.dry_run)
        endtime = time.time()
        logging.info(f"\nTime required to execute the script is: {endtime - starttime:.2f} seconds")
        logging.info("--------- Thank you for using the script ---------")
    except Exception as e:
        logging.error("Unable to perform the task due to:")
        logging.error(e)

if __name__ == "__main__":
    main()
