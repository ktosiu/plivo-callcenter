import os

APP_URL = "http://5b58e10c.ngrok.io"

# Plivo Auth ID and Auth Token
PLIVO_AUTH_ID = os.environ.get('PLIVO_AUTH_ID')
PLIVO_AUTH_TOKEN = os.environ.get('PLIVO_AUTH_TOKEN')

DB_HOST="localhost"
DB_NAME="plivo"
DB_PASSWD=os.environ.get('DB_PASSWD')
SIP_USERNAME = "simula67150918103656"