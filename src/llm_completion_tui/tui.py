import asyncio
from typing import ClassVar

from textual.app import App
from textual.binding import Binding, BindingType
from textual.containers import Horizontal, Vertical
from textual.scroll_view import ScrollView
from textual.widgets import (
    Footer,
    Header,
    Input,
    Label,
    LoadingIndicator,
    Markdown,
)


class QueryApp(App[None]):
    TITLE = "Query Interface"

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("escape", "cancel", "Cancel"),
    ]

    DEFAULT_CSS = """
    Screen {
        align: center middle;
        hatch: right $foreground 10%;
    }

    .modal {
        width: 60;
        max-height: 30;
        height: auto;
        padding: 1 2;
        background: $surface;
        border: tall $primary;
    }

    #header {
        height: 1;
        width: auto;
        margin-bottom: 1;
    }

    .title {
        text-style: bold;
        padding: 0 1;
        width: 1fr;
    }

    Input {
        margin: 1 0;
        height: 1;
        border: tall $primary-darken-2;
        width: 1fr;
        transition: background 80ms linear, border 80ms linear;
    }

    Input.invalid {
        background: $error-muted;
        border: tall $error;
    }

    ScrollView#response-scroller {
        height: auto;
        min-height: 10;
        max-height: 24;
        width: 100%;
        border: tall $primary-darken-2;
        background: $primary-muted;
        margin: 1 0;
        display: none;
    }

    Markdown#response {
        width: 100%;
        color: $text;
        padding: 0 1;
    }

    #keys {
        margin-top: 1;
        height: auto;
        color: $text-muted;
        text-align: center;
    }

    #loading-indicator {
        display: none;
    }
    """

    def on_mount(self) -> None:
        self.response_count = 0
        self.theme = "nord"
        self.query_one(Input).focus()

    def compose(self):
        yield Header()
        with Vertical(classes="modal"):
            with Horizontal(id="header"):
                yield Label("Query Interface", classes="title")
            with ScrollView(id="response-scroller"):
                yield Markdown("", id="response")
            yield Input(placeholder="Type here...")
            yield LoadingIndicator(id="loading-indicator")
            yield Label("Press Enter to submit", id="keys")
        yield Footer()

    async def flash_input(self, times: int = 1) -> None:
        """Flash the input field to indicate invalid input.

        Args:
            times: Number of times to flash the field

        Verified in:
        - Source: src/textual/css/transition.py
        - Version: v2.1.2
        """
        input = self.query_one(Input)
        for _ in range(times):
            input.add_class("invalid")
            await asyncio.sleep(0.1)  # 100ms for transition
            input.remove_class("invalid")
            if (
                _ < times - 1
            ):  # Add a small pause between flashes, except after the last one
                await asyncio.sleep(0.1)

    async def on_input_submitted(self) -> None:
        input = self.query_one(Input)
        loading = self.query_one(LoadingIndicator)
        response = self.query_one("#response", Markdown)
        response_scroller = self.query_one(
            "#response-scroller", ScrollView
        )  # Fixed typo in ScrollView
        keys = self.query_one("#keys", Label)

        raw_input = input.value

        # Handle whitespace-only input with visual feedback
        if raw_input and not raw_input.strip():
            await self.flash_input(times=2)  # Flash twice
            return

        # Handle empty input (no whitespace)
        if not raw_input:
            if response.display:
                self.action_accept()
            else:
                await self.flash_input(times=2)  # Flash twice
                return

        # Sanitize input for non-empty, non-whitespace case
        sanitized_input = " ".join(raw_input.split())
        input.value = sanitized_input

        if response_scroller.display:
            # Non-empty input with response showing -> refine
            self.action_refine()
            return

        # First submission with valid input
        input.display = False
        loading.display = True
        keys.update("Processing...")

        await asyncio.sleep(1.5)

        loading.display = False
        self.response_count += 1
        response_scroller.display = True
        response.update(
            "# Example Long Response\n\n"
            "This is a long response to test scrolling behavior.\n\n"
            "## Code Example\n\n"
            "```python\ndef example_function():\n    print('Testing scroll')\n    for i in range(10):\n        print(f'Line {i}')\n```\n\n"
            "## List Items\n\n"
            "* Item 1 with details\n* Item 2 with more information\n* Item 3 with extended description\n\n"
            "## Additional Section\n\n"
            "More content to demonstrate scrolling capability.\n\n"
            "### Final Notes\n\n"
            "1. First note with details\n2. Second note with explanation\n3. Third note with more text\n"
            "4. Fourth item continuing\n5. Fifth item here\n"
        )
        keys.update("Press Enter to accept, type to refine, or [Esc] to cancel")
        input.value = ""
        input.display = True
        input.focus()

    def action_cancel(self) -> None:
        self.app.exit()

    def has_response(self) -> bool:
        return self.response_count > 0

    def action_accept(self) -> None:
        if self.has_response():
            self.app.exit()

    def action_refine(self) -> None:
        if self.has_response():
            input = self.query_one(Input)
            response = self.query_one("#response", Markdown)
            response_scroller = self.query_one("#response-scroller", ScrollView)

            input.display = True
            response_scroller.display = False
            response.update("")
            self.query_one("#keys", Label).update("Press Enter to submit")
            input.focus()


if __name__ == "__main__":
    app = QueryApp()
    app.run()
