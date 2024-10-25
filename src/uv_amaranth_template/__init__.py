from amaranth import *

from amaranth_boards.icebreaker import ICEBreakerPlatform
from amaranth_boards.versa_ecp5 import VersaECP5Platform
from amaranth_boards.tang_nano import TangNanoPlatform
from amaranth_boards.arty_a7 import ArtyA7_100Platform

from .blinky import Blinky

# Temporary fix until uv supports env files
from dotenv import load_dotenv


class Toplevel(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        m.submodules.blinky = blinky = Blinky(frequency=platform.default_clk_frequency)
        m.d.comb += platform.request("led", 0).o.eq(blinky.led)

        return m


def build_icebreaker():
    load_dotenv()
    ICEBreakerPlatform().build(Toplevel())


def build_ecp5():
    load_dotenv()
    VersaECP5Platform().build(Toplevel())


def build_gowin():
    load_dotenv()
    TangNanoPlatform().build(Toplevel())


def build_arty100():
    load_dotenv()
    ArtyA7_100Platform().build(Toplevel())
