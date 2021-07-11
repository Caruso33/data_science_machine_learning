import random
from collections import defaultdict

import numpy as np


class Agent:
    def __init__(self, nA=6, eps=1.0, alpha=0.5, gamma=0.5, decay=0.6, min_eps=0.):
        """Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.eps = eps
        self.alpha = alpha
        self.gamma = gamma

        self.decay = decay
        self.min_eps = min_eps

    def decay_epsilon(self):
        self.eps *= self.decay

        self.eps = max(self.eps, self.min_eps)

    def epsilon_greedy(self, state):
        """Selects epsilon-greedy action for supplied state.

        Params
        ======
            Q (dictionary): action-value function
            state (int): current state
            nA (int): number actions in the environment
            eps (float): epsilon
        """
        if random.random() > self.eps:  # select greedy action with probability epsilon
            return np.argmax(self.Q[state])

        # otherwise, select an action randomly
        return random.choice(np.arange(self.nA))

    def update_Q_sarsa(self, state, action, reward, next_state=None, next_action=None):
        """Returns updated Q-value for the most recent experience."""

        # estimate in Q-table (for current state, action pair)
        current = self.Q[state][action]

        # get value of state, action pair at next time step
        Qsa_next = self.Q[next_state][next_action] if next_state is not None else 0

        # construct TD target
        target = reward + (self.gamma * Qsa_next)

        # get updated value
        new_value = current + (self.alpha * (target - current))

        return new_value

    def update_Q_sarsamax(self, state, action, reward, next_state=None):
        """Returns updated Q-value for the most recent experience."""

        # estimate in Q-table (for current state, action pair)
        current = self.Q[state][action]

        # value of next state
        Qsa_next = np.max(self.Q[next_state]) if next_state is not None else 0

        # construct TD target
        target = reward + (self.gamma * Qsa_next)

        # get updated value
        new_value = current + (self.alpha * (target - current))

        return new_value

    def update_Q_expsarsa(self, state, action, reward, next_state=None):
        """Returns updated Q-value for the most recent experience."""

        # estimate in Q-table (for current state, action pair)
        current = self.Q[state][action]

        # current policy (for next state S')
        policy_s = np.ones(self.nA) * self.eps / self.nA
        # greedy action
        policy_s[np.argmax(self.Q[next_state])] = 1 - self.eps + (self.eps / self.nA)

        # get value of state at next time step
        Qsa_next = np.dot(self.Q[next_state], policy_s)

        # construct target
        target = reward + (self.gamma * Qsa_next)

        # get updated value
        new_value = current + (self.alpha * (target - current))

        return new_value

    def select_action(self, state):
        """Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # return np.random.choice(self.nA)

        # epsilon-greedy action selection
        action = self.epsilon_greedy(state)

        return action

    def step(self, state, action, reward, next_state, done):
        """Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        # self.Q[state][action] += 1

        # decrease exploration with each episode
        self.decay_epsilon()

        # sarsa, not possible to implement here because `monitor.py` doesn't
        # provide us the next_action
        # Q[state][action] = self.update_Q_sarsa(
        #     state, action, reward, next_state, next_action
        # )

        # q-learning // sarsamax
        # self.Q[state][action] = self.update_Q_sarsamax(
        #     state, action, reward, next_state
        # )

        # expected sarsa
        self.Q[state][action] = self.update_Q_expsarsa(
            state, action, reward, next_state
        )
