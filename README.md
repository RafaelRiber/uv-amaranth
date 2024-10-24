Amaranth FPGA project template using [uv by Astral](https://github.com/astral-sh/uv)

Usage
```
git clone https://github.com/RafaelRiber/uv-amaranth.git
cd uv-amaranth
uv run <target> 
```
Current targets:
- icebreaker board (ice40up5k)


For example:
```
uv run icebreaker
openFPGALoader -b ice40generic build/top.bin
```
