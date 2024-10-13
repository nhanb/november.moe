# Depends on bottle.py 0.12, gunicorn & sqlite3, all of which come with debian bookworm:
#   sudo apt install python3-bottle python3-gunicorn sqlite3
# Then simply run `python3 wishes.py`.
# This script needs read/write access to a `wishes.db` file in the working dir.
# Intentionally single-threaded so we don't have to care about concurrent db access.
import os
import sqlite3

from bottle import default_app, get, post, request, response

WISHES_DEBUG = bool(os.environ.get("WISHES_DEBUG", False))
WISHES_HOST = os.environ.get("WISHES_HOST", None) or "localhost"
WISHES_PORT = int(os.environ.get("WISHES_PORT", None) or 9000)
DB = "wishes.db"


app = default_app()

con = sqlite3.connect(DB)
con.execute("""\
CREATE TABLE IF NOT EXISTS wishes (
    id integer primary key,
    name text,
    content text,
    ip text,
    created_at text default (datetime('now')),
    approved boolean default false
);
""")
con.close()


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers["Access-Control-Allow-Origin"] = "https://november.moe"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = (
            "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"
        )

        if request.method != "OPTIONS":
            return fn(*args, **kwargs)

    return _enable_cors


@get("/")
@enable_cors
def list_wishes():
    con = sqlite3.connect(DB)
    wishes = [
        {
            "name": name,
            "content": content,
            "created_at": created_at,
        }
        for name, content, created_at in con.execute(
            "SELECT name, content, created_at "
            "FROM wishes "
            "WHERE approved IS TRUE "
            "ORDER BY created_at DESC;"
        )
    ]
    con.close()

    return {"wishes": wishes}


@post("/")
@enable_cors
def submit_wish():
    inputs = request.json or {}
    name = inputs.get("name", "").strip()
    content = inputs.get("content", "").strip()

    if not name or not content:
        response.status = 400
        return {"error": "plz do better kthxbye"}

    ip = (
        request.environ.get("HTTP_X_FORWARDED_FOR")
        or request.environ.get("REMOTE_ADDR")
        or "unknown"
    )

    con = sqlite3.connect(DB)
    con.execute(
        "INSERT INTO wishes(name, content, ip) VALUES (?, ?, ?)",
        (name, content, ip),
    )
    con.commit()
    con.close()

    return {}
