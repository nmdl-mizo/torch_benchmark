ARG TORCH_VERSION=1.13.0
ARG CUDA_VERSION=11.6

FROM pytorch/pytorch:${TORCH_VERSION}-cuda${CUDA_VERSION}-cudnn8-runtime
ARG TORCH_VERSION
ARG CUDA_VERSION

RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y install --no-install-recommends \
    gcc \
    libpq-dev \
    && apt clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

COPY . /tmp

RUN pip3 install -U pip && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt -f https://data.pyg.org/whl/torch-${TORCH_VERSION}+cu`echo ${CUDA_VERSION} | sed -e 's/\.//'`.html

WORKDIR /tmp
ENTRYPOINT [ "python3" ]
