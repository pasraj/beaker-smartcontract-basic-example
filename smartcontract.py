from pyteal import abi

from beaker.client.application_client import ApplicationClient
from beaker.application import Application
from beaker.decorators import external
from beaker import sandbox


class Calculator(Application):
    @external
    def add(self, a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
        """Add a and b, return the result"""
        return output.set(a.get() + b.get())

