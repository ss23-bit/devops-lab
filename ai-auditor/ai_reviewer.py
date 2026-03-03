import os
from google import genai

# Setup the Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def review_my_docker():
    if not os.path.exists("Dockerfile"):
        print("❌ No Dockerfile found!")
        return

    with open("Dockerfile", "r") as f:
        content = f.read()

    print("🤖 AI is reviewing your infrastructure...")

    try:
        # Use the exact model name found in your list
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"You are a Senior DevOps Engineer at Agoda. Review this Dockerfile for security and efficiency. Give 3 bullet points of advice:\n\n{content}",
        )

        print("\n--- AGODA SENIOR DEVOPS FEEDBACK ---")
        print(response.text)
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    review_my_docker()
