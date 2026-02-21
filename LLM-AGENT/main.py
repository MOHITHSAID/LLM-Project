# main.py

from agent import run_agent

def main():
    print("\n🧠 AI Monument & Travel Assistant (Gemini Chat)\n")

    monument_name = input("Enter monument or location name: ")
    print("\nYou can now ask questions. Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ")

        if user_query.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Thanks for chatting!")
            break

        # Call the agent without memory
        answer = run_agent(monument_name, user_query)

        print(f"\nAssistant: {answer}\n")


if __name__ == "__main__":
    main()