Developer Workflow
===================

Source Code Structure
---------------------

The repository contains two distinct software systems:

- `All_India_Villages_API/` — the main Next.js frontend and backend application.
- `avi-etl-pipeline/` — the Python ETL service.

Coding Standards
----------------

- Use TypeScript for frontend and backend application code.
- Keep server-side logic in `src/lib` and route-specific behavior in `src/app/api`.
- Keep Python ETL logic isolated in `avi-etl-pipeline/app.py`.

Branching Strategy
------------------

Use feature branches for new capabilities and protected branches for release candidates.
A suggested workflow is:

- `main` / `master` for release-ready production code
- `develop` for staging integration
- `feature/*` for new features and bug fixes

Debugging Guide
---------------

- Use `npm run dev` in `All_India_Villages_API` to launch the Next.js dev server.
- Use browser DevTools and network inspection on API calls.
- For Python, run `python app.py` and inspect Flask logs.

Logging Guide
-------------

- Next.js server errors are surfaced in the console.
- The Python ETL service logs using the `logging` module at `INFO` and `ERROR` levels.

Testing Workflow
----------------

This repository does not currently include dedicated test suites.
Add unit and integration tests to the `All_India_Villages_API` and `avi-etl-pipeline` codebases for future maintainability.
