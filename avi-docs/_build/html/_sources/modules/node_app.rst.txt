Node Application Module Reference
=================================

This section documents the major modules in `All_India_Villages_API`.

Key module responsibilities:

- `src/lib/env.ts` — environment validation and Neon connection hardening.
- `src/lib/drizzle.ts` — Drizzle ORM client initialization.
- `src/lib/schema.ts` — Drizzle table definitions.
- `src/lib/geo-service.ts` — geography lookup and CRUD logic.
- `src/lib/api-auth-redis.ts` — Redis-backed API key validation.
- `src/lib/analytics-service.ts` — request metrics collection and telemetry.
- `src/lib/queue/etl-queue.ts` and `etl-worker.ts` — background ETL job orchestration.
- `pages/api/socket.ts` — Socket.IO server bootstrap.
- `src/app/api/etl/upload/route.ts` — ETL upload and validation endpoint.
- `src/app/api/v1/villages/route.ts` — the main villages data endpoint.

Service Relationships
---------------------

- The web application serves pages and API routes from the App Router.
- Core business logic is encapsulated in `src/lib`.
- Redis provides caching, API-key lookup, rate limiting, analytics, and queue connection.
- BullMQ is used for asynchronous ingestion jobs with progress tracking.

Notes
-----

The Node application uses React and Radix UI for the frontend, but the docs here focus on backend and integration architecture.
