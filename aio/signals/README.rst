aio.signals usage
=================

Using
-----

>>> import asyncio
>>> import aio.testing
>>> from aio.signals import Signals

The handler receives a signal object

signal.name is the name of the signal

signal.data contains the emitted object

>>> @asyncio.coroutine
... def callback(signal):
...     print("%s received with %s" % (signal.name, signal.data))

>>> @aio.testing.run_until_complete
... def run_test(_signals, name, message):
...     yield from _signals.emit(name, message)

>>> signals = Signals()
>>> signals.listen("test-signal", callback)

>>> run_test(signals, "test-signal", 'BOOM!')
test-signal received with BOOM!

The handler is wrapped in a co-routine if its not one already

>>> def callback(signal):
...     yield from asyncio.sleep(1)
...     print("%s received with %s" % (signal.name, signal.data))

>>> signals = Signals()
>>> signals.listen("test-signal-2", callback)

>>> run_test(signals, "test-signal-2", 'BOOM AGAIN!')
test-signal-2 received with BOOM AGAIN!
