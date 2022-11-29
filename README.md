# Torch Benchmark

## Usage

Build the docker image and run container:

```bash
./build_run.sh [SAVE_NAME (default: torch_benchmark.log)] [TORCH_VERSION (default: 1.13.0)] [CUDA_VERSION (default: 11.6)]
```

Or only run container:

```bash
./run.sh [SAVE_NAME (default: torch_benchmark.log)]
```

The result file will be saved in `torch_bench/SAVE_NAME`.

## Add benchmark case

If you want to add a new benchmark case, please add the code under `torch_bench/codes`.
If you need additional packages, please add it to `torch_bench/requirements.txt`.

Before running script, please make sure that your code is runnable with this command:

```bash
python3 [YOUR_CODE]
```
