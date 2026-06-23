# Automated Data Pipeline with CI/CD

## Overview
Containerized data processing pipeline with automated 
CI/CD via GitHub Actions. Built as a demonstration of 
DevOps and automation principles applied to data engineering.

## Tech Stack
- Python 3.10 — pipeline logic and data processing
- Docker — containerized execution
- GitHub Actions — CI/CD: automated test and build on every push
- pytest — automated testing

## Pipeline Steps
1. Generate simulated sensor/event data
2. Validate and clean events
3. Aggregate by event type
4. Output summary JSON

## CI/CD Flow
Push to main → Tests run automatically → 
Docker image built → Pipeline executes in container → 
Output verified

## How to Run Locally
docker-compose up --build

## How to Run Tests
pytest test_process.py -v

## Relevance to Robotics/Industrial Automation
Event types simulate industrial sensor readings 
(sensor_read, motor_command, status_update) — 
reflecting interest in robotics and embedded systems domains.