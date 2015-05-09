Exercise 1: Your first Denial of Service attack
===============================================

Now that your environment is ready to go, let's start testing some servers!

Meet TweetCheck
---------------

Before we can start load testing our site with Locust, we need to point it at the right host.

Go to the Google Spreadsheet below and pick out one of the servers. Put your name in column B, and then copy the hostname in column A.

https://docs.google.com/spreadsheets/d/1bHNLewapR6mrgpk1V5VYPFaBJXYMKF7KHZ4a0XnWP00/edit?usp=sharing

.. warning::

    If you're not doing this workshop in person with me, you will need to stand up your own TweetCheck API server.

    `Follow the instructions in the "Quickstart" section of the TweetCheck repo README. <https://github.com/atbaker/tweetcheck>`_

Open up ``locustfile.py`` in your development environment and find the ``host`` property of the ``WebsiteUser`` class. Set that ``host`` property to ``http://YOUR_HOSTNAME_HERE``

Use your hostname from the spreadsheet as the value for that property and save your locustfile.

You should also take a moment to check out the TweetCheck API, which is what we'll be testing. TweetCheck uses the `Django REST Framework <http://www.django-rest-framework.org/>`_ project, which includes an excellent web browsable API.

You can see your server's TweetCheck data by going to ``http://[your server's hostname here]/api``. You can log in with these credentials:

    **Username:** admin@tweetcheck.com
    
    **Password:** admin

.. note::
    
    You don't need to be familiar with TweetCheck's API to complete this workshop, but feel free to poke around if you're curious.

Fire it up!
-----------

We're finally ready to let our locusts fly. It's time to see how much heat that server can take.

Run the simple command ``locust`` in your development environment. Locust will then load your locustfile and start a web interface to help you run your tests.

.. note::

    Locust may display a few warning messages when you start it up. Don't worry about those for our workshop today.

To access the Locust web interface, go to ``http://[your development environment's hostname here]:8089``. You should see a screen that looks like this:

.. image:: /_static/locust-ready.png

No point in holding back, so let's hit our servers with **250 simultaneous users** at a hatch rate of **25** per second. Click "Start swarming" to kick them off.

If everything worked correctly, your Locust dashboard should look like this:

.. image:: /_static/locust-start.png

.. warning::

    If you're seeing lots of requests pile up in the ``# fails`` column, something's wrong. Please ask me for help.

First, Locust will slowly spawn users at the rate we specified. When all users have been created, Locust resets the stats on the dashboard and will keep our users running indefinitely.

Take a moment to look at all the statistics Locust provides about our API's performance. There's a lot of data there, so I usually focus on the **RPS** (requests per second) value at the top and the **Median** response time column in the middle.

**Make a note of these values to yourself. We'll compare them results from other tests later in our workshop.**

When you're done reflecting on the terrible, widespread destruction you inflict on the Internet with this newfound power, move on to :doc:`exercise_2`. 
