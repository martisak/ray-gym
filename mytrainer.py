from ray.tune.registry import register_env
import gym
import numpy as np
import ray
import ray.tune as tune


def env_creator(env_config):
    return gym.make("LunarLanderContinuous-v2")


if __name__ == "__main__":
    register_env("lunarlander", env_creator)
    ray.init(redis_address='master:6379')

    config = {
        # "num_gpus": 0,
        # "num_gpus_per_worker": 0,
        # "num_workers": 3,
        # "num_envs_per_worker": 8,
        # "lambda": 0.98,
        "lr": tune.grid_search(
            np.logspace(-3, -5, 4).tolist())
        # "num_sgd_iter": tune.grid_search([2, 5, 30]),
        # "gamma": 0.9,
        # "batch_mode": "complete_episodes",
        # "horizon": 16,
    }

    all_trials = tune.run_experiments({
        "ppo1": {
            "run": "PPO",
            "env": "lunarlander",
            "stop": {
                "episode_reward_mean": 200,
                "time_total_s": 7200
            },
            "config": config,
            "checkpoint_freq": 10
        },
    })

    print(all_trials)
