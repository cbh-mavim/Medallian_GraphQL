from msal import ConfidentialClientApplication
from app.settings import config

def build_msal_app():
    return ConfidentialClientApplication(
        config.MICROSOFT_CLIENT_ID,
        authority=config.AUTHORITY_URL,
        client_credential=config.MICROSOFT_CLIENT_SECRET,
    )

def get_auth_url():
    app = build_msal_app()
    return app.get_authorization_request_url(
        scopes=config.SCOPE,
        redirect_uri=config.REDIRECT_URI
    )

def get_token_from_code(auth_code):
    app = build_msal_app()
    result = app.acquire_token_by_authorization_code(
        auth_code,
        scopes=config.SCOPE,
        redirect_uri=config.REDIRECT_URI
    )
    return result
