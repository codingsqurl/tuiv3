from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Digits, Header, Footer
from datetime import datetime

class TuiApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="question_mark", action="help", description="Show help screen", key_display="?"),
        Binding(key="d", action="delete", description="Delete"),
        Binding(key="j", action="down", description="Scroll down", show=False),
        Binding(key="r", action="reload", description="Reload")
    ]

    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Digits("", id="clock")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "TU-DEWI"
        self.sub_title = "A DEVS FOCUS TUI"
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")

if __name__ == "__main__":
    app = TuiApp()
    app.run()
