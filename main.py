import webbrowser
import requests
from flask import Flask, request, redirect, render_template
import json
import os


# Load Strava client credentials from JSON file
with open('json/data.json', 'r') as f:
    data = json.load(f)

CLIENT_ID = data.get("CLIENT_ID")
CLIENT_SECRET = data.get("CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:5000/exchange_token'

app = Flask(__name__)

# Access token stored temporarily in memory (can be persisted to disk)
access_token = None
CACHE_FILE = 'json/activities_cache.json'

# Open Strava authorization page in the browser
def open_strava_authorization():
    auth_url = (
        f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}"
        f"&response_type=code&redirect_uri={REDIRECT_URI}"
        f"&scope=read,activity:read"
    )
    webbrowser.open(auth_url)

# Fetch all user activities from Strava API with pagination
def get_all_activities(access_token):
    activities = []
    per_page = 200
    page = 1

    while True:
        print(f"[📄] Loading page {page}...")
        response = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers={"Authorization": f"Bearer {access_token}"},
            params={"per_page": per_page, "page": page}
        )
        page_data = response.json()

        if not page_data:
            break

        activities.extend(page_data)
        page += 1

    print(f"[✅] Total activities loaded: {len(activities)}")
    return activities

# Save activities to local JSON cache
def save_activities_cache(activities, filename=CACHE_FILE):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

# Load activities from local JSON cache
def load_activities_cache(filename=CACHE_FILE):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

# Handle OAuth token exchange
@app.route('/exchange_token')
def exchange_token():
    global access_token

    code = request.args.get('code')
    token_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=payload)
    data = response.json()

    access_token = data.get("access_token")
    print("[🔐] Access token obtained:", access_token)

    return redirect('/home')

# Display cached or fetched activities
@app.route('/home')
def home():
    global access_token

    if not access_token:
        return "Access token not found. Please authorize first."

    activities = load_activities_cache()
    if activities:
        print("[📁] Loaded activities from cache.")
    else:
        print("[🌐] No cache found, fetching from Strava API...")
        activities = get_all_activities(access_token)
        save_activities_cache(activities)

    return render_template('index.html', activities=activities)

# Refresh cache from Strava API
@app.route('/refresh')
def refresh():
    global access_token

    if not access_token:
        return "Access token not found. Please authorize first."

    activities = get_all_activities(access_token)
    save_activities_cache(activities)
    return redirect('/home')

# Index route with manual link to authorize
@app.route('/')
def index():
    return "<h2>Go to <a href='/authorize'>authorize with Strava</a></h2>"

# Trigger browser to open Strava authorization page
@app.route('/authorize')
def authorize():
    open_strava_authorization()
    return "Opening Strava authorization page..."

if __name__ == '__main__':
    print("🌐 Starting Flask server on port 5000...")
    open_strava_authorization()
    app.run(port=5000)
