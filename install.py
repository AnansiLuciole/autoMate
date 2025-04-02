import subprocess
import sys
from util import download_weights
import urllib.request
import urllib.error

def install_requirements():
    # Check if Google is accessible
    try:
        # Try to connect to Google with a timeout of 3 seconds
        urllib.request.urlopen('https://www.google.com', timeout=3)
        # If successful, install normally
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except (urllib.error.URLError, TimeoutError):
        print("Using Tsinghua mirror")
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', 
            '-r', 'requirements.txt', 
            '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'
        ])


def adjust__env():
    # check if  is at least 3.12
    if sys.version_info.major != 3 or sys.version_info.minor < 12:
        print(" version is less than 3.12, please install  3.12 or higher")
        exit(1)

def install():
    adjust__env()
    install_requirements()
    # download the weight files
    download_weights.download() 
    print("Installation complete!") 

if __name__ == "__main__":
    install()
    print("Installation complete!")