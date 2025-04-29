FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-devel AS cuda-base
ARG UNAME=user
ARG PUID=1000
ARG PGID=1000
# These are my habitual utilities; not required to run the demo.
# Clean them up if you want a smaller image.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    iproute2 \
    wget \
    build-essential \
    ca-certificates \
    ccache \
    sudo \
    cmake \
    curl \
    rsync \
    git \
    jq \
    gettext \
    ripgrep \
    fd-find \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/fdfind /usr/local/bin/fd \
    && /usr/sbin/update-ccache-symlinks \
    && mkdir /opt/ccache && ccache --set-config=cache_dir=/opt/ccache
# Configuring as a development environment; not just a runtime container.
# Running the demo as root would be fine.
RUN groupadd -g $PGID -o $UNAME \
    && useradd -m -u $PUID -g $PGID -o -s /bin/bash $UNAME \
    && usermod -aG sudo $UNAME
RUN mkdir -p /data/cache \
    && chown ${PUID}:${PGID} -R /usr/local /data /opt \
    && echo "${UNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${UNAME}

FROM cuda-base AS notagen
COPY . /src/
RUN ls /src/gradio && chown -R $PUID:$PGID /src

ENV FORCE_CUDA="1"
WORKDIR /src
USER $UNAME
RUN pip install --user --no-cache-dir accelerate optimum huggingface_hub[cli,torch] \
  && pip install --user --no-cache-dir -r requirements.txt

ENTRYPOINT ["/bin/bash"]
