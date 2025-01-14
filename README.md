
# Pub-SUb

It is a console-based CLI notification service that simulates a publisher-consumer model in a console environment. The application allows users to create and manage topics, publish messages, and notify subscribers, demonstrating the fundamentals of messaging systems and object-oriented programming.







## Run Locally

Clone the project

```bash
  git clone https://github.com/thorbus/Pub_sub_model.git
```

Go to the project directory

Run App

```bash
      python .\main.py
```


Commands for demo

Add users
```bash
    addUser admin1 ADMIN

```
```bash
    addUser user1 User

```
```bash
    addUser user2 User

```

Add topics

```bash
     addTopic cricket admin1

```
Subscribe to topic
```bash
     subscribeTopic cricket user1
     subscribeTopic cricket user2

```

Publish Message

```bash
     publishMessage {"id": "1", "topicName": "cricket", "text": "Hi, cricket fans!"}
     publishMessage {"id": "2", "topicName": "cricket", "text": "Hi, cricket fans!"}

```

To Process Message

```bash
   processMessages

```

Additional Commands

To view subscribed topics
```bash
    viewSubscribedTopics user1
    viewSubscribedTopics user2
```

To remove User using admin access only o/w will give error

```bash
    removeUser user1 admin1

```









## Features

User Management

Add users with roles (ADMIN and USER).
Admins manage topics and users; users subscribe to topics and receive notifications.
Topic Management

Create and remove topics (admin-only functionality).
Subscribe users to topics.
Message Publishing and Processing

Publish messages to topics with a unique message ID, topic name, and text.
Process messages to notify all subscribers of a topic.
Notification Delivery

View subscribed topics for a user.
Remove users and topics with admin access.
Logical and language-based error handling.
Console Emulation
