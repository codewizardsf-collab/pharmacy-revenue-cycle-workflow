# Pharmacy Revenue Cycle Workflow

A healthcare workflow project for classifying pharmacy claim denials and routing follow-up work to the correct operational queue.

## Stack

Python, healthcare revenue cycle, claim routing

## Problem

Revenue cycle teams need consistent handling for prior authorizations, eligibility issues, coding errors, and manual review exceptions.

## Architecture

- claim_workflow.py maps denial reason codes to operational queues.
- Tests document prior authorization routing behavior.
- The domain is framework-light and ready for API or worker integration.

## Implemented Production Readiness

- CI compiles application and test modules.
- Routing outcomes use stable queue names.
- Denial classification is centralized for auditability.

## Run And Test

```powershell
python -m compileall app tests
```

## Quality Gates

- Project-specific GitHub Actions workflow included under .github/workflows/ci.yml.
- Generated build outputs and dependency folders are excluded through .gitignore.
- Tests and validation commands are intentionally small enough to run during code review.

## Production Extension Points

- Add claim lifecycle APIs.
- Add queue workers for denial follow-up.
- Add compliance export reports.

## Repository Hygiene

This repository contains original portfolio code only. It does not include employer source code, private resumes, generated binaries, local credentials, or large media files.

