Architecture Overview
=====================

The repository contains two separate but related systems:

- `All_India_Villages_API` — a TypeScript-based Next.js application that exposes an API surface, dashboards, realtime events, and ETL orchestration.
- `avi-etl-pipeline` — a Python Flask service that cleans, validates, and ingests MDDS-style data into PostgreSQL.

System Boundaries
-----------------

- The Next.js application is responsible for frontend routing, secure API endpoints, analytics, and Redis-backed operational helpers.
- The Python ETL service is responsible for dataset ingestion and raw data cleaning.

Core Components
---------------

- `src/lib/env.ts` — environment validation and Neon URL hardening.
- `src/lib/drizzle.ts` — Postgres client initialization and schema binding.
- `src/lib/schema.ts` — Drizzle table definitions for identity, geography, analytics, and API keys.
- `src/lib/geo-service.ts` — hierarchical geography access and caching.
- `src/lib/etl/validator.ts` — strict dataset validation of MDDS rows.
- `src/lib/etl/uploader.ts` — transactional ingestion using Drizzle.
- `src/lib/queue/etl-queue.ts` and `src/lib/queue/etl-worker.ts` — BullMQ job scheduling and background processing.
- `pages/api/socket.ts` — Socket.IO server bootstrap.
- `avi-etl-pipeline/app.py` — ETL Flask application with `/upload` and `/upload-to-db` routes.

Technology Stack
----------------

- Next.js 15 App Router
- TypeScript
- React 19
- Drizzle ORM for Postgres
- Redis for caching and queue coordination
- BullMQ for background ETL jobs
- Flask, pandas, SQLAlchemy for the Python ETL service

Deployment Considerations
-------------------------

- The Node app requires a host with raw HTTP and WebSocket support for Socket.IO.
- The Python ETL service should be placed behind secure network controls if exposed publicly.
- Shared data store assumptions: PostgreSQL compatible with Neon, and Redis for cache and queueing.
