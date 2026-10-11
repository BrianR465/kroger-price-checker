# Kroger Price Checker

Pull current prices from the Kroger closest to me.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and set `KROGER_CLIENT_ID` and
   `KROGER_CLIENT_SECRET` to your Kroger developer credentials.
4. Run `python main.py` to request an access token.

Do not commit `.env` or share its contents. If a credential has been exposed,
rotate it in the Kroger developer portal.
