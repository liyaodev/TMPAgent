FROM ubuntu:20.04
LABEL maintainer=liyaodev

# 设置非互动安装
ENV DEBIAN_FRONTEND=noninteractive

# Build Python Env
RUN apt-get clean && apt-get update && apt-get install -y \
    build-essential curl git htop man zip unzip i7z vim wget cmake unrar gcc g++ \
    automake software-properties-common libzmq5 libblas-dev liblapack-dev libpcre3 libpcre3-dev \
    bison byacc ffmpeg libsm6 libxext6 libxrender-dev zlib1g-dev lsof gdb nginx gettext tzdata libbz2-dev \
    iputils-ping libssl-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev \
    liblzma-dev libpython3.10 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install python-3.10
RUN wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tar.xz \
    && tar -xvf Python-3.10.10.tar.xz \
    && cd Python-3.10.10 \
    && ./configure \
    && make \
    && make install \
    && cd / && rm Python-3.10.10.tar.xz && rm -rf Python-3.10.10
RUN rm -rf /usr/local/bin/python && ln -s /usr/local/bin/python3.10 /usr/local/bin/python

# Install pip3
RUN wget https://bootstrap.pypa.io/pip/get-pip.py \
    && rm -rf /usr/bin/lsb_release \
    && python3 get-pip.py -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com \
    && rm /get-pip.py
RUN rm -rf /usr/local/bin/pip && ln -s /usr/local/bin/pip3 /usr/local/bin/pip

# 设置字符字符集
ENV LANG=C.UTF-8

# Set the time zone
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

# Set HOME variable
ENV HOME /www

# Set WorkSpace.
WORKDIR /www

# Define default command.
CMD ["/bin/bash"]
