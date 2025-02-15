import requests
from decouple import config
from dotenv import load_dotenv

load_dotenv()


# Disable IPv6
requests.packages.urllib3.util.connection.HAS_IPV6 = False

try:
    SERVER_IP = requests.get("https://api.ipify.org", timeout=5).text.strip()
except requests.exceptions.RequestException:
    print("Failed to get SERVER_IP, using 127.0.0.1 instead")
    SERVER_IP = "127.0.0.1"


SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL", default="sqlite:///db.sqlite3")


UVICORN_HOST = config("UVICORN_HOST", default="0.0.0.0")
UVICORN_PORT = config("UVICORN_PORT", cast=int, default=443)
UVICORN_UDS = config("UVICORN_UDS", default=None)
UVICORN_SSL_CERTFILE = config("UVICORN_SSL_CERTFILE", default=None)
UVICORN_SSL_KEYFILE = config("UVICORN_SSL_KEYFILE", default=None)


DEBUG = config("DEBUG", default=False, cast=bool)
DOCS = config("DOCS", default=False, cast=bool)


XRAY_JSON = config("XRAY_JSON", default="./xray.json")
XRAY_FALLBACKS_INBOUND_TAG = config("XRAY_FALLBACKS_INBOUND_TAG", cast=str, default="") \
    or config("XRAY_FALLBACK_INBOUND_TAG", cast=str, default="")
XRAY_EXECUTABLE_PATH = config("XRAY_EXECUTABLE_PATH", default="/usr/local/bin/xray")
XRAY_ASSETS_PATH = config("XRAY_ASSETS_PATH", default="/usr/local/share/xray")
XRAY_EXCLUDE_INBOUND_TAGS = config("XRAY_EXCLUDE_INBOUND_TAGS", default='').split()
XRAY_SUBSCRIPTION_URL_PREFIX = config("XRAY_SUBSCRIPTION_URL_PREFIX", default="").strip("/")


TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN", default=None)
TELEGRAM_ADMIN_ID = config("TELEGRAM_ADMIN_ID", cast=int, default=0)
TELEGRAM_PROXY_URL = config("TELEGRAM_PROXY_URL", default=None)

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = config("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=1440)


# USERNAME: PASSWORD
SUDOERS = {
    config("SUDO_USERNAME", default="admin"): config("SUDO_PASSWORD", default="admin")
}
