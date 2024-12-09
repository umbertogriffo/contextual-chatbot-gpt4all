from enum import Enum

from bot.model.settings.llama import Llama31Settings, Llama32Settings
from bot.model.settings.openchat import OpenChat35Settings, OpenChat36Settings
from bot.model.settings.phi import Phi31Settings, Phi35Settings
from bot.model.settings.stablelm_zephyr import StableLMZephyrSettings
from bot.model.settings.starling import StarlingSettings


class ModelType(Enum):
    ZEPHYR = "zephyr"
    MISTRAL = "mistral"
    DOLPHIN = "dolphin"
    STABLELM_ZEPHYR = "stablelm-zephyr"
    OPENCHAT_3_5 = "openchat-3.5"
    OPENCHAT_3_6 = "openchat-3.6"
    STARLING = "starling"
    PHI_3_1 = "phi-3.1"
    PHI_3_5 = "phi-3.5"
    LLAMA_3_1 = "llama-3.1"
    LLAMA_3_2 = "llama-3.2"


SUPPORTED_MODELS = {
    ModelType.STABLELM_ZEPHYR.value: StableLMZephyrSettings,
    ModelType.OPENCHAT_3_5.value: OpenChat35Settings,
    ModelType.OPENCHAT_3_6.value: OpenChat36Settings,
    ModelType.STARLING.value: StarlingSettings,
    ModelType.PHI_3_1.value: Phi31Settings,
    ModelType.PHI_3_5.value: Phi35Settings,
    ModelType.LLAMA_3_1.value: Llama31Settings,
    ModelType.LLAMA_3_2.value: Llama32Settings,
}


def get_models():
    return list(SUPPORTED_MODELS.keys())


def get_model_settings(model_name: str):
    model_settings = SUPPORTED_MODELS.get(model_name)

    # validate input
    if model_settings is None:
        raise KeyError(model_name + " is a not supported model")

    return model_settings
