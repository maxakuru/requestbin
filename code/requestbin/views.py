from urllib.parse import urlparse
import os
from flask import session, request, render_template, make_response

from requestbin import app, db, config

def update_recent_bins(name):
    if 'recent' not in session:
        session['recent'] = []
    if name in session['recent']:
        session['recent'].remove(name)
    session['recent'].insert(0, name)
    if len(session['recent']) > 10:
        session['recent'] = session['recent'][:10]
    session.modified = True


def expand_recent_bins():
    if 'recent' not in session:
        session['recent'] = []
    recent = []
    for name in session['recent']:
        try:
            recent.append(db.lookup_bin(name))
        except KeyError:
            session['recent'].remove(name)
            session.modified = True
    return recent

@app.endpoint('views.home')
def home():
    return render_template('home.html', recent=expand_recent_bins())


@app.endpoint('views.bin')
def bin(name):
    try:
        bin = db.lookup_bin(name)
    except KeyError:
        return "Not found\n", 404
    if request.query_string == 'inspect':
        if bin.private and session.get(bin.name) != bin.secret_key:
            return "Private bin\n", 403
        update_recent_bins(name)
        
        root_url = config.ROOT_URL
        if root_url is None:
            protocol=os.environ.get("PROTOCOL", "http")
            if host is None:
                if request.referrer:
                    host: str = request.referrer
                    url_parts = urlparse(request.referrer)
                    host = url_parts.hostname
                    protocol = url_parts.scheme
                else:
                    host = request.host
            root_url = f"{protocol}://{host}"
            
        return render_template('bin.html',
            bin=bin,
            root_url=root_url)
    else:
        db.create_request(bin, request)
        resp = make_response("ok\n")
        return resp


@app.endpoint('views.docs')
def docs(name):
    doc = db.lookup_doc(name)
    if doc:
        return render_template('doc.html',
                content=doc['content'],
                title=doc['title'],
                recent=expand_recent_bins())
    else:
        return "Not found", 404
