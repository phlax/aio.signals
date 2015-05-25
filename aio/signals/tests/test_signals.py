import unittest
import asyncio

import aio.testing
from aio.signals import Signals


class AioSignalsTestCase(unittest.TestCase):

    def test_listen(self):

        def signal_called(signal):
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)

        self.assertEqual(
            signals._signals,
            {"test-signal": set([signal_called])})

    def test_listen_again(self):

        def signal_called(signal):
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.listen('test-signal', signal_called)

        self.assertEqual(
            signals._signals,
            {"test-signal": set([signal_called])})

    def test_unlisten(self):

        def signal_called(signal):
            pass

        def signal_called2(signal):
            pass

        signals = Signals()
        signals.listen('test-signal', signal_called)
        signals.listen('test-signal', signal_called2)
        signals.unlisten('test-signal', signal_called)

        self.assertEqual(
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

        self.assertEqual(
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

        self.assertEqual(
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
        self.assertEqual(
            signals._signals,
            {"test-signal": set([signal_called])})

    @aio.testing.run_until_complete
    def test_emit(self):
        """
        """
        class Checker:
            signal = None
            args = None
        checker = Checker()

        @asyncio.coroutine
        def signal_called(signal):
            yield from asyncio.sleep(2)
            checker.signal = signal.name
            checker.args = signal.data
            return "done"

        signals = Signals()
        signals.listen('test-signal', signal_called)

        result = yield from signals.emit('test-signal', "EXPECTED RESULT")

        self.assertEqual(result, ["done"])
        self.assertEqual(checker.signal, "test-signal")
        self.assertEqual(checker.args, "EXPECTED RESULT")
