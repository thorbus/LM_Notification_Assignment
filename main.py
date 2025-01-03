import json
from system import NotificationService

def main():
    service = NotificationService()
    while True:
        command = input("Enter command: ").strip()
        if command == "exit":
            break
        try:
            parts = command.split(" ", 1)
            action = parts[0]

            if action == "addUser":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                user_name, role = parts[1].split()
                service.add_user(user_name, role)

            elif action == "addTopic":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                topic_name, admin_name = parts[1].split()
                service.add_topic(topic_name, admin_name)

            elif action == "subscribeTopic":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                topic_name, user_name = parts[1].split()
                service.subscribe_topic(topic_name, user_name)

            elif action == "publishMessage":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                message_body = json.loads(parts[1])
                service.publish_message(message_body)

            elif action == "processMessages":
                service.process_messages()

            elif action == "viewSubscribedTopics":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                user_name = parts[1]
                service.view_subscribed_topics(user_name)

            elif action == "removeUser":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                user_name1, user_name2 = parts[1].split()
                service.remove_user(user_name1, user_name2)

            elif action == "removeTopic":
                if len(parts) < 2:
                    print("Error: Missing command arguments")
                    continue
                topic_name, admin_name = parts[1].split()
                service.remove_topic(topic_name, admin_name)

            else:
                print("Error: Invalid command")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
