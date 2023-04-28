""" Webhook service for Chatwoot."""

import uvicorn
from woot import AsyncChatwoot
from typer import Typer
from typing import Dict
from woothook.utils import load_config
from fastapi import FastAPI, Response, status

app = Typer()


class WootHook:
    def __init__(self, config_file: str):
        self.config = load_config(config_file)
        self.chatwoot = AsyncChatwoot(
            chatwoot_url=self.config.chatwoot.url,
            access_key=self.config.chatwoot.access_key,
        )
        self.port = self.config.service.port
        self.host = self.config.service.host

        async def message_handler(request):
            await self.process_message(request)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        self.listener = FastAPI()
        self.listener.add_api_route("/", message_handler, methods=["POST"])

    async def process_message(self, request: Dict):
        # TODO: Implement your own logic here
        print(request)


@app.command()
def start(config_file: str):
    hook = WootHook(config_file)
    uvicorn.run(
        hook.listener, host=hook.host, port=hook.port
    )  # Change the host and port as per your requirements


if __name__ == "__main__":
    app()
