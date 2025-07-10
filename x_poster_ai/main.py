from post_generator import generate_post
from twitter_api import post_to_x

def run():
    topic = input("Enter a topic for the post: ")
    message = generate_post(topic)
    print(f"\nGenerated Post:\n{message}")
    confirm = input("\nPost to X? (y/n): ")
    if confirm.lower() == 'y':
        post_to_x(message)

if __name__ == "__main__":
    run()
