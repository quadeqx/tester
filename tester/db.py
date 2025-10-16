import subprocess
import time
import os
from azure.identity import ClientSecretCredential


class TokenProvider:
    _credential = None

    @classmethod
    def get_token(cls):
        """Returns a fresh AAD token (auto-refreshes)."""
        print("Retrieving token...")
        time.sleep(3)
        try:
            # Initialize the credential only once (auto-refreshes internally)
            if cls._credential is None:
                cls._credential = ClientSecretCredential(
                    tenant_id=os.getenv("TENANT_ID"),
                    client_id=os.getenv("CLIENT_ID", "placeholder"),
                    client_secret=os.getenv("CLIENT_SECRET")
                )

            # Always request a new access token (SDK handles refresh)
            token = cls._credential.get_token(
                "https://ossrdbms-aad.database.windows.net/.default"
            )
            print("Token retrieved...")
            return token.token
        except Exception as e:
            print(f"=====ERROR====\n{e}")
            time.sleep(2)
            return
