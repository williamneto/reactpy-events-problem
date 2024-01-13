from reactpy import component, run, html, use_state
from reactpy_events_problem import text_field

@component
def app():
    text, set_text = use_state("Text")

    return html.div(
        html.h1(text),
        text_field(
            attrs={
                "value": text,
                "onChange": lambda e: set_text(e["target"]["value"])
            }
        )
    )

run(app)