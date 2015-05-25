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

Requires python >= 3.4

Install with:

.. code:: bash

	  pip install aio.signals


Quickstart
----------

The listen function is called synchronously, but the callback listener will be called as a coroutine if it isnt one

The callback listener receives a signal object that has the name of the signal and the object that the signal was emitted with

The emit function is a coroutine

Add the following code to a file my_signals.py

.. code:: python

	  import asyncio
	  from aio.signals import Signals	  
	  
	  def listener(signal):
	      yield from asyncio.sleep(1)
	      print(signal.data)

	  signals = Signals()
	  signals.listen("my-signal", listener)

	  loop = asyncio.get_event_loop()
	  loop.run_until_complete(
	      signals.emit("my-signal", 'BOOM!'))


Run with

.. code:: bash

	  python my_signals.py

