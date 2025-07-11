# 🏃‍♂️ Strava Flask Viewer

**A local Flask app to fetch, cache, and display your Strava activities — sortable, clickable, and beautiful.**  
Supports heart rate, speed, distance, and more.

---

## 🚀 Features

- ✅ OAuth2 authorization with Strava
- 🧠 Caches all activities to avoid API rate limits
- 📊 Sortable table by date, distance, speed, heart rate
- 🔗 Clickable activity links (opens on Strava)
- 🧪 Useful for testing, analysis, or just data nerds
- 💾 Easy to run locally with Python

---

## 📦 Quick Start

To get started, follow the step-by-step instructions in:

👉 [`GUIDE.md`](GUIDE.md)

---

## 🛠 Tech Stack

- Python 3
- Flask
- Jinja2 Templates
- Strava API v3

---

## 📁 Project Structure

```
📦 strava-flask-viewer/
├── main.py                  # Main Flask app
├── json/
│   ├── data.json               # Your Strava credentials (not committed)
│   └── activities_cache.json   # Cached data
├── templates/
│   └── index.html          # HTML template for activity list
├── GUIDE.md   # Setup instructions
└── README.md               # You're here!
```

---

## 🧑‍💻 Author

Made with ❤️ by a Strava user for Strava users.  
Pull requests welcome!

---

## 📄 License

MIT License
