aio.signals usage
=================

Using
-----

>>> class Result:
...     message = None
>>> result = Result()

>>> from aio.signals import Signals
>>> signals = Signals()

>>> def callback(signal, message):
...     print(message)

>>> import asyncio
>>> import aio.testing

>>> signals.listen("test-signal", asyncio.coroutine(callback))

>>> @aio.testing.run_until_complete
... def run_test():
...     yield from signals.emit("test-signal", 'BOOM!')

>>> run_test()
BOOM!
