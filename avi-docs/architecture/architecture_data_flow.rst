Data Flow Diagrams
===================

This section describes the request lifecycle and data flow for both the main application and the ETL pipeline.

.. mermaid::
   :align: center

   flowchart TD
     UI[User Interface] -->|HTTP| NextApi[Next.js App]
     NextApi -->|DB queries| Postgres[(PostgreSQL)]
     NextApi -->|Redis cache| Redis[(Redis)]
     NextApi -->|Socket.IO| Client[Realtime Client]
     NextApi -->|ETL job| BullMQ[(BullMQ)]
     BullMQ -->|Worker| ETLUploader[ETL Uploader]
     ETLUploader -->|DB writes| Postgres
     ETLService[Python ETL Service] -->|Upload CSV/XLSX| Postgres

Main Application Request Lifecycle
----------------------------------

1. Client sends a request to a Next.js route or page.
2. Server actions or API routes validate authorization and environment state.
3. `GeoService` fetches or persists data through Drizzle.
4. Redis is used for caching and API key validation.
5. Analytics events are logged to Redis and persisted in Postgres.

ETL Data Flow
-------------

1. The Flask service accepts `POST /upload` or `POST /upload-to-db`.
2. The ETL loader reads CSV or Excel data into pandas.
3. The dataset is normalized and validated by column mapping.
4. Unique entries are inserted into normalized tables with `ON CONFLICT DO NOTHING`.
5. The raw dataset is also inserted into `village_data` for audit traces.
