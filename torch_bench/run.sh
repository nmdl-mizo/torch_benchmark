#! /bin/bash

SAVE_NAME="${1:-torch_benchmark.log}"

docker run -d  \
    -u `id -u`:`id -g` \
    --rm \
    --gpus all \
    --mount type=bind,source="$(pwd)",target=/tmp \
    torch_benchmark \
    main.py --save_name "${SAVE_NAME}"
