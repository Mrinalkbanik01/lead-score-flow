from groq import Groq

client = Groq(api_key="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")
response = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[{"role": "user", "content": "Hello, what is AI?"}]
)
print(response.choices[0].message.content)