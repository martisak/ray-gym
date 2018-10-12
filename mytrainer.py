import ray
from ray.tune.registry import register_env
import ray.tune as tune


def env_creator(env_config):
    import gym
    return gym.make("CartPole-v0")  # or return your own custom env


if __name__ == "__main__":
    register_env("cartpole", env_creator)
    ray.init()

    # gpu_fraction in newer versions

    config = {
        # "num_gpus": 0,
        # "num_gpus_per_worker": 0,
        # "num_workers": 3,
        # "num_envs_per_worker": 8,
        # "lambda": 0.98,
        # "sgd_stepsize": tune.grid_search(
        #     np.logspace(-3, -4, 2).tolist()),
        # "num_sgd_iter": tune.grid_search([2, 5, 30]),
        # "gamma": 0.9,
        # "batch_mode": "complete_episodes",
        # "horizon": 16,
    }

    all_trials = tune.run_experiments({
        "apex_ddpg": {
            "run": "APEX_DDPG",
            "env": "cartpole",
            # "stop": {
            #     "episode_reward_mean": 1000,
            #     "time_total_s": 7200
            # },
            "config": config,
            "checkpoint_freq": 10
        },
    })

    print(all_trials)
