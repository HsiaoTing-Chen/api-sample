#!/usr/bin/env python3

import websocket
import json
from utils import get_env_info, get_spot_ws_url


def on_message(ws, message):
    print(json.dumps(json.loads(message), indent=2))


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### socket closed ###")


def on_open(ws):
    payload = {
        "op": "subscribe",
        "args": ["orderBookApi:BTC-USD_0"],
    }
    ws.send(json.dumps(payload))


if __name__ == "__main__":
    # websocket.enableTrace(True)
    env = get_env_info()
    ws = websocket.WebSocketApp(
        get_spot_ws_url(env["WS_HOST"]),
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()
