import asyncio
import os
from nemoguardrails import LLMRails, RailsConfig

config = RailsConfig.from_path("./config")
app = LLMRails(config)

async def main():
    print("--- Testing Question 1 (Related to Job Report) ---")
    response = await app.generate_async(messages=[{
        "role": "user",
        "content": "How was the job market in March 2023 according to the report?"
    }])
    print("AI Response 1:", response['content'])

    print("\n--- Testing Question 2 (Off-topic) ---")
    response_offtopic = await app.generate_async(messages=[{
        "role": "user",
        "content": "What is the capital of France?"
    }])
    print("AI Response 2:", response_offtopic['content'])

if __name__ == "__main__":
    asyncio.run(main())
