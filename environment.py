class Environment():
    def __init__(self, size):
        self.size = size
        self.showcase = 0
        self.reset()

    def reset(self):
        self.position = 0
        self.vector = [0 for i in range(self.size) ]
        self.vector[self.position] = 1

    def action(self, action):
        #computes reward, returns reward and new state
        self.update_position(action)
        reward = 0
        done = 0

        if self.position ==self.size-1:
            reward = 1
            done = 1
        
        if self.showcase: self.show_state()
        return reward, self.vector, done

    def get_state(self):
        return self.vector
    
    def get_dist(self):
        return self.size-1-self.position
    
    def update_position(self, action):
        self.vector[self.position] = 0
        if action == 1: 
            self.position = min(self.size-1, self.position+1)
        else: 
            self.position = max(0, self.position-1)
        self.vector[self.position] = 1

    def set_showcase(self):
        self.showcase = 1

    def show_state(self):
        print(self.get_state())

        