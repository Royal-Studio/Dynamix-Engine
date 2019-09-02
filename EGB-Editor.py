from webview import create_window, start

window = create_window("EGB-ENGINE", url="http://127.0.0.1:5000",
    width=1400, height=950, resizable=False, confirm_close=True)

start(window)