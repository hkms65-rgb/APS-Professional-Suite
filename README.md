# APS Professional Suite

Build 0.3.0 expands APS into a larger Enterprise Operating System foundation.

## Current Engineering Direction

APS is being evolved toward Build 10.0.0 through verified implementation increments. GitHub remains the authoritative source of truth.

## Added in 0.3.0
- Authentication service
- Policy engine
- Workflow engine
- Notification center
- Document manager
- Integration hub
- Finance, HR, Warehouse, Manufacturing, Procurement, and AI Studio services
- Expanded FastAPI API routes
- Tests and validation

## Current verified implementation additions
- Signed token infrastructure
- Environment-backed runtime configuration
- SQLite database persistence foundation
- Versioned database migration runner
- Repository-backed CRM, Finance, Warehouse, Procurement, HR, and Real Estate services
- Persistent CRM, Finance, Warehouse, Procurement, and Real Estate API wiring
- HR repository and service persistence implemented; HR API wiring pending after connector safety block

## Runtime configuration

APS reads runtime settings from environment variables with safe development defaults.

| Variable | Default | Purpose |
| --- | --- | --- |
| `APS_APP_NAME` | `APS Professional Suite` | FastAPI application title |
| `APS_VERSION` | `0.3.0` | Runtime version string |
| `APS_ENVIRONMENT` | `development` | Runtime environment label |
| `APS_DATABASE_PATH` | `data/aps.sqlite3` | SQLite database file path |
| `APS_SIGNING_KEY` | `development-key-change-me` | Development signing key setting |

## Run
```bash
pip install -e . pytest fastapi uvicorn
python -m pytest tests -q
uvicorn aps_api.main:app --reload
```
