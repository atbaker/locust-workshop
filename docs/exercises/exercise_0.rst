Exercise 0: Getting started
===========================

In this section we will set up your development environment to use Locust.

Skip the setup
--------------

The easiest way to get started today is to use one of my cloud servers. I have already configured these servers with everything you need for today's lesson.

If you are comfortable writing code in a terminal session, I recommend using one of these servers so you can get started immediately.

Pick out a server from this Google Spreadsheet and put your name next to the one you want to use: https://docs.google.com/spreadsheets/d/1FRZcEmD3l9c2M8EaO9Nj-H0BiWkzBUgz0KkdNoZClXM/edit?usp=sharing

Download the |identity_file_link| identity file, and then connect to your server by running the command in column B.

.. |identity_file_link| raw:: html

   <a href="/locust_tutorial.pem" download>locust_tutorial.pem</a>

.. note::

    You may need to change the permissions on the ``locust_tutorial.pem`` file. On Mac and Linux, you can do that with ``chmod 600 locust_tutorial.pem``.

Once in, you will need to first activate a Python virtual environment by running ``source venv/bin/activate``.

After that, ``cd`` into the directory called ``locust-workshop``. That's what we'll use for the rest of this workshop.

Local development
-----------------

If you prefer to develop locally on your laptop, follow these instructions:

#. Install Python and pip if you haven't already
#. Clone this repo: https://github.com/atbaker/locust-workshop
#. Create a new virtuale environment
#. Install the requirements with ``pip install -r requirements.txt``. (If you hit errors, consult the `Locust installation docs for your OS <http://docs.locust.io/en/latest/installation.html>`_)
#. Run ``locust --help`` - if it works, you're ready to go!

Next steps
----------

Once your development environment is ready to go, continue to :doc:`exercise_1`
