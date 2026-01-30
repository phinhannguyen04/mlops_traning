"""Exercise 5 Solution: API Integration"""
from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
    features: list[float]
    model_name: Literal["iris", "mnist"] = "iris"

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float = Field(ge=0, le=1)

def main():
    req = PredictionRequest(features=[5.1, 3.5, 1.4, 0.2])
    resp = PredictionResponse(prediction="setosa", confidence=0.95)
    print(f"Request: {req}")
    print(f"Response: {resp.model_dump_json()}")

if __name__ == "__main__":
    main()
