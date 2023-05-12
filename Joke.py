import tkinter as tk
import random
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke App")

        self.label = tk.Label(root, text="Enter your joke prompt:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Tell me a joke", command=self.tell_joke)
        self.button.pack(pady=5)

    def tell_joke(self):
        prompt = self.entry.get()
       # if self.entry.get() == '':
            #prompt = "give me a random joke"
        joke = self.generate_joke(prompt)
        self.display_joke(joke)

    def generate_joke(self, prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=0.2,
            presence_penalty=0.0
        )

        return response.choices[0].text.strip()

    def display_joke(self, joke):
        if not joke:
            joke = "I couldn't come up with a joke. Please try again!"
        self.label.config(text=joke)

root = tk.Tk()
joke_app = JokeApp(root)
root.mainloop()
