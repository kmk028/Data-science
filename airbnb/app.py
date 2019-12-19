from flask import Flask, request

def create_app():
    app = Flask(__name__)
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'airbnb predictive project'

    @app.route('/predict', methods=['POST'])
    def predict(name=None):
            name = name or request.values['user_name']
            try:
                if request.method == 'POST':
                    return name
            except Exception as e:
                message = f"Error adding: {e}"
    
    return app

