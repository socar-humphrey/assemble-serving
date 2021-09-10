import os
from typing import Dict

from bentoml import BentoService, api, artifacts, env
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.pickle import PickleArtifact
from bentoml.utils import cloudpickle

from main import app

example_input = {
    "image_url": "https://d1ot6qrzkadyo.cloudfront.net/000138/13895/202107/07e50201-73ba-4b64-a7bb-80f166d5f273.jpg"
}

model_zip_path = os.path.join(os.path.dirname(__file__), "damage_detection_model-4.0.2.tar.gz")


@env(infer_pip_packages=True, zipimport_archives=["damage_detection_model-4.0.2.tar.gz"])
@artifacts([PickleArtifact('model')])
class AccidaServiceV4(BentoService):
    @api(input=JsonInput(http_input_example=example_input))
    def predict(self, body: Dict):
        return self.artifacts.model.inference(body)


if __name__ == '__main__':
    accida_service_v4 = AccidaServiceV4()
    with open('model.pkl', 'wb') as f:
        cloudpickle.dump(app.model, f)
    with open('model.pkl', 'rb') as f:
        model_pickled = cloudpickle.load(f)
    accida_service_v4.pack('model', model_pickled)
    saved_path = accida_service_v4.save()
