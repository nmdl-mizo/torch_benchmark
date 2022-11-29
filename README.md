# Torch Benchmark

## Usage

Build the docker image and run container:

```bash
chmod +x build_run.sh [SAVE_NAME (default: torch_benchmark.log)] [TORCH_VERSION (default: 1.13.0)] [CUDA_VERSION (default: 11.6)]
./build_run.sh
```

Or only run container:

```bash
chmod +x run.sh [SAVE_NAME (default: torch_benchmark.log)]
./run.sh
```

## Add benchmark case

If you want to add a new benchmark case, please add the code under `torch_bench/codes`.
If you need additional packages, please add it to `torch_bench/requirements.txt`.
