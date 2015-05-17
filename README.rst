aio.signals
===========

Pubsub system for the aio_ asyncio framework

.. _aio: https://github.com/phlax/aio



Build status
------------

.. image:: https://travis-ci.org/phlax/aio.signals.svg?branch=master
	       :target: https://travis-ci.org/phlax/aio.signals

----


Installation
------------
Install with:

.. code:: bash

	  pip install aio.signals

----


Code example
------------

.. code:: python

	  import asyncio

	  from aio.signals import Signals

The callback listener takes 2 arguments, the name of the signal, and the argument that was emitted

.. code:: python

	  def listener(signal, message):
	      print(message)

	  signals = Signals()

The listen function is called synchronously, but the callback listener should be a coroutine or future

.. code:: python

	  signals.listen("my-signal", asyncio.coroutine(listener))

The emit function is a coroutine

.. code:: python

	  loop = asyncio.get_event_loop()
	  loop.run_until_complete(
	      signals.emit("my-signal", 'BOOM!'))
