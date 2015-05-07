import unittest
import asyncio

from aio.testing import aiotest
from aio.signals import Signals


class AioSignalsTestCase(unittest.TestCase):

    def test_listen(self):

        def signal_called():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)

        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called])})

    def test_listen_again(self):

        def signal_called():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.listen('test-signal', signal_called)

        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called])})

    def test_unlisten(self):

        def signal_called():
            pass

        def signal_called2():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.listen('test-signal', signal_called2)
        signals.unlisten('test-signal', signal_called)

        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called2])})

    def test_unlisten_again(self):
        """
        calling signals.unlisten twice does nothing
        """

        def signal_called():
            pass

        def signal_called2():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.listen('test-signal', signal_called2)
        signals.unlisten('test-signal', signal_called)
        signals.unlisten('test-signal', signal_called)

        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called2])})

    def test_unlisten_missing_signal(self):
        """
        if signals.unlisten is called with non-existent signal
        silently ignore
        """

        def signal_called():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.unlisten('FOO-SIGNAL', signal_called)

        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called])})

    def test_unlisten_missing_func(self):
        """
        if signals.unlisten is called with non-existent callback func
        silently ignore
        """

        def signal_called():
            pass

        def signal_called2():
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.unlisten('test-signal', signal_called2)
        self.assertEquals(
            signals._signals,
            {"test-signal": set([signal_called])})

    @aiotest
    def test_emit(self):
        """
        """
        class Checker:
            signal = None
            args = None
        checker = Checker()

        @asyncio.coroutine
        def signal_called(signal, args):
            yield from asyncio.sleep(2)
            checker.signal = signal
            checker.args = args
            return "done"

        signals = Signals()
        signals.listen('test-signal', signal_called)

        result = yield from signals.emit('test-signal', "EXPECTED RESULT")

        self.assertEquals(result, ["done"])
        self.assertEquals(checker.signal, "test-signal")
        self.assertEquals(checker.args, "EXPECTED RESULT")