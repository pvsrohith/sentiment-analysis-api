# sentiment-analysis-api

A FastAPI service that scores text sentiment (positive, negative, or neutral) using VADER sentiment analysis, with support for single and batch requests.

## Features

- Single text sentiment scoring with compound, positive, negative, and neutral scores
- Batch analysis endpoint for scoring multiple texts in one request
- Simple label classification (positive, negative, neutral) based on compound score thresholds
- Auto-generated interactive docs via FastAPI/Swagger

## Tech Stack

Python, FastAPI, vaderSentiment, Pydantic

## Getting Started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs for interactive API docs.

## API Overview

- `GET /` - health check
- `POST /analyze` - analyze sentiment of a single text, returns scores and label
- `POST /analyze/batch` - analyze sentiment for a list of texts
- 
