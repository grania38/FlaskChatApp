from website import socketio, create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)       # Every change in the source code the web server will be automatically rerun


