import os
import reflex as rx
from openai import OpenAI

import creds
from creds import *
from pathlib import Path
from gpt4all import GPT4All

model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
model = GPT4All(model_name=model_name, model_path=model_path)
system_template = 'A chat between Lawrence and Lucy an artificial intelligence assistant.\n'

os.environ["OPENAI_API_KEY"] = f"{creds.api_key}"

# Checking if the API key is set properly
if not os.getenv("OPENAI_API_KEY"):

    raise Exception("Please set OPENAI_API_KEY environment variable.")


class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


DEFAULT_CHATS = {
    "Intros": [],
}


class State(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = DEFAULT_CHATS

    # The current chat name.
    current_chat = "Intros"

    # The current question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""

    def create_chat(self):
        """Create a new chat."""
        # Add the new chat to the list of chats.
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        # Get the question from the form
        question = form_data["question"]

        # Check if the question is empty
        if question == "":
            return

        # model = self.openai_process_question
        model = self.gpt4all_local
        async for value in model(question):
            yield value

    async def openai_process_question(self, question: str):
        """Get the response from the API.

        Args:
            form_data: A dict with the current question.
        """

        # Add the question to the list of questions.
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)

        # Clear the input and start the processing.
        self.processing = True
        yield

        # Build the messages.
        messages = [
            {
                "role": "system",
                "content": "A chat between Lawrence and Lucy an artificial intelligence assistant.",
            }
        ]
        for qa in self.chats[self.current_chat]:
            messages.append({"role": "user", "content": qa.question})
            messages.append({"role": "assistant", "content": qa.answer})

        # Remove the last mock answer.
        messages = messages[:-1]

        # Start a new session to answer the question.
        session = OpenAI().chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=messages,
            stream=True,
        )

        # Stream the results, yielding after every word.
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer_text = item.choices[0].delta.content
                # Ensure answer_text is not None before concatenation
                if answer_text is not None:
                    self.chats[self.current_chat][-1].answer += answer_text
                else:
                    # Handle the case where answer_text is None, perhaps log it or assign a default value
                    # For example, assigning an empty string if answer_text is None
                    answer_text = ""
                    self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield

        # Toggle the processing flag.
        self.processing = False

    async def gpt4all_local(self, question: str):
        # Add the question to the list of questions.
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)

        # Clear the input and start the processing.
        self.processing = True
        yield

        # Build the messages.
        """
        messages = [
            {
                "role": "system",
                "content": "A chat between Lawrence and Lucy an artificial intelligence assistant.\n",
            }
        ]
        """
        messages = [
            {
                "A chat between Lawrence and Lucy an artificial intelligence assistant.\n\n"
            }
        ]

        for qa in self.chats[self.current_chat]:
            # messages.append({"role": "user", "content": qa.question})
            # messages.append({"role": "assistant", "content": qa.answer})
            messages.append({qa.question})
            messages.append({qa.answer})

        # Remove the last mock answer.
        messages = messages[:-1]

        model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
        # model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
        model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
        model = GPT4All(model_name=model_name, model_path=model_path)
        system_template = 'A chat between Lawrence and Lucy an artificial intelligence assistant.\n'
        # prompt_template = f'USER: \n\nASSISTANT: \n\n'
        tokens = []
        with model.chat_session(system_template):
            for token in model.generate(f"{qa.question}", max_tokens=900, streaming=True):
                tokens.append(token)
                # print(tokens)
                self.chats[self.current_chat][-1].answer += token
                self.chats = self.chats
                yield

        print(f"Question Asked: {qa.question}\n\n")
        print(f"Answer Given: {qa.answer}\n\n")

        # Creating Chat History
        # f = open("incremental_name.txt", "x")
        f = open("chat_history.txt", "a")
        f.write(f"Question Asked: {qa.question}\n\n")
        f.write(f"Answer Given: {qa.answer}\n\n")

        # Toggle the processing flag.
        self.processing = False
        # print(self.chats)

