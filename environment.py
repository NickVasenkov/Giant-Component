import gymnasium as gym
import graph
import rustworkx as rx
import numpy as np

# This class returns as an observation sizes of components that will appear
# after creating edges.
# The corresponding observations are in folders that start with "2-"
class GC(gym.Env):
    def __init__(self, env_config=None):
        # CHANGE THE NUMBER OF NODES
        self.node_number = 1000
        # IN ORDER TO CHANGE THE SIZE OF THE GIANT COMPONENT,
        # WE NEED TO CHANGE NUMBERS IN self.observation_space
        # AND IN FUNCTION done
        self.observation_space = gym.spaces.Box(low=2, high=round(self.node_number / 4),
                                                shape=(2,), dtype=np.int64)
        self.action_space = gym.spaces.Discrete(2)

    def reset(self, *, seed=None, options=None):
        self.G = graph.initiate_graph(self.node_number)
        self.biggest_component = 0
        self.nodes_to_choose = graph.choose_nodes(self.G)
        self.sizes = graph.calculate_sizes(self.G, self.nodes_to_choose)
        self.total_reward = 0
        return self._get_obs(), {}

    def _get_obs(self):
        return self.sizes

    def reward(self):
        return self.total_reward

    def done(self):
        return self.biggest_component >= self.node_number / 10

    def step(self, action):
        if action in [0, 1]:
            self.G.add_edge(self.nodes_to_choose[action * 2],
                            self.nodes_to_choose[action * 2 + 1], None)
            self.biggest_component = max(self.biggest_component,
                                         self.sizes[action])
        else:
            raise ValueError("Action must be in {0,1}")
        self.nodes_to_choose = graph.choose_nodes(self.G)
        self.sizes = graph.calculate_sizes(self.G, self.nodes_to_choose)
        self.total_reward += 1
        # Return observation/reward/done
        return self._get_obs(), self.reward(), self.done(), False, {}

# This class returns as an observation 4 sizes of the components of the four
# nodes in 2 pairs.
# If one of the pairs is in the same component, the corresponding sizes
# will be zeros.
# The corresponding observations are in folders that start with "4-"
class GC_4(gym.Env):
    def __init__(self, env_config=None):
        # CHANGE THE NUMBER OF NODES
        self.node_number = 1000
        # CHANGE THE SIZE OF THE GIANT COMPONENT
        self.giant_size = 100
        self.observation_space = gym.spaces.Box(low=0,
                                                high=self.giant_size * 2,
                                                shape=(4,), dtype=np.int64)
        self.action_space = gym.spaces.Discrete(2)

    def reset(self, *, seed=None, options=None):
        self.G = graph.initiate_graph(self.node_number)
        self.biggest_component = 0
        self.nodes_to_choose = graph.choose_nodes(self.G)
        self.sizes = graph.calculate_sizes_4(self.G, self.nodes_to_choose)
        self.total_reward = 0
        return self._get_obs(), {}

    def _get_obs(self):
        return self.sizes

    def reward(self):
        return self.total_reward

    def done(self):
        return self.biggest_component >= self.giant_size

    def step(self, action):
        if action in [0, 1]:
            self.G.add_edge(self.nodes_to_choose[action * 2],
                            self.nodes_to_choose[action * 2 + 1], None)
            new_component = len(rx.node_connected_component(self.G,
                            self.nodes_to_choose[action * 2]))
            self.biggest_component = max(self.biggest_component,
                                         new_component)
        else:
            raise ValueError("Action must be in {0,1}")
        self.nodes_to_choose = graph.choose_nodes(self.G)
        self.sizes = graph.calculate_sizes_4(self.G, self.nodes_to_choose)
        self.total_reward += 1
        # Return observation/reward/done
        return self._get_obs(), self.reward(), self.done(), False, {}


#
# env = GC_4()
#
# print(env.reset())
# done = False
# count = 0
# while not done:
#     step = env.step(0)
#     print(step)
#     done = step[2]
#     count += 1
# print(count)

