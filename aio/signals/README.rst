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
 ...     result.message = message

 >>> import asyncio
 >>> signals.listen("test-signal", asyncio.coroutine(callback))

 >>> def run_test():
 ...     yield from signals.emit("test-signal", 'BOOM!')

 >>> from aio.testing import aiotest

 >>> aiotest(run_test)()
 >>> result.message
 'BOOM!'
