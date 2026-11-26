# OmniVerify

OmniVerify is a Streamlit attendance app with teacher and student portals, subject enrollment, and face and voice attendance pipelines.

## Run locally

Use Python 3.11, then install the packages from `requirements.txt`:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

The face recognition dependencies include native model files, so installation may take a while and may depend on the operating system and Python version.

## Supabase configuration

The app reads `SUPABASE_URL` and `SUPABASE_SECRET_KEY` from Streamlit secrets. For local development, create `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "https://YOUR_PROJECT_REF.supabase.co"
SUPABASE_SECRET_KEY = "YOUR_SERVER_SIDE_SECRET_KEY"
```

Keep this file private. It is excluded from Git. For a hosted Streamlit app, add the same settings in the app's Secrets configuration instead of committing them.

The Supabase project must have the tables and permissions expected by the app's database code. Do not expose a service-role or secret key in browser-side code.

## Deploy on Streamlit Community Cloud

1. Push the project to GitHub without `.venv` or local secrets.
2. Create a Streamlit app connected to this repository, using `app.py` as the entry point.
3. Add `SUPABASE_URL` and `SUPABASE_SECRET_KEY` in the app's Secrets settings.
4. Deploy and review the build logs if a native face-recognition dependency fails to install.

Dependencies are listed in `requirements.txt`. The repository intentionally does not include a virtual environment; each machine or deployment creates its own from that file.

## Typography

Use **Outfit** as the app's standard font, including for future landing pages. The shared font stack and responsive heading sizes are defined in `src/ui/base_layout.py`; pages that call `style_base_layout()` inherit them. Outfit loads from Google Fonts, with system UI fonts as fallbacks when it is unavailable. Heading sizes use CSS `clamp()` so they scale between phone, tablet, and desktop widths.
