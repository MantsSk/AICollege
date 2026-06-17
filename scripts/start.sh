#!/usr/bin/env bash
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Seeding courses from markdown..."
python -m app.seed

echo "Starting AI College..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
