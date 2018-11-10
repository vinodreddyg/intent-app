from typing import List, Union
import numpy as np

from deeppavlov.core.common.errors import ConfigError
from deeppavlov.core.common.registry import register
from deeppavlov.core.common.log import get_logger
from deeppavlov.core.models.component import Component

@register('proba2dict')
class Proba2Dict(Component):
    def __init__(self, classes, **kwargs):
        self.classes = list(classes)
    
    def get_dict(self, proba):
        return dict(zip(self.classes, proba))
    
    def __call__(self, data, *args, **kwargs):
        return [self.get_dict(proba) for proba in data]