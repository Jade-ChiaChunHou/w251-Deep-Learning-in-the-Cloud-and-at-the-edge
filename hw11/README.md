# HW11

## 1. What parameters did you change?
I've tried changing the **density_first_layer**,  **density_second_layer**, **num_epochs**, **batch_size** and **epsilon_min**.
## 2. What values did you try?
```
 self.density_first_layer = 16, 24, 
        self.density_second_layer = , 8, 12
        self.num_epochs = 1, 2, 5, 10, 100
        self.batch_size = 32, 64, 128
        self.epsilon_min = 0.01, 0.001, 0.05
```
## 3. Did you try any other changes that made things better or worse?
When the **density_first_layer**,  **density_second_layer** bigger the rewards will increase, for example changing **density_first_layer** from 16 to 24 and **density_second_layer** 8 to 12.
## 4. Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?
## 5. Based on what you observed, what conclusions can you draw about the different parameters and their values?
## 6. What is the purpose of the epsilon value?
## 7. Describe "Q-Learning".
Q-learning is a model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances. It does not require a model (hence the connotation "model-free") of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations.
```
$$Q^new(s_t, a_t)$$
```
