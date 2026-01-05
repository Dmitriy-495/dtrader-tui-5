from textual.app import App, ComposeResult
from textual.widgets import Static


class BotApp(App):
    def compose(self) -> ComposeResult:
        yield Static("I'm BOT")


if __name__ == "__main__":
    BotApp().run()
