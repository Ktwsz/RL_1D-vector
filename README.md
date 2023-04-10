# Reinforcement Learning Model trained to reach end of a vector starting from index 0.

## Environment
One dimensional vector of size 10 filled with zeroes. Agent's postion is marked by 1 at corresponding index. Agent gets +1 reward if he moves to the right and 0 otherwise.

## Model
Implemented SARSA algorithm using TensorFlow, input is state of environment - 10 element vector, output is 2 element vector [R<sub>left</sub>, R<sub>right</sub>] where R is predicted reward for going in given direction

One hidden layer with 64 nodes, using ReLU for nonlinearity, TensorFlow's Adam optimizer.

## Dependencies required
TensorFlow

## Usage
To train and export model to file model.pt run main.py 

To see results run showcase.py
