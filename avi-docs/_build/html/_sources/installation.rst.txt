Installation Guide
===================

This section describes how to configure, install, and run the All India Villages API documentation and projects locally.

Local Setup
-----------

1. Clone the repository and open the workspace.
2. Create or activate the Python virtual environment from the repository root:

   .. code-block:: bash

      python -m venv .venv
      source .venv/Scripts/activate  # Windows
      source .venv/bin/activate      # macOS/Linux

3. Install documentation dependencies:

   .. code-block:: bash

      .venv\Scripts\python.exe -m pip install --upgrade pip
      .venv\Scripts\python.exe -m pip install -r avi-docs/requirements.txt

4. Install application dependencies for the Node application in `All_India_Villages_API`:

   .. code-block:: bash

      cd All_India_Villages_API
      npm install

5. Install Python ETL dependencies if you plan to execute the ETL pipeline directly:

   .. code-block:: bash

      cd avi-etl-pipeline
      .venv\Scripts\python.exe -m pip install -r requirements.txt

Development Setup
-----------------

- Start the Next.js application with `npm run dev` from `All_India_Villages_API`.
- Start the Python ETL service with `python app.py` from `avi-etl-pipeline`.
- Build the documentation with `cd avi-docs && ..\.venv\Scripts\sphinx-build.exe -b html . _build/html`.

Production Setup
----------------

1. Provision a PostgreSQL-compatible database and Redis instance.
2. Set application environment variables for `DATABASE_URL`, `NEXTAUTH_URL`, and `NEXTAUTH_SECRET`.
3. Deploy the Next.js application to a container or cloud host that supports Socket.IO.
4. Deploy the Python ETL service behind an authenticated ingress for file upload.

Environment Variables
---------------------

Required environment variables for the Node application:

- `DATABASE_URL`
- `NEXTAUTH_SECRET`
- `NEXTAUTH_URL`
- `REDIS_URL` (optional)
- `RESEND_API_KEY` (optional)

Required environment variables for the Python ETL service:

- `DATABASE_URL`

Dependency Installation
-----------------------

- Node dependencies managed in `All_India_Villages_API/package.json`
- Python ETL dependencies managed in `avi-etl-pipeline/requirements.txt`
- Sphinx documentation dependencies managed in `avi-docs/requirements.txt`

Virtual Environment Setup
-------------------------

Use the repository-level `.venv` to isolate documentation dependencies from system Python.

Docker Setup
------------

This repository currently does not include a dedicated Dockerfile. Use the `apphosting.yaml` and platform-specific configuration for container deployment.
