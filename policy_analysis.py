from environment import GC
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.models.preprocessors import get_preprocessor
import torch
import numpy as np

NAME = '2-1000-10'

default_config = (
    PPOConfig()
    .framework("torch")
    .rollouts(create_env_on_local_worker=True)
    .debugging(seed=0, log_level="ERROR")
    .training(model={"fcnet_hiddens" : [32, 32]})
)

ppo = default_config.build(env=GC)

path = 'C:/Users/mikej/My Drive/5/Graph Research/Giant Component/models/' + NAME

ppo.restore(path)


# def query_policy(trainer, env, obs, actions=None):
#     policy = trainer.get_policy()
#     model = policy.model
#     prep = get_preprocessor(env.observation_space)(env.observation_space)
#     #print(prep.transform(obs))
#     model_output = model({"obs": torch.from_numpy(prep.transform(obs)[None])})[0]
#     dist = policy.dist_class(model_output, model)
#     if actions is None:
#         actions = [0,1]
#     probs = np.exp(dist.logp(torch.from_numpy(np.array(actions))).detach().numpy())
#     return probs
#
# print(query_policy(ppo, GC(), [45,12], actions=[0,1]))

print(ppo.compute_single_action([45, 12], explore=False))



