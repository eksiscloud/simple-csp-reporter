from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

LOGFILE = "/var/log/csp-violations.log"

@app.route("/", methods=["POST"])
@app.route("/csp-report", methods=["POST"])  # both endpoints
def csp_report():
    data = request.get_json(force=True, silent=True)

    if data:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "report": data
        }

        try:
            with open(LOGFILE, "a") as f:
                f.write(json.dumps(log_entry, indent=2) + "\n\n")  # empty line for netter readibility
            print("✅ Logging succesful:")
            print(json.dumps(log_entry, indent=2))
            return "OK", 200
        except Exception as e:
            print(f"🚨 Logging error: {e}")
            return "Internal Server Error", 500
    else:
        print("⚠️ CSP-raport faulty or missing JSON")
        return "Bad Request", 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
