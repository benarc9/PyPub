from abc import ABC, abstractmethod

class EventManager:
    subscribers = {}

    @staticmethod
    def subscribe(subscriber):
        if subscriber.getTopic() not in EventManager.subscribers:
            EventManager.subscribers[subscriber.getTopic()] = []
        EventManager.subscribers[subscriber.getTopic()].append(subscriber.receive)
            
    @staticmethod
    def unsubscribe(subscriber):
        topicSubscribers = EventManager.subscribers[subscriber.getTopic()]
        del topicSubscribers[subscriber]

    @staticmethod
    def publish(topic, publishData):
        subscribers = EventManager.subscribers[topic]
        for subscriber in subscribers:
            subscriber(publishData)

class Suscriber():
    def __init__(self, topic, callback):
        self.topic = topic
        self.callback = callback
        EventManager.subscribe(self)
    
    def receive(self, publishData):
        self.callback(publishData)

    def getTopic(self):
        return self.topic

class Publisher():
    def __init__(self, topic):
        self.topic = topic
    
    def publish(self, publishData):
        EventManager.publish(self.topic, publishData)

    def getTopic(self):
        return self.topic

class PublishData(ABC):
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data