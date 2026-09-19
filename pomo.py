from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header

class TimeDisplay(Digits):
    remaining_time = reactive(25 * 60)
    running = False

    def on_mount(self) -> None:
        #creates new paused timer that calls self.tick function every 1 second and saves it to the self.timer variable
        self.timer = self.set_interval(1, self.tick, pause=True)

    def toggle(self) -> None:
        if self.running:
            self.timer.pause()
        else:
            self.timer.resume()
        self.running = not self.running

    def tick(self) -> None:
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.pause()
            self.running = False

    def watch_remaining_time(self, value: int) -> None:
        minutes, seconds = divmod(value, 60)
        self.update(f"{minutes:02}:{seconds:02}")

    def reset(self) -> None:
        self.timer.pause()
        self.running = False
        self.remaining_time = 25 * 60


class PomoTimer(App):
    BINDINGS = [
        Binding("space", "toggle_timer", "Start/Pause"),
        Binding("r", "reset_timer", "Reset the timer"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TimeDisplay()
        yield Footer()

    def action_toggle_timer(self) -> None:
        self.query_one(TimeDisplay).toggle()

    def action_reset_timer(self) -> None:
        self.query_one(TimeDisplay).reset()


if __name__ == "__main__":
    app = PomoTimer()
    app.run()
