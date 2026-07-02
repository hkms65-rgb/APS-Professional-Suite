# APS Professional Suite

APS Professional Suite is an Enterprise Operating System.

## Build 0.2.0

This build adds:
- Enterprise Kernel
- Platform Runtime
- SQLite persistence
- Identity model
- Organization model
- Real Estate & Facilities service/API
- CRM service/API
- Market Intelligence app integration
- FastAPI backend
- Static command center
- Engineering docs
- Tests and validation

## Run

```bash
pip install -e . pytest fastapi uvicorn
python -m pytest tests -q
uvicorn aps_api.main:app --reload
```
