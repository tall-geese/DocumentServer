import os
import waitress
from __init__ import create_app
from pathlib import Path

file_dir = Path(__file__).parent
os.chdir(file_dir)

waitress.serve(create_app(), listen='jade76:8081')