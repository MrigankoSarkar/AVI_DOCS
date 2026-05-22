Database Documentation
======================

This section documents the data model and persistence strategy used by the project.

Data Model
----------

The application model is defined in two parallel formats:

1. `prisma/schema.prisma` — canonical schema documentation.
2. `src/lib/schema.ts` — Drizzle table definitions for runtime SQL access.

Core Entities
-------------

- `Country`, `State`, `District`, `Subdistrict`, `Village`
- `Client`, `Staff`
- `ApiKey`, `ApiLog`
- `Contact`, `Newsletter`

Primary relationships:

- Country -> State -> District -> Subdistrict -> Village
- Client -> ApiKey
- Account/User -> Session

Runtime Persistence
-------------------

- `src/lib/drizzle.ts` configures the Postgres client.
- `src/lib/env.ts` hardens Neon database URLs with `sslmode=require` and endpoint options.
- The ETL ingestion layer uses Drizzle transactions for atomic upserts.

Python ETL Schema
-----------------

The Python ETL pipeline creates a normalized target schema in `app.py`:

- `country`
- `state`
- `district`
- `subdistrict`
- `village`
- `village_data`

`village_data` captures raw normalized audit records for each uploaded row.

Schema Synchronization
----------------------

The TypeScript and Python models should remain aligned on administrative hierarchy and unique constraints.
Any schema changes in the Node app should be reflected in the ETL database DDL and vice versa.
