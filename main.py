from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI(title="Sentiment Analysis API")
analyzer = SentimentIntensityAnalyzer()

class TextIn(BaseModel):
    text: str

class BatchIn(BaseModel):
    texts: List[str]

def classify(compound: float) -> str:
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"

def score_text(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    return {
        "text": text,
        "scores": scores,
        "label": classify(scores["compound"]),
    }

@app.get("/")
def root():
    return {"status": "ok", "service": "sentiment-analysis-api"}

@app.post("/analyze")
def analyze(payload: TextIn):
    return score_text(payload.text)

@app.post("/analyze/batch")
def analyze_batch(payload: BatchIn):
    return {"results": [score_text(t) for t in payload.texts]}
