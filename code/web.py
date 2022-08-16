from requestbin import config, app

if __name__ == "__main__":
    port = int(config.PORT_NUMBER)
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)
