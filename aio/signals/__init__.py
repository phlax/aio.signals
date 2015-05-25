import asyncio
import logging

log = logging.getLogger("aio.signals")


class SignalEvent(object):

    def __init__(self, name, data):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data


class Signals(object):

    def __init__(self):
        self._signals = {}

    def listen(self, signal, cb):
        log.debug('listening %s %s' % (signal, cb))
        if signal not in self._signals:
            self._signals[signal] = set()
        self._signals[signal].add(cb)

    def unlisten(self, signal, cb):
        log.debug('listening %s %s' % (signal, cb))
        if signal in self._signals:
            if cb in self._signals[signal]:
                self._signals[signal].remove(cb)

    @asyncio.coroutine
    def emit(self, s, v):
        log.debug('emitting %s %s' % (s, v))

        if s in self._signals:
            tasks = []
            for signal in self._signals[s]:
                log.debug('emitting %s %s %s' % (s, signal, v))
                if not asyncio.iscoroutinefunction(signal):
                    signal = asyncio.coroutine(signal)
                tasks.append(asyncio.async(signal(SignalEvent(s, v))))
            # dont yield from here
            return asyncio.gather(*tasks)
