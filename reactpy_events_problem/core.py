from pathlib import Path
from typing import Any
from reactpy.web.module import export, module_from_file
from reactpy import component

_js_module = module_from_file(
    "reactpy-events-problem",
    file=Path(__file__).parents[0] / "bundle.js"
)

new_text_field = export(_js_module, "TextField")

@component
def text_field(attrs: Any ={}):
    return new_text_field(attrs)