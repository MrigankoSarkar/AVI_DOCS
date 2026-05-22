Deployment Pipeline
===================

The repository is prepared for GitHub publishing and ReadTheDocs documentation deployment.

CI/CD Build
-----------

A GitHub Actions workflow is provided at `.github/workflows/docs.yml` to validate the documentation build:

- `actions/checkout@v4`
- `actions/setup-python@v5`
- install requirements from `avi-docs/requirements.txt`
- build the documentation with `sphinx-build`

ReadTheDocs Configuration
-------------------------

ReadTheDocs is configured by `.readthedocs.yaml` at repository root.
It installs documentation dependencies from `avi-docs/requirements.txt` and runs `sphinx-build -b html . _build/html`.

Documentation Publishing
------------------------

1. Push changes to the repository.
2. Connect the repository to ReadTheDocs if not already configured.
3. Set the build command to use the repository root configuration.

Containerization
----------------

The project does not provide a production Dockerfile in the repository.
For container deployments, build a container around:

- the Next.js application in `All_India_Villages_API`
- the Python ETL service in `avi-etl-pipeline`
- a shared PostgreSQL and Redis backend

Infrastructure Setup
--------------------

- Use `apphosting.yaml` settings for host platform resource recommendations.
- Ensure a platform with raw HTTP server support for Socket.IO if the main application uses real-time events.
