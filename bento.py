from typing import Dict

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.pickle import PickleArtifact

from main import app

example_input = {
    "image_url": "https://d1ot6qrzkadyo.cloudfront.net/000138/13895/202107/07e50201-73ba-4b64-a7bb-80f166d5f273.jpg"
}


@artifacts([PickleArtifact('model')])
class AccidaServiceV4(BentoService):
    @api(input=JsonInput(http_input_example=example_input))
    def predict(self, body: Dict):
        return self.artifacts.model.inference(body)


if __name__ == '__main__':
    accida_service_v4 = AccidaServiceV4()
    accida_service_v4.pack(app.model)
    saved_path = accida_service_v4.save()
