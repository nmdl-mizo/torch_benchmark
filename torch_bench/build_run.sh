#! /bin/bash

SAVE_NAME="${1:-torch_benchmark.log}"
TORCH_VERSION="${2:-1.13.0}"
CUDA_VERSION="${3:-11.6}"

docker image build -t torch_benchmark \
    --build-arg TORCH_VERSION="${TORCH_VERSION}" \
    --build-arg CUDA_VERSION="${CUDA_VERSION}" \
    .

docker run -d  \
    -u `id -u`:`id -g` \
    --rm \
    --gpus all \
    --mount type=bind,source="$(pwd)",target=/tmp \
    torch_benchmark \
    main.py --save_name "${SAVE_NAME}"
