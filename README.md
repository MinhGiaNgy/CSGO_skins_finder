# CS:GO / CS2 Skin Indexer

An API-driven indexer that pulls skin market data from Steam Community Market, stores it in SQLite, and exposes it for fast lookup (including StatTrak filtering and Discord bot integration).

## Overview

This project is built to solve one problem well:
- Keep a local, queryable index of CS skins with price + listing metadata.

It includes:
- A FastAPI sync service to ingest market data
- A SQLite-backed local index
- Search utilities for partial-name matching
- Discord bot commands for chat-based lookups

## Features

- Bulk ingestion from Steam Community Market (`appid=730`)
- Local persistence in `steamskinsdata.db`
- Search by skin name tokens
- StatTrak and non-StatTrak filtering
- Discord commands:
  - `.search <skin name>`
  - `.searchst <skin name>`

## Project Structure

```text
.
|- main/
|  |- database.py   # FastAPI + Steam ingestion + SQLite sync endpoint
|  |- bot1.py       # Discord bot commands backed by SQLite lookups
|  |- OOP.py        # In-memory fetch/search prototype
|  |- main.py       # Archived experimental code
|  |- poems.py      # Legacy experiment (not part of skin indexer flow)
|- discord_bot/
|  |- main.py       # Earlier standalone API test script
|- image.png
|- LICENSE
|- README.md
```

## Tech Stack

- Python
- FastAPI
- Uvicorn
- SQLite
- Pydantic
- Requests
- discord.py

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install fastapi uvicorn requests pydantic discord.py
```

3. Start the sync API:

```bash
uvicorn main.database:app --reload
```

4. Trigger a market sync:

```bash
curl -X POST http://127.0.0.1:8000/skinsync
```

This populates `steamskinsdata.db` with current Steam market snapshot data.

## Discord Bot Usage

The bot implementation is in `main/bot1.py`.

Supported commands:
- `.search ak-47 redline`
- `.searchst ak-47 redline`

Before running:
- Replace the placeholder token in `main/bot1.py`
- Ensure `steamskinsdata.db` exists and has been synced

## Data Model

Indexed fields:
- `name`
- `sell_price`
- `sell_listings`

## Known Limitations

- Steam endpoint rate limits can affect sync reliability.
- SQL query strings are currently built directly in code and should be parameterized for safety.
- Repository includes legacy/experimental files from earlier iterations.

## Why This Project Matters

This project demonstrates practical backend engineering skills:
- External API integration at scale
- Data ingestion and local indexing
- API + bot interfaces on top of shared storage
- Iterative delivery from prototype to usable tooling
