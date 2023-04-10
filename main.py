from model import Model
from environment import Environment
import torch.optim as optim
import torch

def main():
    env_size = 10
    m = Model(env_size, 2, 0.9, 0.5, -0.0001)
    env = Environment(env_size)

    optimizer = optim.Adam(m.parameters(), lr=0.01)

    for epoch in range(100000):
        for t in range(env_size):
            
            done = m.policy(env)
            
            if done == 1:
                break
        loss = m.train(optimizer)
        print(epoch, loss)
        env.reset()
        if epoch == 9: env.showcase = 0
    
    torch.save(m.net.state_dict(), "model.pt")
    


if __name__ == '__main__':
    main()
