import reflex as rx
import sys


class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


class State(rx.State):
    # The current question being asked.
    question: str

    chats: dict[str, list[QA]]

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot is not very smart right now...
        print(self.question)
        answer = lucy_gpt_local(query=self.question)
        self.chat_history.append((self.question, answer))

        # answer = self.lucy_gpt_local_testing(query=self.question)

        self.question = ""

    def lucy_gpt_local_testing(self, query: str):
        from pathlib import Path
        from gpt4all import GPT4All

        # Add the question to the list of questions.
        qa = QA(question=query, answer="")
        State.chats[State.current_chat].append(qa)

        # Clear the input and start the processing.
        State.processing = True
        yield

        model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
        # model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
        model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
        model = GPT4All(model_name=model_name, model_path=model_path)
        system_template = 'A chat between Lawrence and Lucy an artificial intelligence assistant.\n'
        tokens = []
        with model.chat_session():
            for token in model.generate(f"{query}", streaming=True):
                tokens.append(token)
        print(tokens)
        State.chats[State.current_chat][-1].answer += tokens
        yield


def lucy_gpt_local(query):
    from pathlib import Path
    from gpt4all import GPT4All

    model_name = 'Meta-Llama-3-8B-Instruct.Q4_0.gguf'
    # model_name = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
    model_path = Path.home() / 'Library/Application Support/nomic.ai/GPT4All/'
    model = GPT4All(model_name=model_name, model_path=model_path)
    system_template = 'A chat between a curious user and Lucy an artificial intelligence assistant.\n'

    with model.chat_session(system_template):
        response1 = model.generate(prompt=f'{query}')
        print(response1)
        print()
        return f"{response1}"
