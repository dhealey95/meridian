# Meridian

A scalable FastAPI backend service.

## Tech stack

| Layer | Technology |
|---|---|
| Framework | FastAPI + Uvicorn |
| ORM | SQLAlchemy 2 (async) |
| Migrations | Alembic |
| Database | PostgreSQL (asyncpg driver) |
| Validation | Pydantic v2 |
| Auth | JWT (python-jose) + bcrypt |
| Logging | structlog (JSON) |
| Testing | pytest + pytest-asyncio |
| Linting | Ruff + mypy |

## Project structure

```
app/
├── api/
│   ├── deps.py              # Dependency injection (DB session, auth)
│   └── v1/
│       ├── router.py        # Aggregates all v1 endpoint routers
│       └── endpoints/       # One file per resource domain
├── core/
│   ├── config.py            # Pydantic Settings (reads .env)
│   ├── exceptions.py        # Typed HTTP exceptions + handlers
│   ├── logging.py           # structlog configuration
│   └── security.py          # JWT + password hashing helpers
├── db/
│   ├── base.py              # SQLAlchemy DeclarativeBase
│   └── session.py           # Async engine + session factory
├── models/
│   └── base.py              # BaseModel (UUID PK + timestamps)
├── schemas/
│   └── common.py            # Shared Pydantic schemas
├── services/
│   └── base.py              # Generic async CRUD repository
└── main.py                  # App factory + middleware + lifespan
alembic/                     # Migration scripts
tests/                       # Mirrors app/ layout
```

## Getting started

### Prerequisites

- Python 3.12+
- PostgreSQL 15+

### Setup

```bash
# 1. Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# 2. Configure environment
cp .env.example .env
# Edit .env with your values (DATABASE_URL, APP_SECRET_KEY)

# 3. Run migrations
alembic upgrade head

# 4. Start the development server
uvicorn app.main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

### Docker

```bash
# Copy and edit env file
cp .env.example .env

# Start everything (API + Postgres)
docker compose up --build
```

## Development

```bash
# Run tests with coverage
pytest

# Lint and format
ruff check .
ruff format .

# Type check
mypy app/

# Create a new migration
alembic revision --autogenerate -m "describe change"

# Apply migrations
alembic upgrade head
```

## Adding a new resource

1. Create `app/models/your_model.py` extending `BaseModel`
2. Import the model in `app/models/__init__.py` so Alembic detects it
3. Create `app/schemas/your_model.py` with request/response schemas
4. Create `app/services/your_service.py` extending `BaseRepository`
5. Create `app/api/v1/endpoints/your_resource.py` with route handlers
6. Register the router in `app/api/v1/router.py`
7. Generate and apply a migration: `alembic revision --autogenerate -m "add your_model"`
