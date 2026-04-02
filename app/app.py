from flask import Flask, Response, render_template_string
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests to the app"
)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS DevOps Starter</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 30px;
        }

        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.35);
            backdrop-filter: blur(10px);
        }

        .badge {
            display: inline-block;
            background: #22c55e;
            color: #08110b;
            font-weight: bold;
            padding: 8px 14px;
            border-radius: 999px;
            margin-bottom: 20px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        p {
            font-size: 1.1rem;
            line-height: 1.7;
            color: #e2e8f0;
            margin-bottom: 20px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 18px;
            margin-top: 30px;
        }

        .card {
            background: rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 20px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .card h3 {
            margin-bottom: 10px;
            color: #93c5fd;
        }

        .card p {
            font-size: 0.95rem;
            margin-bottom: 0;
            color: #cbd5e1;
        }

        .buttons {
            margin-top: 30px;
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
        }

        .btn {
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 10px;
            font-weight: bold;
            transition: 0.2s ease;
        }

        .btn-primary {
            background: #3b82f6;
            color: white;
        }

        .btn-secondary {
            background: #111827;
            color: #f8fafc;
            border: 1px solid #475569;
        }

        .btn:hover {
            transform: translateY(-2px);
            opacity: 0.95;
        }

        .footer {
            margin-top: 30px;
            font-size: 0.95rem;
            color: #94a3b8;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">● Live on AWS EC2</div>
        <h1>AWS DevOps Starter Platform</h1>
        <p>
            This application is running successfully inside a Docker container on an EC2 instance
            provisioned with Terraform and integrated with Prometheus, Grafana, GitHub Actions,
            and Docker Hub.
        </p>
        
        <p><strong>Total Requests:</strong> {{ count }}</p>
        
        <div class="grid">
            <div class="card">
                <h3>Infrastructure</h3>
                <p>Provisioned with Terraform on AWS EC2.</p>
            </div>
            <div class="card">
                <h3>Containers</h3>
                <p>Application deployed using Docker and Docker Compose.</p>
            </div>
            <div class="card">
                <h3>Monitoring</h3>
                <p>Prometheus and Grafana are available for observability.</p>
            </div>
            <div class="card">
                <h3>CI/CD</h3>
                <p>Image build, scan, and push handled by GitHub Actions.</p>
            </div>
        </div>

        <div class="buttons">
            <a class="btn btn-primary" href="/metrics">View Metrics</a>
            <a class="btn btn-secondary" href="http://3.85.3.177:9090" target="_blank">Prometheus</a>
            <a class="btn btn-secondary" href="http://3.85.3.177:3000" target="_blank">Grafana</a>
        </div>

        <div class="footer">
            Built by Esther — AWS • Terraform • Docker • Monitoring • CI/CD
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    count = REQUEST_COUNT._value.get()
    return render_template_string(HTML_PAGE, count=count)

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)