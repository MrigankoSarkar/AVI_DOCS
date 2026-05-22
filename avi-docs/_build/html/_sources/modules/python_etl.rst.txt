Python ETL Module Reference
===========================

This section documents the Python ETL pipeline modules in `avi-etl-pipeline`.

The single entrypoint is `app.py`, which provides:

- dataset loading with `load_dataset()`
- dataset cleaning with `clean_dataset_dataframe()`
- schema creation with `create_tables()`
- file upload endpoint logic for `/upload` and `/upload-to-db`
- transactional database writes via SQLAlchemy `engine.begin()`
- a raw audit table `village_data`

Autodoc Example
---------------

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

ETL Behavior
------------

- Input formats: CSV, XLS, XLSX
- Required fields are mapped to canonical MDDS names
- Duplicate rows are deduplicated by `village_code`
- Postgres tables are created if missing
- Hierarchical inserts are performed for country, state, district, subdistrict, and village
- Raw payloads are persisted in `village_data`
