import openai

openai.api_key = "YOUR_API_KEY"

def chatGPT_answer(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"].strip()
    return message

while True:
    question = input("You: ")
    if question == "quit":
        break
    answer = chatGPT_answer(question + " about Miami")
    print("ChatGPT: " + answer)
