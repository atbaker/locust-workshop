Exercise 2: More realistic users
================================

Now that we know how to run Locust, let's take a closer look at exactly what our Locust users were doing.

.. warning::
    
    For this exercise, I won't be as explicit about what the correct answer is. You may need to reference the `Locust documentation <http://docs.locust.io/en/latest/writing-a-locustfile.html>`_ to complete all the tasks.

Locustfile 101
--------------

Stop the Locust server (if you haven't already) and open up the ``locustfile.py`` file in a text editor of your choice.

That first class defined in our locustfile is our **TaskSet**. When Locust runs our load testing, it's executing the requests specified in the methods we define in this class. The ``@task()`` decorator is used to tell Locust that we want a method to be executed as part of our load test.

You'll notice that right now we have only one task defined in our TaskSet - ``view_api_root``. When Locust executes that task, it just makes a simple ``GET`` request to the ``/api/`` URL on our host.

If you pull up that URL in the Django REST Framework web browsable API, you'll see that there's not much to it::

    HTTP 200 OK
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json

    {
        "users": "http://192.168.59.103:8000/api/users/",
        "devices": "http://192.168.59.103:8000/api/devices/",
        "actions": "http://192.168.59.103:8000/api/actions/",
        "tweets": "http://192.168.59.103:8000/api/tweets/",
        "handles": "http://192.168.59.103:8000/api/handles/"
    }

All this URL returns is a list of other API endpoints available on our server. Load testing this URL isn't very useful, since a real user probably won't be interested in our API architecture.

**Define a new task within our TaskSet that makes a GET request to the "tweets" endpoint.** This endpoint lists all the Tweets that are pending review for a given organization, and is used every time a user visits their TweetCheck dashboard.

.. note::

    The URL for that endpoint is ``/api/tweets/``.

Now start up your Locust server again and run it for **250 users** with a spawn rate of **25**.

**Take a look at the RPS and median response time stats.** How do they compare with test from the last exercise?

POSTing Locusts
---------------

Our new Locust task does a good job simulating when users visit our application's dashboard, but it's still not an accurate representation of user behavior. Sometimes, our users are going to create new tweets and submit them for review.

Let's write a new Locust task that adds a new tweet to our API. To do that, we need to make a ``POST`` request to the ``tweets`` endpoint. We also need to include some data in that request, a handle and a tweet body.

**Make a new Locust task that sends a POST request to the tweets endpoint.** The data of your request should look like this: ``{'handle': 1, 'body': 'This tweet brought to you by Locust'}``.

.. note::

    If you need a hint for creating a POST request in Locust, check out `this section of the documentation <http://docs.locust.io/en/latest/writing-a-locustfile.html#using-the-http-client>`_

When you're done, fire up our Locust server again with the same users and spawn rate. How do the stats compare from our last test?

It should be immediately evident that creating new tweets with our API is much harder for our server to handle at scale than reading data about existing tweets.

And our server's task is complicated by the fact that the list of tweets (hit in our second task) keeps growing as our tests go on. If you watch closely, you may be able to see performance steadily decrease as the database fills up with more and more data.

Wrap-up
-------

I hope you have seen today that Locust is an easy and fun way to stress-test your web applications.

We just scratched the surface on what a valid Locust test looks like, but now you have the tools and knowledge to see how far you can push your own applications.
