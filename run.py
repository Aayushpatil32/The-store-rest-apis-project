from app import create_app, db  # Remove socketio import

app = create_app()  # Modify create_app() to not return socketio

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)  # Replace socketio.run with app.run