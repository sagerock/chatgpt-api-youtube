import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an essay about penguine"}])
print(completion.choices[0].message.content)