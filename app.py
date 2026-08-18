# © The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved

from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import boto3
import uuid
import subprocess

app = Flask(__name__, template_folder=".")

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    )

    # Enable only when your site is HTTPS-only
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )

    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

@app.route('/api/execute', methods=['POST'])
def execute():
    data = request.json
    code = data.get('code')
    is_cli = data.get('is_cli', False)
    
    try:
        if is_cli:
            result = subprocess.run(code, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return jsonify({'success': True, 'output': result.stdout})
            else:
                return jsonify({'success': False, 'error': result.stderr})
        else:
            exec(code, {'boto3': boto3, 'uuid': uuid})
            return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

