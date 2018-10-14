import time
import ray


@ray.remote
def f():
    time.sleep(0.01)
    return ray.services.get_node_ip_address()


ray.init(redis_address='master:6379')

# Get a list of the IP addresses of the nodes that have joined the cluster.
ids = set(ray.get([f.remote() for _ in range(1000)]))
print(ids)
