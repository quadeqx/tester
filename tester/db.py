import os
from azure.identity import ClientSecretCredential


class TokenProvider:
    _credential = None

    @classmethod
    def get_token(cls):
        """Returns a fresh AAD token (auto-refreshes)."""
        print("Retrieving token...")
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

            # Return the token as the database password
            return token.token

        except ValueError as e:
            return
