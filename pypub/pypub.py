from abc import ABC, abstractmethod

class EventManager:
    """Manage publishing of and subscription to event publishers.

        Provides ability to subscribe and unsubscibe to topics and publish events.
        The methods in EventManager are static because there should only ever be 
        one instance of EventManager at any time.
    """

    subscribers = {}

    @staticmethod
    def subscribe(subscriber):
        """Add a subscriber based on the passed in subscriber's declared topic.

        Arguments:
        subscriber -- the Subscriber to add to future topic publications
        """

        if subscriber.getTopic() not in EventManager.subscribers:
            EventManager.subscribers[subscriber.getTopic()] = []
        EventManager.subscribers[subscriber.getTopic()].append(subscriber.receive)
            
    @staticmethod
    def unsubscribe(subscriber):
        """Remove a subscriber based on the passed in subscriber's declared topic.

        Arguments:
        subscriber -- the subscriber to be removed from future topic publications
        """

        topicSubscribers = EventManager.subscribers[subscriber.getTopic()]
        del topicSubscribers[subscriber]

    @staticmethod
    def publish(publishData, topic=""):
        """Publish a new event with passed in data to all subscribers of the passed in topic.

        Arguments:
        publishData -- the event data
        topic -- the topic to publish the event to (default "")
        """
        subscribers = EventManager.subscribers[topic]
        for subscriber in subscribers:
            subscriber(publishData)

class Suscriber():
    """Receive events from the EventManager according to declared topic.

        A Subscriber specifies the topic they care about. The Subscriber's callback
        will only be called if the published event topic matches the Subscriber's 
        declared topic. Upon receiving a new event, the Subscriber's callback method 
        is called. A PublishData object may or may not be passed into the Subscriber's
        callback method.
    """

    def __init__(self, topic, callback):
        self.topic = topic
        self.callback = callback
        EventManager.subscribe(self)
    
    def receive(self, publishData):
        self.callback(publishData)

    def getTopic(self):
        return self.topic

class Publisher():
    """Publishes events to the EventManager on the declared topic.

       Sends event publications to the EventManager with the passed in data value.
    """
    def __init__(self, topic):
        self.topic = topic
    
    def publish(self, publishData):
        EventManager.publish(self.topic, publishData)

    def getTopic(self):
        return self.topic

class PublishData(ABC):
    """Data object wrapper passed to the EventManager as event data.

        PublishData objects are simply wrappers around an object that one
        wishes to pass into an event as event data when that event is 
        published.
    """
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data