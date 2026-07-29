# Retail Inventory Platform

Production-style backend scaffold for a retail inventory synchronization platform with planned Clover POS integration.

## Goals

- Provide a clean, modular FastAPI backend foundation.
- Use PostgreSQL with SQLAlchemy 2.0 and Alembic migrations.
- Support local development with Docker Compose.
- Keep architecture ready for growth without implementing business logic yet.

## Tech Stack

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Docker Compose
- Pytest

## Project Structure

```text
retail-inventory-platform/
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   └── main.py
├── alembic/
├── tests/
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Architecture Overview (Sprint 1)

The scaffold keeps only layers that already execute in the current sprint:

- **API layer (`app/api`)**: HTTP routes and request handling.
- **Core (`app/core`)**: Configuration and cross-cutting app settings.
- **Database (`app/database`)**: Engine, session, and ORM base definitions.

Additional layers (`models`, `schemas`, `services`, `repositories`, `integrations`, `utils`) will be introduced when the first feature needs them.

## Structure Decisions (Keep / Remove / Merge)

This project follows iterative development: keep what is active now, add only when needed.

- **Kept `app/api/`**: already provides active behavior (`GET /health`) and route composition.
- **Kept `app/core/`**: isolates environment/config concerns from web/database code.
- **Kept `app/database/`**: SQLAlchemy base/session are immediately used and deserve clear separation.
- **Kept `alembic/` + `alembic.ini`**: migrations are part of production readiness from day one.
- **Kept `tests/`**: verifies baseline app behavior and protects future refactors.
- **Removed `app/models/`**: was an empty placeholder; no ORM entities exist yet.
- **Removed `app/schemas/`**: no request/response DTOs beyond inline health response yet.
- **Removed `app/services/`**: no business orchestration exists in sprint 1.
- **Removed `app/repositories/`**: no concrete persistence abstraction implemented yet.
- **Removed `app/integrations/clover/`**: Clover integration is planned, but no near-term code shipped yet.
- **Removed `app/utils/`**: no shared helpers exist yet; avoids catch-all dumping ground early.
- **Removed top-level `scripts/`, `data/`, `docs/`**: each contained only `.gitkeep`; no current runtime, tests, or delivery value.
- **Merge decision (`core` + `database`)**: intentionally **not merged**. They each contain active multi-file responsibilities; combining now would reduce clarity without reducing meaningful complexity.

## Setup

1. Copy environment variables:

   ```bash
   cp .env.example .env
   ```

2. Start PostgreSQL:

   ```bash
   docker compose up -d db
   ```

3. Install dependencies (Python 3.12+):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Run the API:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. Verify health endpoint:

   ```bash
   curl http://localhost:8000/health
   ```

## Database Migrations

Create a new migration:

```bash
alembic revision --autogenerate -m "create initial tables"
```

Apply migrations:

```bash
alembic upgrade head
```

## Testing

Run tests with:

```bash
pytest
```

## File-by-File Explanation

- `app/main.py`: FastAPI app entrypoint and router registration.
- `app/api/router.py`: Central API router that composes endpoint modules.
- `app/api/health.py`: Health-check route (`GET /health`) for service monitoring.
- `app/core/config.py`: Environment-driven app settings loaded from `.env`.
- `app/database/base.py`: Shared SQLAlchemy declarative base.
- `app/database/session.py`: SQLAlchemy engine/session setup and DB dependency.
- `alembic.ini`: Alembic runtime configuration.
- `alembic/env.py`: Alembic migration environment and metadata wiring.
- `alembic/script.py.mako`: Template used for generating migration scripts.
- `docker-compose.yml`: Local PostgreSQL service configuration with healthcheck.
- `requirements.txt`: Python dependency manifest.
- `.env.example`: Template for required environment variables.
- `.gitignore`: Excludes environment files, caches, build artifacts, and logs.
- `tests/test_health.py`: Baseline endpoint test using FastAPI TestClient.
