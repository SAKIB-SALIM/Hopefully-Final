import subprocess
import sys
import os

def main():
    if hasattr(sys, '_MEIPASS'):
        helper_path = os.path.join(sys._MEIPASS, 'SysInfo.exe')
    else:
        helper_path = os.path.join(os.path.dirname(__file__), 'helper.exe')
    subprocess.run([helper_path])
