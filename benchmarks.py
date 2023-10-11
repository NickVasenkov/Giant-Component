from environment import GC_4
import json
import numpy as np
import pandas as pd

# CHOOSE NAMES TO TEST (the number of nodes and size of the giant component
# have to be changed in the environment.py)
NAMES = ['2-1000-100', '4-1000-100']

PATH = 'C:/Users/mikej/My Drive/5/Graph Research/Giant Component/models/'

def run_random():
    env = GC_4()
    obs = env.reset()
    #print(obs)
    done = False
    count = 0
    while not done:
        obs = env.step(0)
        #print(obs)
        done = obs[2]
        count += 1
    #print(count)
    return count

def run_sum():
    env = GC_4()
    obs = env.reset()
    #print(obs)
    done = False
    count = 0
    while not done:
        sum1 = obs[0][0] + obs[0][1]
        sum2 = obs[0][2] + obs[0][3]
        if sum1 <= sum2:
            obs = env.step(0)
        else:
            obs = env.step(1)
        #print(obs)
        done = obs[2]
        count += 1
    #print(count)
    return count

def run_product():
    env = GC_4()
    obs = env.reset()
    #print(obs)
    done = False
    count = 0
    while not done:
        product1 = obs[0][0] * obs[0][1]
        product2 = obs[0][2] * obs[0][3]
        if product1 <= product2:
            obs = env.step(0)
        else:
            obs = env.step(1)
        #print(obs)
        done = obs[2]
        count += 1
    #print(count)
    return count

def run_benchmarks():
    for name in NAMES:
        print(name)
        with open(PATH + name + "/rewards_train.txt", "r") as fp:
            rewards_train = np.array(json.load(fp))
        averages_ai = np.sqrt(rewards_train * 2)
        steps_random = []
        averages_random = []
        steps_sum = []
        averages_sum = []
        steps_product = []
        averages_product = []

        for i in range(len(rewards_train)):
            steps_random.append(run_random())
            averages_random.append(np.mean(steps_random))
            steps_sum.append(run_sum())
            averages_sum.append(np.mean(steps_sum))
            steps_product.append(run_product())
            averages_product.append(np.mean(steps_product))

        zipped = list(zip(averages_ai,
                          averages_random, averages_sum, averages_product))

        data_frame = pd.DataFrame(zipped, columns =['AI', 'random',
                                                    'sum', 'product'])
        data_frame.to_csv(PATH + name + '/performance_df.csv')


run_benchmarks()

