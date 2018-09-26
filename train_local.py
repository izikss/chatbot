from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies import KerasPolicy, MemoizationPolicy, FallbackPolicy
#from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    training_data_file = 'stories.md'
    model_path = './models/dialogue'
    fallback = FallbackPolicy(fallback_action_name='utter_unclear', core_threshold=0.2, nlu_threshold=0.6)
    agent = Agent('domain.yml', policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback])

    agent.train(
        training_data_file,
        epochs=400,
        batch_size=20,
        validation_split=0.1)

    agent.persist(model_path)