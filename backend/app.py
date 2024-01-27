from flask import Flask
from routes import receiptsroutesobject  # Import the receiptsroutes blueprint

app = Flask(__name__)

# Register the receiptsroutes blueprint
app.register_blueprint(receiptsroutesobject, url_prefix='/receipts')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)