# chatapp.py

import reflex as rx
from Lucy_AI_ChatBot import Style, state


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=Style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=Style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            state.State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=state.State.question,
            placeholder="Ask a question",
            on_change=state.State.set_question,
            # style=Style.input_style,
            size='2',
            # on_key_down=state.State.search_on_key_down,
        ),
        rx.button(
            "Ask",
            on_click=state.State.answer,
            style=Style.button_style,
        ),
        type="submit",
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            background_color=rx.color("mauve", 1),
            color=rx.color("mauve", 12),
            min_height="100vh",
            align_items="stretch",
            spacing="0",
            # align="center",
        )
    )


app = rx.App()
app.add_page(index)
