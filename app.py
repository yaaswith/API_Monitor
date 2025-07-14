from flask import Flask, jsonify, send_from_directory
import random
import datetime

app = Flask(__name__)

# Simulated metrics data
def get_metrics():
    return {
        "activeFor": random.choice(["11 hours", "12 hours", "11 hours 10 minutes", "11 hours 30 minutes"]),
        "lastCheck": random.choice(["20 seconds ago", "30 seconds ago", "10 seconds ago", "1 minute ago"]),
        "responseTime": f"{random.randint(190, 250)} ms",
        "certExpiry": "Aug 28, 2025 7 PM",
        "totalChecks": random.randint(50, 60),
        "uptimePercent": f"{random.uniform(83.0, 87.0):.1f} %",
        "incidents": random.randint(5, 12),
        "avgResponseTime": f"{random.randint(220, 240)} ms"
    }

@app.route('/')
def serve_dashboard():
    return send_from_directory('.', 'index.html')

@app.route('/api/metrics')
def metrics():
    return jsonify(get_metrics())

# Optional: serve CSS/JS files if moved external
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
