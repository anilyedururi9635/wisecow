import os
import shutil
import subprocess
from datetime import datetime
SOURCE_DIR = "/path/to/local/directory"                
BACKUP_DIR = "/path/to/local/backup/folder"
USE_REMOTE_SERVER = False 
REMOTE_USER = "ec2-user"
REMOTE_HOST = "your.remote.server"
REMOTE_DIR = "/remote/backup/path"
def local_backup():
    try:
        timestamp = datetime.now().strftime("Yearmonthday_Hourmonthsecond")
        destination = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
        shutil.copytree(SOURCE_DIR, destination)
        print(f"Local backup created at {destination}")
    except Exception as e:
        print(f"Local backup failed: {e}")
def remote_backup():
    try:
        result = subprocess.run(
            ["rsync", "-avz", "--delete", SOURCE_DIR, f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"Remote backup completed successfully.")
        else:
            print(f" Remote backup failed:\n{result.stderr}")
    except Exception as e:
        print(f" Remote backup failed: {e}")
if __name__ == "__main__":
    print(" Starting Backup...")
    if USE_REMOTE_SERVER:
        remote_backup()
    else:
        local_backup()
