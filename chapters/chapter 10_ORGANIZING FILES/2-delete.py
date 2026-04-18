import os
from pathlib import Path
import send2trash
for filename in Path(Path.cwd()/'1/backup/spam_backup').glob('*.txt'):
    os.unlink(filename)
    #or
    # send2trash.send2trash(filename)