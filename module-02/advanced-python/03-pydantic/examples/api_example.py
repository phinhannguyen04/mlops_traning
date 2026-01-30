"""API Integration Example

This module demonstrates using Pydantic for API request/response models.
"""

from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class PredictionRequest(BaseModel):
    """ML model prediction request."""
    features: list[float] = Field(min_length=1, max_length=100)
    model_name: Literal["iris", "mnist", "sentiment"] = "iris"
    return_probabilities: bool = False


class PredictionResponse(BaseModel):
    """ML model prediction response."""
    prediction: str | int
    confidence: float = Field(ge=0, le=1)
    model_version: str
    timestamp: datetime = Field(default_factory=datetime.now)


class TrainRequest(BaseModel):
    """Model training request."""
    dataset_path: str
    model_type: Literal["random_forest", "svm", "neural_net"]
    hyperparameters: dict[str, float | int | str]
    validation_split: float = Field(default=0.2, ge=0, le=1)


class TrainResponse(BaseModel):
    """Model training response."""
    job_id: str
    status: Literal["queued", "training", "completed", "failed"]
    metrics: dict[str, float] | None = None


def simulate_api() -> None:
    """Simulate API with Pydantic models."""
    print("=== API Request Validation ===")

    # Valid prediction request
    request = PredictionRequest(
        features=[5.1, 3.5, 1.4, 0.2],
        model_name="iris"
    )
    print(f"Request validated: {request.features}")

    # Simulate response
    response = PredictionResponse(
        prediction="setosa",
        confidence=0.95,
        model_version="1.0.0"
    )
    print(f"Response: {response.model_dump_json()}")

    print("\n=== Training Request ===")

    train_req = TrainRequest(
        dataset_path="/data/train.csv",
        model_type="random_forest",
        hyperparameters={"n_estimators": 100, "max_depth": 10}
    )
    print(f"Training {train_req.model_type}")
    print(f"Params: {train_req.hyperparameters}")


def main() -> None:
    """Run API simulation."""
    simulate_api()


if __name__ == "__main__":
    main()
