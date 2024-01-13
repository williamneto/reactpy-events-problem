from reactpy import component, run, html, use_state
from custom import text_field

@component
def app():
    text, set_text = use_state("")

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