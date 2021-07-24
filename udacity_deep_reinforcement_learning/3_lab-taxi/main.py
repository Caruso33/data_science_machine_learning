import os
import pickle
from itertools import product

import gym

from agent import Agent
from monitor import interact


def custom_grid_search(hyperparameters, run_interaction, on_results):

    combinations = [hyperparameters[hp] for hp in hyperparameters]

    cartesian_product = product(*combinations)

    param_sets = [
        {k: v for k, v in zip(hyperparameters.keys(), prod)}
        for prod in cartesian_product
    ]

    no_runs = len(param_sets)
    print("Number of different runs", no_runs)

    results = []

    best_rewards = 0
    best_score = 0
    best_param_set = None

    for i_run, param_set in enumerate(param_sets):
        print("Number of run", i_run, "//", no_runs)

        agent = Agent(**param_set)

        avg_rewards, best_avg_reward = run_interaction(agent)

        if best_avg_reward > best_score:
            best_rewards = avg_rewards
            best_score = best_avg_reward
            best_param_set = param_set

        print("Params", param_set, "Score", best_avg_reward, "\n")

        results.append(
            dict(
                param_set=param_set,
                avg_rewards=avg_rewards,
                best_avg_reward=best_avg_reward,
            )
        )

    # print("best_rewards", best_rewards)

    print("best_score", best_score)
    print("best_param_set", best_param_set)

    if callable(on_results):
        on_results(results)


def get_file_methods(filename, remove_pickle_if_present):
    terminate_program = False

    if remove_pickle_if_present:
        if os.path.exists(filename):
            os.remove(filename)

            terminate_program = True

    if os.path.exists(filename):
        with open(filename, "rb") as outputfile:
            results = pickle.load(outputfile)

            best_avg_reward = max(results, key=lambda x: x["best_avg_reward"])
            print("best_avg_reward", best_avg_reward)

            terminate_program = True

    def write_results(results):
        with open(filename, "wb") as outputfile:
            pickle.dump(results, outputfile)

    return terminate_program, write_results


def run_grid_search():
    # default kwargs
    # eps=1.0, alpha=0.5, gamma=0.5, decay=0.6, min_eps=0.

    filename = "results.pkl"

    remove_pickle_if_present = False

    terminate_program, write_results = get_file_methods(
        filename, remove_pickle_if_present
    )
    if terminate_program:
        return

    hyperparameters = {
        "eps": [1.0, 0.8, 0.6],
        "alpha": [0.3, 0.5, 0.7, 0.9, 0.99],
        "gamma": [0.3, 0.5, 0.7, 0.9, 0.99],
        "decay": [0.3, 0.5, 0.7, 0.9, 0.99],
        "min_eps": [0.0, 0.05, 0.1, 0.3],
    }

    num_episodes = 20000

    env = gym.make("Taxi-v2")

    def run_interaction(agent):
        avg_rewards, best_avg_reward = interact(env, agent, num_episodes=num_episodes)

        return avg_rewards, best_avg_reward

    def on_results(results):
        write_results(results)

    custom_grid_search(hyperparameters, run_interaction, on_results)


run_grid_search()
