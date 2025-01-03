import time
from models import User, Topic, Message
import json

class NotificationService:
    def __init__(self):
        self.users = {}
        self.topics = {}

    def add_user(self, user_name, role):
        if user_name in self.users:
            print("Error: User already exists")
            return
        self.users[user_name] = User(user_name, role)
        print("User successfully added")

    def add_topic(self, topic_name, admin_name):
        if admin_name not in self.users or self.users[admin_name].role != "ADMIN":
            print("Error: Admin access required")
            return
        if topic_name in self.topics:
            print("Error: Topic already exists")
            return
        self.topics[topic_name] = Topic(topic_name)
        print("Topic successfully added")

    def subscribe_topic(self, topic_name, user_name):
        if topic_name not in self.topics:
            print("Error: Topic does not exist")
            return
        if user_name not in self.users:
            print("Error: User does not exist")
            return
        topic = self.topics[topic_name]
        user = self.users[user_name]
        if user in topic.subscribers:
            print("Error: User already subscribed")
            return
        topic.subscribers.append(user)
        print("Topic successfully subscribed")

    def publish_message(self, message_body):
        msg_id = message_body["id"]
        topic_name = message_body["topicName"]
        text = message_body["text"]
        

        if topic_name not in self.topics:
            print("Error: Topic does not exist")
            return

        message = Message(msg_id, topic_name, text)
        self.topics[topic_name].messages.append(message)
        print("Message successfully published")

    def process_messages(self):
        print("Processing messages")
        for topic in self.topics.values():
            for message in topic.messages[:]:
                
                for subscriber in topic.subscribers:
                    print({
                        "topic": topic.topic_name,
                        "message": message.text,
                        "sentTo": subscriber.user_name
                    })
                topic.messages.remove(message)
        print("Messages successfully processed")

    def view_subscribed_topics(self, user_name):
        if user_name not in self.users:
            print("Error: User does not exist")
            return
        user = self.users[user_name]
        subscribed_topics = [topic.topic_name for topic in self.topics.values() if user in topic.subscribers]
        print(f"Subscribed topics for {user_name}: {subscribed_topics}")

    def remove_user(self, user_name1, user_name2):
        if user_name2 not in self.users or self.users[user_name2].role != "ADMIN":
            print("Error: Admin access required")
            return
        if user_name1 not in self.users:
            print(f"Error: User {user_name1} does not exist")
            return
        if user_name1 == user_name2:
            print("Error: Admin cannot remove themselves")
            return

        # Remove the user from all topics they are subscribed to
        for topic in self.topics.values():
            topic.subscribers = [user for user in topic.subscribers if user.user_name != user_name1]

        del self.users[user_name1]
        print(f"User {user_name1} successfully removed")

    def remove_topic(self, topic_name, admin_name):
        if admin_name not in self.users or self.users[admin_name].role != "ADMIN":
            print("Error: Admin access required")
            return
        if topic_name not in self.topics:
            print(f"Error: Topic {topic_name} does not exist")
            return
        del self.topics[topic_name]
        print(f"Topic {topic_name} successfully removed")
