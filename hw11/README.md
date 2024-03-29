# HW11

## 1. What parameters did you change?
I've tried changing the **density_first_layer**,  **density_second_layer**, **num_epochs**, **batch_size** and **epsilon_min**, **lr**.

## 2. What values did you try?
```
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
- When the **density_first_layer**,  **density_second_layer** bigger the rewards will increase, for example changing **density_first_layer** from 16 to 24 and **density_second_layer** 8 to 12. Increasing **num_epochs** the reward will also increase, but the training time will also incease.
- When changing the **batch_size** to 32 or 128, the score become worse.
 
## 4. Did they improve or degrade the model? Did you have a test run with 100% of the scores above 200?
By changing the value of the **density_first_layer**,  **density_second_layer**, **num_epochs** the model seems to be improve, but haven't improve to scores above 200.

No, I didn't had a test run with 100% of the scores above 200.

## 5. Based on what you observed, what conclusions can you draw about the different parameters and their values?
The meaning if the hyperparameter:
- **density_first_layer**: The neuron number of first layer.
- **density_second_layer**: The neuron number of second layer.
- **num_epochs** : The number of epochs is a hyperparameter that defines the number times that the learning algorithm will work through the entire training dataset.
- **batch_size**: The batch size is a hyperparameter that defines the number of samples to work through before updating the internal model parameters.


To conclude, in this example when increse the **num_epochs** the score will improve. That means the times that model run though the training set will increase. So the score will likely improve by increasing the number of the epochs. Increase the **density_first_layer**,  **density_second_layer** the score also improve. When the **batch_size** = 64 seems to have the better score. Also decrease the **lr** the score will improve, but it will also increase the training time.

## 6. What is the purpose of the epsilon value?
The purpose of the epsilon value is to balance the exploration / exploitation in the Q-learning.

There are two ways for Q-learning to make update. The first way is **exploiting** which use the q-table as a reference and view all possible actions for a given state. It will select the action with max value base on the available information we had.

The sencond way **exploring**  is to take the action randomly without selecting the action based on the max reward. This is important because allows the Q-learning to discover new states.

If set the epsilon = 0.2, that means we want to explore 20% and exploit 80%.

## 7. Describe "Q-Learning".
Q-learning is an off-policy / model-free reinforcement learning algorithm that seeks to find the best action to take given the current state. It’s considered off-policy because the Q-learning function learns from actions that are outside the current policy, like taking random actions, and therefore a policy isn’t needed. More specifically, Q-learning seeks to learn a policy that maximizes the total reward.

<img width="615" alt="截圖 2020-08-02 下午4 11 46" src="https://user-images.githubusercontent.com/50607384/89118780-10065c00-d4db-11ea-9dcc-afd87ffc21f4.png">

## IBM Object Storge tarining episode link:
http://s3.ap.cloud-object-storage.appdomain.cloud/w251jade/episode340.mp4
