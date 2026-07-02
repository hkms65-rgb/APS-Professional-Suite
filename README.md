# APS Professional Suite

Build 0.3.0 expands APS into a larger Enterprise Operating System foundation.

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

## Run
```bash
pip install -e . pytest fastapi uvicorn
python -m pytest tests -q
uvicorn aps_api.main:app --reload
```
