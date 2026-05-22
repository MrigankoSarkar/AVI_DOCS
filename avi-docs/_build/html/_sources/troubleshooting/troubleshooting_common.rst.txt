Common Issues
==============

Build Failures
--------------

- Ensure the Python virtual environment is active and documentation dependencies are installed.
- Confirm `avi-docs/conf.py` includes the correct `sys.path` entries.
- If `sphinx-build` fails, run `python -m pip install -r avi-docs/requirements.txt` again.

Runtime Issues
--------------

- For the Python ETL service, ensure `DATABASE_URL` is properly set and reachable.
- For the Node app, ensure `NEXTAUTH_URL` and `NEXTAUTH_SECRET` are configured.
- Validate that `REDIS_URL` is correct for Redis-backed caching and queueing.

Deployment Failures
-------------------

- If Socket.IO does not connect, verify the deployed platform supports WebSockets and raw HTTP.
- If database migrations fail, check the `DATABASE_URL` and the state of the Postgres schema.

Dependency Conflicts
--------------------

- Keep Node modules in sync with `All_India_Villages_API/package.json`.
- Keep Python ETL dependencies in sync with `avi-etl-pipeline/requirements.txt`.
