DB_CONFIG = {
    "driver": "ODBC Driver 18 for SQL Server",  # or 18 if you're using that
    "server": "DESKTOP-KQ88M7T\\SQLEXPRESS",    # double backslash required
    "database": "DataWareHouse",
    "username": "ChinmaySqlUser",
    "password": "Chinmay12",       # replace with the actual password
    "trusted_connection": "no"
}

MICROSOFT_CLIENT_ID = "7e2c0deb-441f-4533-b861-01cbdc0e9dcd"
MICROSOFT_CLIENT_SECRET = "REPLACE IT"
MICROSOFT_TENANT_ID = "74c129d6-75e9-47bc-89e7-fc64baa89a47"
AUTHORITY_URL = f"https://login.microsoftonline.com/{MICROSOFT_TENANT_ID}"
REDIRECT_URI = "http://localhost:8000/auth/callback"
SCOPE = ["User.Read"]
