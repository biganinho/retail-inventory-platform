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
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── integrations/
│   │   └── clover/
│   ├── utils/
│   └── main.py
├── alembic/
├── tests/
├── scripts/
├── data/
├── docs/
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Architecture Overview

The scaffold follows layered backend structure aligned with clean architecture principles:

- **API layer (`app/api`)**: HTTP routes and request handling.
- **Service layer (`app/services`)**: Business orchestration (to be added later).
- **Repository layer (`app/repositories`)**: Data access abstractions.
- **Model layer (`app/models`)**: SQLAlchemy ORM models.
- **Schema layer (`app/schemas`)**: Request/response contracts.
- **Integration layer (`app/integrations`)**: External systems like Clover POS.
- **Core (`app/core`)**: Configuration and cross-cutting app settings.
- **Database (`app/database`)**: Engine, session, and ORM base definitions.

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
- `app/models/__init__.py`: Placeholder package for ORM entities.
- `app/schemas/__init__.py`: Placeholder package for Pydantic schemas.
- `app/services/__init__.py`: Placeholder package for domain/application services.
- `app/repositories/__init__.py`: Placeholder package for persistence repositories.
- `app/integrations/clover/__init__.py`: Placeholder package for Clover integration code.
- `app/utils/__init__.py`: Placeholder package for shared utilities.
- `alembic.ini`: Alembic runtime configuration.
- `alembic/env.py`: Alembic migration environment and metadata wiring.
- `alembic/script.py.mako`: Template used for generating migration scripts.
- `alembic/versions/`: Generated migration revisions live here.
- `docker-compose.yml`: Local PostgreSQL service configuration with healthcheck.
- `requirements.txt`: Python dependency manifest.
- `.env.example`: Template for required environment variables.
- `.gitignore`: Excludes environment files, caches, build artifacts, and logs.
- `tests/test_health.py`: Baseline endpoint test using FastAPI TestClient.
- `scripts/`, `data/`, `docs/`: Reserved directories for automation, sample/local data, and project docs.
