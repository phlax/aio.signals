aio.signals usage
=================

Using
-----

>>> import asyncio
>>> import aio.testing
>>> from aio.signals import Signals

>>> @asyncio.coroutine
... def callback(signal, message):
...     print(message)

>>> @aio.testing.run_until_complete
... def run_test(_signals, message):
...     yield from _signals.emit("test-signal", message)

>>> signals = Signals()
>>> signals.listen("test-signal", callback)

>>> run_test(signals, 'BOOM!')
BOOM!

The handler doesnt have to be a coroutine but it will be wrapped if its not

>>> def callback(signal, message):
...     yield from asyncio.sleep(2)
...     print(message)

>>> signals = Signals()
>>> signals.listen("test-signal", callback)

>>> run_test(signals, 'BOOM AGAIN!')
BOOM AGAIN!
