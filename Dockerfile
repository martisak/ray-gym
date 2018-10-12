FROM martisak/ray-demo
LABEL maintaner="Martin Isaksson"

COPY . /root/

CMD ["tensorboard",  "--logdir=/root/ray_results/", "--port=3000"]
