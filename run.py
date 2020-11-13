from blog import app

ap = app.create_app()

if __name__ == '__main__':
    ap.run()