import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def fix_my_docker():
    with open("Dockerfile", "r") as f:
        old_content = f.read()

    print("🔧 AI is re-engineering your Dockerfile for Agoda production standards...")

    prompt = f"""
    You are a Senior DevOps Engineer. Rewrite this Dockerfile to be production-ready.
    Apply these specific fixes:
    1. Use python:3.9-slim as the base image.
    2. Create a non-root user named 'agoda_user' to run the app.
    3. Use a proper WORKDIR and clean up apt-get lists.
    4. Ensure it uses gunicorn instead of http.server.
    
    Original Dockerfile:
    {old_content}
    
    Return ONLY the code for the new Dockerfile. No explanations.
    """

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    # Save the new version
    with open("Dockerfile.fixed", "w") as f:
        f.write(response.text.strip().replace("```dockerfile", "").replace("```", ""))

    print("✅ Fixed Dockerfile saved as 'Dockerfile.fixed'!")


if __name__ == "__main__":
    fix_my_docker()
