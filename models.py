class User:
    def __init__(self, user_name, role):
        self.user_name = user_name
        self.role = role

class Topic:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.subscribers = []
        self.messages = []

class Message:
    def __init__(self, msg_id, topic_name, text):
        self.id = msg_id
        self.topic_name = topic_name
        self.text = text
        
