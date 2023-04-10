from environment import Environment
from model import Model
from time import sleep
import torch

env_size = 10

m = Model(env_size, 2, 0.9, 0.0, -0.000001)
m.net.load_state_dict(torch.load("model.pt"))


env = Environment(env_size)
env.set_showcase()

for t in range(5*env_size):
    done = m.policy(env)
    if done == 1:
        break
    sleep(1)
