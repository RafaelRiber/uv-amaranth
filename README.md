# Amaranth FPGA project template using [uv by Astral](https://github.com/astral-sh/uv)

Template for Amaranth projects, based on the [Amaranth Project template](https://github.com/amaranth-lang/template-fpga)

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
### TODO:
- [ ] Implement tests
- [ ] remove python-dotfiles dependency when uv has merged the integration of .env files (https://github.com/astral-sh/uv/issues/1384)
