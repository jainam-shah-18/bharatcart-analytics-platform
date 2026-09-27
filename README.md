# BharatCart Analytics Platform

An end-to-end analytics engineering platform for a fictional Indian e-commerce business.

## Project Overview

This project builds a modern data pipeline that ingests e-commerce data into Amazon S3, loads it into Snowflake, transforms it using dbt Core, validates data quality, and prepares business-ready datasets for Power BI.

## Architecture

Amazon S3 → Snowflake RAW → dbt STAGING → dbt INTERMEDIATE → dbt MARTS → Power BI

## Technology Stack

- AWS S3
- Snowflake
- dbt Core
- Python
- Apache Airflow
- Docker Compose
- Power BI
- GitHub Actions
- SQL and Python

## Current Status

### Completed

- S3 storage and IAM integration
- Snowflake storage integration
- Nine RAW tables
- Nine dbt staging models
- Four dbt intermediate models
- One dbt mart model
- Fifteen data-quality tests
- GitHub repository setup

### In Progress

- Python ingestion
- Airflow orchestration
- Docker Compose
- Power BI dashboard
- GitHub Actions CI/CD

## Data Layers

- **RAW:** Source data loaded from S3
- **STAGING:** Cleaned and standardized data
- **INTERMEDIATE:** Aggregated and enriched order data
- **MARTS:** Business-ready analytical datasets

## Key Validation

- 99,441 unique orders
- Zero duplicate rows in the enriched order model
- All 15 dbt tests passing

## Security

Credentials and environment files are excluded from Git. AWS identifiers and secrets should be replaced with placeholders in public documentation.