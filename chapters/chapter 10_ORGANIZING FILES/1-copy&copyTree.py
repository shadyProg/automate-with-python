import shutil , os
from pathlib import Path
p = Path.cwd()
shutil.copytree(p / '1/files/', p / '1/backup/')