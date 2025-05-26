from flask import Flask, request
import json
import datetime

# pip install flask --break-system-packages
# mkdir /usr/local/bin/csp_receiver
# nano /usr/local/bin/csp_receiver/csp_receiver.py
# copy, paste & save this
# chmod +x /usr/local/bin/csp_receiver/csp_receiver.py
# chown www-data:www-data /usr/local/bin/csp_receiver/csp_receiver.py

app = Flask(__name__)

# save into log
LOGFILE = "/var/log/csp-violations.log"

@app.route('/csp-violation', methods=['POST'])
def csp_violation():
    try:
        report_data = request.get_json()
        timestamp = datetime.datetime.utcnow().isoformat()

        with open(LOGFILE, "a") as log:
            log.write(f"[{timestamp}] {json.dumps(report_data)}\n")

        return '', 204
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
