aio.signals
===========

Pubsub system for the aio_ asyncio framework

.. _aio: https://github.com/phlax/aio


Build status
------------

.. image:: https://travis-ci.org/phlax/aio.signals.svg?branch=master
	       :target: https://travis-ci.org/phlax/aio.signals



Installation
------------
Install with:

.. code:: bash

	  pip install aio.signals


Code example
------------

.. code:: python

	  import asyncio

	  from aio.signals import Signals

	  def listener(signal, message):
	      print(message)

	  signals = Signals()

The listen function is called synchronously

	  signals.listen("listener", asyncio.coroutine(callback))

	  loop = asyncio.get_event_loop()
	  loop.run_until_complete(
	      signals.emit("my-signal", 'BOOM!'))
