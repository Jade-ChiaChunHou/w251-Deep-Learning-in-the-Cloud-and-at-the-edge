# HW11

## 1. What parameters did you change?
I've tried changing the **density_first_layer**,  **density_second_layer**, **num_epochs**, **batch_size** and **epsilon_min**.
## 2. What values did you try?
```
#######################
# Change these parameters to improve performance       
self.density_first_layer = 16, 24, 
self.density_second_layer = , 8, 12
self.num_epochs = 1, 2, 5, 10, 100
self.batch_size = 32, 64, 128
self.epsilon_min = 0.01, 0.001, 0.05

# epsilon will randomly choose the next action as either
# a random action, or the highest scoring predicted action
self.epsilon = 1.0
self.epsilon_decay = 0.995
self.gamma = 0.99

# Learning rate
self.lr = 0.001, 0.005, 0.0001
```
## 3. Did you try any other changes that made things better or worse?
- **density_first_layer**
- **density_second_layer**
- **num_epochs** : The number of epochs is a hyperparameter that defines the number times that the learning algorithm will work through the entire training dataset.
- **batch_size**: The batch size is a hyperparameter that defines the number of samples to work through before updating the internal model parameters.
- **epsilon_min**
When the **density_first_layer**,  **density_second_layer** bigger the rewards will increase, for example changing **density_first_layer** from 16 to 24 and **density_second_layer** 8 to 12. Increasing **num_epochs** the reward will also increase, but the training will incease.
## 4. Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?
## 5. Based on what you observed, what conclusions can you draw about the different parameters and their values?
## 6. What is the purpose of the epsilon value?
## 7. Describe "Q-Learning".
Q-learning is an off-policy / model-free reinforcement learning algorithm that seeks to find the best action to take given the current state. It’s considered off-policy because the Q-learning function learns from actions that are outside the current policy, like taking random actions, and therefore a policy isn’t needed. More specifically, Q-learning seeks to learn a policy that maximizes the total reward.


```
$$Q^new(s_t, a_t)$$
```
