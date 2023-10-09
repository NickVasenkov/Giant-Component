from environment import GC
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.utils import check_env
import matplotlib.pyplot as plt
import json

# CHANGE THREE THINGS:
# 1) CHANGE NAME
NAME = '2-1000-10'
default_config = (
    PPOConfig()
    .framework("torch")
    .rollouts(create_env_on_local_worker=True)
    .debugging(seed=0, log_level="ERROR")
    .training(model={"fcnet_hiddens": [32, 32]})
)
# 2) CHANGE ENVIRONMENT HERE
check_env(GC())
# 3) AND CHANGE ENVIRONMENT HERE
ppo = default_config.build(env=GC)

path = 'C:/Users/mikej/My Drive/5/Graph Research/Giant-Component/models/' + NAME
rewards_train = []
rewards_evaluation = []

for i in range(3):
    train_info = ppo.train()
    reward_train = train_info['episode_reward_mean']
    print(i)
    print(reward_train)
    rewards_train.append(reward_train)
    print(train_info)
    if i != 0 and i % 10 == 0:
        with open(path + "/rewards_train.txt", "w") as fp:
            json.dump(rewards_train, fp)
        reward_evaluation = ppo.evaluate()["evaluation"]["episode_reward_mean"]
        print("Evaluation: {}".format(reward_evaluation))
        rewards_evaluation.append(reward_evaluation)

        print(train_info)

checkpoint_dir = ppo.save(path)
print(checkpoint_dir)
with open(path + "/rewards_train.txt", "w") as fp:
    json.dump(rewards_train, fp)
reward_evaluation = ppo.evaluate()["evaluation"]["episode_reward_mean"]
rewards_evaluation.append(reward_evaluation)
with open(path + "/rewards_evaluation.txt", "w") as fp:
    json.dump(rewards_evaluation, fp)
with open(path + "/iterations_counter.txt", "w") as fp:
    json.dump(i, fp)

plt.figure(figsize=(5, 3))
plt.plot(rewards_train)
plt.xlabel("training iteration")
plt.ylabel("steps")
plt.show()