FROM ubuntu:24.04

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
ENV TZ="America/Los_Angeles"
ENV DEBIAN_FRONTEND=noninteractive

# Install Node.js for Jupyter extensions and widgets
RUN apt-get install -y curl gnupg
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get autoremove -y

RUN apt-get install -y nodejs

RUN apt-get -y install wget iproute2
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8

RUN apt-get install -y zsh
# Uses "robbyrussell" theme (original Oh My Zsh theme), with no plugins
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.0/zsh-in-docker.sh)" -- -t robbyrussell

RUN update-ca-certificates

# Install uv first to manage Python apps.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN echo "downloaded uv successfully"

# Ensure venv Python and uv are accessible.
ENV PATH=/venv/bin:$PATH
ENV PATH=/root/.cargo/bin:$PATH
ENV PATH="/root/.local/bin/:$PATH"
ENV UV_LINK_MODE=copy
