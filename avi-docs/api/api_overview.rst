API Overview
============

This project exposes two distinct API surfaces:

- Next.js internal API routes under `src/app/api/` for geography, ETL orchestration, authentication, health, and socket events.
- Python Flask endpoints under `avi-etl-pipeline/app.py` for file cleaning and database ingestion.

The main API surface includes:

- `/api/v1/countries`
- `/api/v1/states`
- `/api/v1/districts`
- `/api/v1/subdistricts`
- `/api/v1/villages`
- `/api/etl/upload`
- `/api/etl/status/[jobId]`
- `/api/socket/emit`
- `/api/admin/create-api-key`
- `/api/auth/[...nextauth]`
- `/api/health/db`

The ETL service includes:

- `/upload`
- `/upload-to-db`
- `/health`

Authentication
--------------

- The Next.js API uses API keys validated through Redis and the `src/lib/api-auth-redis.ts` module.
- The Flask ETL service currently does not require authentication.
