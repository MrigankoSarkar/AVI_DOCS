# All India Villages API Docs (v1.0.0)

<p align="center">
  Enterprise-grade Indian administrative geography API, analytics platform, and ETL ecosystem built with Next.js, PostgreSQL, Redis, BullMQ, and Python ETL services.
</p>

<p align="center">

  <!-- Documentation -->
  <a href="https://avi-docs.readthedocs.io/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/readthedocs/avi-docs?style=for-the-badge" alt="Read the Docs">
  </a>

  <!-- License -->
  <a href="./LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License">
  </a>

  <!-- Repo Stats -->
  <img src="https://img.shields.io/github/stars/MrigankoSarkar/All_India_Villages_API?style=for-the-badge" alt="Stars">

  <img src="https://img.shields.io/github/forks/MrigankoSarkar/All_India_Villages_API?style=for-the-badge" alt="Forks">

  <img src="https://img.shields.io/github/issues/MrigankoSarkar/All_India_Villages_API?style=for-the-badge" alt="Issues">

</p>

---

## Deployments


<p align="center">

  <!-- Main Website -->
  <a href="https://all-india-villages-api-lyart.vercel.app" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Live_Website-All_India_Villages_API-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Website">
  </a>

  <!-- ETL Pipeline Website -->
  <a href="https://avi-etl-pipeline.onrender.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/ETL_Pipeline_Website-Cloud_Hosting-5A67D8?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  </a>

  <!-- Neon -->
  <a href="https://neon.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Neon-Serverless_Postgres-00E599?style=for-the-badge&logo=neon&logoColor=black" alt="Neon">
  </a>

  <!-- Vercel -->
  <a href="https://vercel.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Vercel-Deployment-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
  </a>

  <!-- Upstash -->
  <a href="https://upstash.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Upstash-Redis-00C98D?style=for-the-badge&logo=upstash&logoColor=white" alt="Upstash">
  </a>

  <!-- Render -->
  <a href="https://render.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Render-Cloud_Hosting-5A67D8?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  </a>

</p>

---

## Overview

The **All India Villages API** is a production-grade administrative geography platform designed to provide normalized hierarchical access to Indian administrative divisions from country level down to villages.

The platform combines:

- A scalable Next.js API and analytics service
- Redis-backed caching and authentication
- BullMQ-based ETL queue processing
- PostgreSQL relational geography storage
- A standalone Python ETL ingestion pipeline
- Dashboard, analytics, and realtime event support

The system is designed for enterprise data services, GIS workflows, government datasets, analytics platforms, and large-scale geography lookup systems.

---

## Repository Structure

```bash
.
├── All_India_Villages_API/   # Main Next.js application
├── avi-etl-pipeline/         # Python ETL ingestion service
├── avi-docs/                 # Sphinx documentation
├── .github/                  # GitHub workflows
└── .readthedocs.yaml         # Read the Docs config
```

This documentation summarizes the full source code and architecture of the All India Villages API project. It covers both:

- `All_India_Villages_API/` — the main Next.js application with API services, authentication, analytics, Redis support, and frontend pages.
- `avi-etl-pipeline/` — the separate Python-based ETL pipeline for cleaning and ingesting MDDS-like village data into PostgreSQL.

The file is intentionally written as a single consolidated documentation to provide a unified reference for both projects while keeping the two codebases distinct.

---

## 1. All_India_Villages_API

### 1.1 Project Purpose

The main application is a production-grade, enterprise-style Node.js service built with Next.js 15 App Router. Its purpose is to publish a normalized hierarchical catalog of Indian administrative divisions from country down to village, expose an authenticated API surface, support dashboard/analytics flows, and integrate ETL ingestion with background processing.

### 1.2 Technology Stack

- Next.js 15 App Router
- React 19
- TypeScript
- Drizzle ORM (`drizzle-orm/postgres-js`) for runtime DB access
- Prisma schema for canonical model definition
- Redis via `ioredis` for caching, API-key lookup, and rate limiting
- BullMQ for queueing ETL ingestion jobs
- Socket.IO for realtime event delivery
- Firebase, Resend, and Auth.js style patterns for authentication/email flows
- Tailwind CSS and Radix UI for frontend UI components

### 1.3 Repository Layout

Key top-level files and directories:

- `package.json` — Node scripts, dependencies, and build commands.
- `drizzle.config.ts` — Drizzle CLI configuration.
- `next.config.ts` — Next.js application configuration.
- `prisma/schema.prisma` — canonical data model definition for the relational schema.
- `src/app/` — Next.js App Router pages, layouts, and route handlers.
- `src/lib/` — core application services and utilities.
- `src/components/` — reusable UI components and primitives.
- `src/hooks/` — custom React hooks.
- `pages/api/socket.ts` — Socket.IO server bootstrap using the Pages Router.
- `scripts/etl_processor.py` — an additional ETL utility script.

### 1.4 Data Model

The project models identity, enterprise usage, location hierarchies, and analytics.

#### Identity & Access

- `Account` — Auth.js provider account data.
- `Session` — Auth session store.
- `User` — authenticated portal user.
- `VerificationToken` — promo/login verification token.
- `Client` — enterprise client account metadata.
- `Staff` — internal staff users and departments.
- `ApiKey` — credential store for API key usage.

#### Geography

- `Country` — root country entity.
- `State` — state entity, unique by `(countryId, code)`.
- `District` — district entity, unique by `(stateId, code)`.
- `Subdistrict` — subdistrict entity, unique by `(districtId, code)`.
- `Village` — village entity, unique by `(subdistrictId, code)`.

#### Analytics & Logging

- `ApiLog` — request metrics and response data.
- `Contact` — contact form submissions.
- `Newsletter` — emailed newsletter subscribers.

### 1.5 Runtime Architecture

#### Environment Loading

`src/lib/env.ts` validates and normalizes required environment settings using Zod. It also hardens Neon PostgreSQL URLs by adding `sslmode=require` and `options=endpoint=...` to improve Neon compatibility.

#### Database Layer

`src/lib/drizzle.ts` instantiates a pooled `postgres` client and exposes `db = drizzle(client, { schema })`.

`src/lib/prisma.ts` is intentionally neutralized and serves only as a placeholder because the runtime uses Drizzle while Prisma remains the canonical schema provider.

#### Redis & Caching

`src/lib/redis.ts` creates a shared Redis client tuned for serverless/cloud environments with short timeouts and lazy connection. It is used for:

- API-key lookup (`api-auth-redis.ts`)
- cached geographic listings (`geo-service.ts`)
- analytics counters and telemetry (`analytics-service.ts`)
- rate limiting (`rate-limit.ts`)

#### API Key Validation

- `src/lib/api-auth.ts` validates an API key/secret pair against the database using bcrypt.
- `src/lib/api-auth-redis.ts` validates credentials against Redis cache for sub-5ms authorization and supports automatic expiry cleanup.

#### Geo Service

`src/lib/geo-service.ts` provides hierarchical CRUD operations for countries, states, districts, subdistricts, and villages. It includes:

- cache-backed state listing
- hierarchical fetches for villages by state/district/subdistrict
- search and pagination for villages
- create/update/delete operations for each entity
- a simple statistics summary method

### 1.6 API Surface

The service exposes both internal and external API endpoints.

#### Realtime Socket

- `pages/api/socket.ts` initializes a Socket.IO server and listens for `join-room` events.
- `src/lib/socket-emitter.ts` triggers socket events through an internal route from server-side actions.

#### Geo Endpoints

- `src/app/api/v1/countries/route.ts`
- `src/app/api/v1/states/route.ts`
- `src/app/api/v1/districts/route.ts`
- `src/app/api/v1/subdistricts/route.ts`
- `src/app/api/v1/villages/route.ts`

These endpoints perform:

- `GET` for data retrieval with optional filtering
- `POST` to create new records
- `PATCH` to update existing records
- `DELETE` to remove records

All v1 endpoints are wrapped with request telemetry and Redis API-key validation.

#### ETL API

- `src/app/api/etl/upload/route.ts` accepts validated JSON dataset payloads and enqueues ingestion jobs using BullMQ.
- `src/app/api/etl/status/[jobId]/route.ts` returns job state, progress, result, and errors.
- `src/app/api/etl/process/route.ts` is intentionally disabled and returns a 404-style error.

#### Upload and User APIs

The codebase also includes endpoint groups for:

- `api/admin/create-api-key`
- `api/auth/[...nextauth]`
- `api/health/db`
- `api/socket/emit`

and many frontend-facing action pages under `src/app/(auth)` and `src/app/dashboard`.

### 1.7 Background Processing

#### ETL Queue

- `src/lib/queue/etl-queue.ts` defines a BullMQ queue with exponential retry backoff and cleanup policy.
- `src/lib/queue/etl-worker.ts` defines a worker that processes batches of rows sequentially and updates progress.

#### ETL Validation and Upload

- `src/lib/etl/validator.ts` performs strict MDDS validation, structure normalization, deduplication within the upload batch, and returns accepted/rejected rows.
- `src/lib/etl/uploader.ts` ingests validated rows via Drizzle transactions and performs upserts for the full MDDS hierarchy.

### 1.8 Frontend and UI

The UI is organized under `src/app/` and includes:

- global layouts and CSS: `globals.css`, `layout.tsx`
- auth flows: login, register, forgot-password
- dashboard and admin pages
- nested page structures for API, ETL, analytics, and documentation
- reusable component library in `src/components/ui/`

The app uses Radix UI primitives and Tailwind-based custom components.

### 1.9 Operational and Security Notes

- `package.json` includes dev scripts for `dev`, `build`, `start`, `lint`, `typecheck`, and `db:push`.
- The code is designed to support Neon/Postgres and optionally Redis.
- `src/lib/env.ts` requires `DATABASE_URL`, `NEXTAUTH_SECRET`, and `NEXTAUTH_URL`.
- `RESEND_API_KEY` is optional for email integration.
- The code includes a rate limiter that fails open if Redis is unavailable.
- Socket.IO deployment is only safe on platforms that expose a raw HTTP server.

### 1.10 Gaps and Recommendations

- The ETL route `src/app/api/etl/process/route.ts` is disabled; this likely requires planned future implementation or migration to a dedicated worker process.
- `src/lib/prisma.ts` is a stub; if Prisma runtime is needed, the file must be replaced with a real client.
- API documentation is implicit; adding an OpenAPI spec or Swagger would improve developer onboarding.
- The current file upload and dashboard flows appear to be internal and would benefit from explicit authentication enforcement on ETL endpoints.

---

## 2. avi-etl-pipeline

### 2.1 Project Purpose

`avi-etl-pipeline/` is a standalone Python ETL web service intended to clean MDDS-like village dataset files and insert normalized administrative geography into PostgreSQL.

### 2.2 Technology Stack

- Python 3.x
- Flask
- pandas
- SQLAlchemy
- psycopg2-binary
- python-dotenv

### 2.3 Repository Layout

- `app.py` — complete Flask application, input validation, dataset cleaning, and database ingestion.
- `requirements.txt` — Python dependency manifest.
- `runtime.txt` — runtime version hint (`python-3.11.11`).
- `templates/index.html` — simple upload UI.
- `static/app.js`, `static/style.css` — supporting client assets.
- `uploads/` — temporary upload storage.
- `cleaned_output/` — cleaned CSV export storage.
- `cleaned-etl-dataset/` — sample cleaned output dataset storage.

### 2.4 Data Flow

#### Upload and Clean

- `POST /upload` accepts `csv`, `xls`, or `xlsx`.
- Input is loaded with pandas:
  - `read_csv` with UTF-8, fallback to Latin1
  - `read_excel` for Excel files
- Columns are renamed from MDDS-like names to canonical fields.
- Required columns are validated.
- Data is normalized by trimming, title-casing, and removing blanks.
- Duplicates are removed based on `village_code`.
- A cleaned CSV file is generated and returned as an attachment.

#### Upload to DB

- `POST /upload-to-db` performs the same cleaning flow and additionally:
  - creates the normalized table schema if missing
  - inserts the root `country` record for India
  - inserts state, district, subdistrict, and village rows using hierarchical lookups
  - writes a raw `village_data` audit table row for every record
  - uses `ON CONFLICT DO NOTHING` for idempotent ingestion

### 2.5 Database Schema

The ETL uses a normalized relational schema with these tables:

- `country`
- `state`
- `district`
- `subdistrict`
- `village`
- `village_data`

Unique constraints enforce one record per code per parent entity, which matches the MDDS nested structure.

### 2.6 Environment and Execution

- Requires `DATABASE_URL` in `.env`.
- Configured to require TLS by setting `sslmode=require`.

Quick startup example:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
set DATABASE_URL="postgresql://user:pass@host:5432/dbname"
python app.py
```

### 2.7 Observations and Risks

- The service is intended for internal ETL use and has no authentication on upload endpoints.
- Large datasets may require chunked ingestion; currently the entire upload is processed in-memory.
- CSV and Excel support is good, but the schema mapping is fixed to a narrow set of column names.
- The Python ETL and the Node.js app use separate ingestion pipelines; this is useful for separation but also means two independent codebases must remain aligned on schema and data cleanliness.

### 2.8 Improvement Opportunities

- Add authentication or network-level protection for `/upload` and `/upload-to-db`.
- Introduce streaming/batch ingestion to support large files safely.
- Add explicit schema validation on read and after cleaning.
- Add an audit trail for dataset uploads and ingestion events.

---

## 3. Integration Between Projects

### 3.1 How They Fit Together

- The main Next.js service provides the API and frontend experience.
- The Python ETL service is designed to clean and populate the same geographic model but in a separate process.
- `prisma/schema.prisma` in the Node app and the SQL schema in `avi-etl-pipeline/app.py` are aligned in structure: country, state, district, subdistrict, village.
- The Node app also has an internal ETL path (`src/app/api/etl/upload`) using JSON and BullMQ that is currently active, while the Python app is external and file-based.

### 3.2 Consistency Notes

- Both projects use the standard hierarchical code/name pairs of MDDS data.
- Both treat `IN` / India as the root country.
- Both support deduplication and idempotent ingest patterns via conflict handling.

---

## 4. Recommendations

### 4.1 Immediate Fixes

- Re-enable or implement the disabled `src/app/api/etl/process/route.ts` if the internal ETL pipeline is intended to be used.
- Add explicit authentication on the Python ETL upload endpoints before exposing them beyond trusted infrastructure.
- Maintain synchronization between the `prisma/schema.prisma` schema and the Python ETL SQL schema.

### 4.2 Improvements for Production

- Add OpenAPI/Swagger documentation for the API endpoints.
- Add unit and integration tests for the ETL validator, uploader, and API routes.
- Add a `.env.example` file documenting environment variables.
- Add a `CONTRIBUTING.md` or `DEVELOPMENT.md` for local runbooks and deployment instructions.
- Add a dedicated log/metrics export pipeline for production.

### 4.3 Architecture Enhancements

- Move the ETL ingestion worker into a dedicated background service and keep route handlers lightweight.
- Consider using `COPY` or bulk insert mechanisms in the Python ETL for very large datasets.
- Add monitoring for Redis and PostgreSQL connectivity.

---

## 5. Conclusion

This documentation is based on a full codebase of both All India Villages API Project and ETL Pipeline. It captures the architecture, runtime behavior, data model, API surface, ETL processing, operational concerns, and recommended improvements for both the `All_India_Villages_API` and `avi-etl-pipeline` directories.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

## Author

Developed and maintained by **Mriganko Sarkar**.

---

## Maintainers

Maintained by the All India Villages API contributors.

For enterprise integrations, ETL workflows, collaboration, or infrastructure support, contact via LinkedIn or email above.

---

## Documentation

Full documentation is available at: [ReadTheDocs](https://avi-docs.readthedocs.io/)