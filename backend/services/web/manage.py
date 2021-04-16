from wsgi import AppModule

app_module = AppModule()


if __name__ == '__main__':
    app_module.manager.run()
