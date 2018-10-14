FROM martisak/ray-demo
LABEL maintaner="Martin Isaksson"

COPY . /root/

RUN apt-get install -y swig python-pygame
RUN pip install box2d

CMD ["tensorboard",  "--logdir=/root/ray_results/", "--port=3000"]
