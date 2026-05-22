Security Principles
===================

Authentication and Authorization
--------------------------------

- The Node application performs API-key authentication using Redis and a database-backed credential store.
- `src/lib/api-auth-redis.ts` provides fast credential validation with active status and expiry checks.
- `src/app/api/v1/*/route.ts` enforces authorization on geography endpoints.
- The Python ETL service does not implement authentication for file uploads as currently submitted.

Secrets Handling
----------------

- Environment variables are used to configure secrets and database connectivity.
- `src/lib/env.ts` validates required keys and hardens Neon database connection strings.
- Do not commit `.env` files or direct credentials into source control.

Encryption and Transport
------------------------

- PostgreSQL connections are hardened with `sslmode=require` and `options=endpoint=...` for Neon compatibility.
- Redis connections are configured with TLS when the URL starts with `rediss://`.

Potential Vulnerabilities
-------------------------

- The ETL upload endpoints should be explicitly protected in production.
- Socket.IO requires a deployment environment that supports long-lived WebSocket connections.
- `NEXTAUTH_URL` and session secrets must be securely managed.
