import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Use Environment Variables for the Database URL
# This is a major DevOps best practice!
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/dbname")


@app.route("/db-check")
def db_check():
    try:
        # Try to connect to the database
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "Connected", "db_version": db_version})
    except Exception as e:
        return jsonify({"status": "Error", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
