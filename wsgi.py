import sys
sys.path.append('/home/garciagi/SCS_Tool')
sys.path.append('/home/garciagi/.local/lib/python3.6/site-packages')

from main import app as application

if __name__ == '__main__':
    application.run()