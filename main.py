from typing import Dict, List

from damage_detection_model.model import CarDamageDetectionModel
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request
import uvicorn


class AccidaModelInput(BaseModel):
    image_url: str


class AccidaModelOutputMeta(BaseModel):
    is_damage: bool
    polygon: List = Field(default_factory=list)


class AccidaModelOutput(BaseModel):
    image_url: str
    section: str
    damage_level: int
    damage_prob: float
    scratch: AccidaModelOutputMeta
    dent: AccidaModelOutputMeta
    spacing: AccidaModelOutputMeta


class Model:
    def inference(self, _input: ...) -> ...:
        pass


class AccidaModel(Model):
    def __init__(self, model):
        self.model = model

    def inference(self, _input: AccidaModelInput) -> AccidaModelOutput:
        inference_result, _, _ = self.model.do_inference(_input.image_url, "url")
        return AccidaModelOutput(**inference_result)


app = FastAPI()
app.model = AccidaModel(model=CarDamageDetectionModel(model_version="4.0.0"))


@app.post("/inference", response_model=AccidaModelOutput)
def inference(body: AccidaModelInput, request: Request):
    return request.app.model.inference(body)


if __name__ == '__main__':
    uvicorn.run(app)
