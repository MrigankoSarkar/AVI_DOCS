FAQ
===

This section provides answers to frequent questions about the project.

Q: What does the project deliver?
A: It provides a geo-hierarchical API for Indian administrative units and a separate ETL pipeline for ingesting MDDS-like village data.

Q: Is the ETL pipeline part of the main API app?
A: No. `avi-etl-pipeline` is a separate Python service that can be run independently.

Q: How are API credentials validated?
A: The Node API validates API keys using Redis first and then falls back to a persistent store if needed.

Q: How is schema management handled?
A: The canonical data model is expressed in `prisma/schema.prisma`, and runtime access uses `drizzle-orm`.
