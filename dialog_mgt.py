from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies import KerasPolicy, MemoizationPolicy, FallbackPolicy
#from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def train_dialogue(domain_file='domain.yml',
                   model_path='./models/dialogue',
                   training_data_file='stories.md'):
    fallback = FallbackPolicy(fallback_action_name='utter_unclear', core_threshold=0.2, nlu_threshold=0.6)
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), fallback])

    agent.train(
        training_data_file,
        epochs=300,
        batch_size=50,
        validation_split=0.2)

    agent.persist(model_path)
    return agent


def run_sonatel_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/vocalbot_nlu')
    agent = Agent.load('./models/dialogue', interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

    return agent


if __name__ == '__main__':
   # train_dialogue()
    run_sonatel_bot()