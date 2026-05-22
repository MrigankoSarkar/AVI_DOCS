API Endpoint Reference
======================

Next.js App API Endpoints
-------------------------

.. list-table:: Next.js API Endpoints
   :header-rows: 1
   :widths: 30 15 55

   * - Endpoint
     - Method
     - Purpose
   * - /api/v1/countries
     - GET, POST, PATCH, DELETE
     - Retrieve and manage country data.
   * - /api/v1/states
     - GET, POST, PATCH, DELETE
     - Retrieve and manage state records.
   * - /api/v1/districts
     - GET, POST, PATCH, DELETE
     - Retrieve and manage district records.
   * - /api/v1/subdistricts
     - GET, POST, PATCH, DELETE
     - Retrieve and manage subdistrict records.
   * - /api/v1/villages
     - GET, POST, PATCH, DELETE
     - Retrieve and manage villages with filtering and pagination.
   * - /api/etl/upload
     - POST
     - Accept JSON payloads for ETL ingestion.
   * - /api/etl/status/[jobId]
     - GET
     - Fetch background ETL job state and progress.
   * - /api/socket/emit
     - POST
     - Emit a Socket.IO message from server-side code.
   * - /api/admin/create-api-key
     - POST
     - Create a new API credential pair for clients.

Python ETL Endpoints
--------------------

.. list-table:: Python ETL Endpoints
   :header-rows: 1
   :widths: 35 15 50

   * - Endpoint
     - Method
     - Purpose
   * - /upload
     - POST
     - Clean uploaded dataset files and return a cleaned CSV.
   * - /upload-to-db
     - POST
     - Clean uploaded dataset files and ingest them into PostgreSQL.
   * - /health
     - GET
     - Return a simple availability check.

Request/Response Expectations
-----------------------------

- Next.js ETL ingestion expects a JSON array of normalized rows.
- Python ETL accepts multipart form uploads of CSV/XLS/XLSX files.
- API responses follow a JSON structure with `success`, `data`, `meta`, and error details.
