from flask import Flask, render_template
from system_metrics import get_system_metrics

app = Flask(__name__)

@app.route('/')
def index():
    # Get metrics from system_metrics.py
    metrics = get_system_metrics()
    # Render the HTML template and pass the metrics to it
    return render_template('index.html', metrics=metrics)

if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)
