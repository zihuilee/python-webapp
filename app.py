import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    appruner = web.AppRunner(app)
    await appruner.setup()
    srv = await loop.create_server(appruner.server, '127.0.0.1', 8000)
    logging.info('server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()