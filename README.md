# Amaranth FPGA project template using [uv by Astral](https://github.com/astral-sh/uv)

[![CI](https://github.com/RafaelRiber/uv-amaranth-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/RafaelRiber/uv-amaranth-template/actions/workflows/ci.yml)

Template for Amaranth projects using the uv package and project manager, based on the [Amaranth Project template](https://github.com/amaranth-lang/template-fpga)

### Usage
- [Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
```
git clone https://github.com/RafaelRiber/uv-amaranth.git
cd uv-amaranth
uv run <target> 
```
Current targets:
- icebreaker board (ice40up5k)

For example:
```
uv run build_icebreaker
openFPGALoader -b ice40_generic build/top.bin
```

### Tests
To run the tests located in the tests/ directory, use uv to run pytest:
```
uv run -m pytest
```


### TODO:
- [x] Implement tests
- [ ] remove python-dotfiles dependency when uv has merged the integration of .env files (https://github.com/astral-sh/uv/issues/1384)
- [ ] Explore the use of [pytest-amaranth-sim](https://github.com/cr1901/pytest-amaranth-sim)





