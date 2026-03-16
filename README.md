# Personal Portfolio + Blog

This repository represents my personal developer space: a portfolio/blog project plus supporting experiments and automation work.

The goal is simple:
- Build in public
- Document what I learn
- Ship practical tools end-to-end

## What Recruiters Should Know

I use this project to demonstrate how I think and build:
- I iterate quickly and improve over time.
- I work across API integration, backend services, and automation.
- I prioritize clarity, maintainability, and real-world usefulness.

This is an actively evolving project, not a frozen template.

## Current Repository Layout

```text
.
|- main/          # Core Python experiments and API-based prototypes
|- discord_bot/   # Discord integration prototype
|- image.png      # Legacy screenshot from an earlier feature test
|- LICENSE
|- README.md
```

## Tech Used In This Repo

- Python
- FastAPI
- Uvicorn
- Requests
- Pydantic
- SQLite

## Running Locally

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn requests pydantic
   ```
3. Run one of the app entry points:
   ```bash
   uvicorn main.database:app --reload
   ```

## Project Direction

Planned improvements:
- Cleaner portfolio/blog front-end integration
- Better project organization and dependency management
- Stronger test coverage and CI workflow
- More polished documentation around architecture and decisions

## Contact

If you are a recruiter, engineer, or collaborator and want to connect:
- Open an issue in this repo
- Or reach out directly through my portfolio contact channels

---

Thanks for stopping by.
