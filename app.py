from fastapi import FastAPI

from darthnall.api import DarthnallApi


class Darthnall:
    def __init__(self) -> None:
        self.api = DarthnallApi()
        return None

    def create_app(self) -> FastAPI:
        self._app = FastAPI()

        @self._app.get("v1/")
        def home() -> dict:
            return { "msg": "Homepage" }

        @self._app.get("v1/bot/{bot_id}")
        def get_bot(bot_id: int) -> dict:
            bot = self.api.get_bot_by_id(bot_id)
            return { "id": bot_id, "bot": bot }

        return self._app

    @property
    def app(self) -> FastAPI:
        return self.create_app()


app = Darthnall().app
