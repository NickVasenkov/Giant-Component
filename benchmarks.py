from environment import GC_4



def run_random():
    env = GC_4()
    obs = env.reset()
    print(obs)
    done = False
    count = 0
    while not done:
        obs = env.step(0)
        print(obs)
        done = obs[2]
        count += 1
    print(count)
    return count

def run_product():
    env = GC_4()
    obs = env.reset()
    print(obs)
    done = False
    count = 0
    while not done:
        product1 = obs[0][0] * obs[0][1]
        product2 = obs[0][2] * obs[0][3]
        if product1 <= product2:
            obs = env.step(0)
        else:
            obs = env.step(1)
        print(obs)
        done = obs[2]
        count += 1
    print(count)
    return count

def run_sum():
    env = GC_4()
    obs = env.reset()
    print(obs)
    done = False
    count = 0
    while not done:
        sum1 = obs[0][0] + obs[0][1]
        sum2 = obs[0][2] + obs[0][3]
        if sum1 <= sum2:
            obs = env.step(0)
        else:
            obs = env.step(1)
        print(obs)
        done = obs[2]
        count += 1
    print(count)
    return count

run_sum()