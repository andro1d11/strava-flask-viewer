# 🏃‍♂️ Strava Flask Viewer — Getting Started

This guide will help you set up the project, get your `client_id`, `client_secret`, and connect your Strava account to start viewing and analyzing your activities locally.

---

## ✅ 1. Requirements

- Python 3.7+
- `pip` (Python package installer)
- A [Strava](https://www.strava.com) account

Install dependencies:

```bash
pip install flask requests
```

---

## 🔑 2. Get Strava API credentials

1. Go to: [https://www.strava.com/settings/api](https://www.strava.com/settings/api)
2. Click **"Create & Manage Your App"**
3. Fill in:
   - **Application Name**: anything you like (e.g., "My Flask Viewer")
   - **Authorization Callback Domain**: `localhost` (required!)
4. After saving, you'll get:
   - **Client ID**
   - **Client Secret**

---

## 🧾 3. Create `data.json` file

In the root of the project folder, create a file named `data.json`:

```json
{
  "CLIENT_ID": "your_client_id_here",
  "CLIENT_SECRET": "your_client_secret_here"
}
```

Replace with actual values from step 2.

---

## 🚀 4. Start the Flask App

Run the Python script:

```bash
python main.py
```

This will:

- Open your browser
- Ask you to log in to Strava and authorize the app
- Redirect you to `http://localhost:5000/exchange_token`
- The app will receive the temporary `code` and exchange it for an `access_token`

---

## 🧠 What is the `code` and `access_token`?

- `code`: a **one-time authorization code** sent by Strava after user login.
- `access_token`: the actual token you use to access the Strava API.
  - It is stored **in memory only** unless you implement persistent storage.

---

## 📁 5. Caching your activities

Once authorized:

- The app will fetch **all your activities** from Strava using the API.
- They will be saved to `activities_cache.json` to avoid using daily API limits.
- To manually refresh from Strava, visit:  
  [http://localhost:5000/refresh](http://localhost:5000/refresh)

---

## 📊 6. View your activities

Visit:

```bash
http://localhost:5000/home
```

You’ll see:

- Date, name, distance
- Average and max speed (converted to km/h)
- Heart rate (if available)
- All columns are sortable!

---

## ♻️ 7. Authorize again?

If you restart the app and lost your `access_token`, just go to:

```
http://localhost:5000/authorize
```

It will open the Strava auth page again.

---

## ❓ Troubleshooting

- **403 error or empty activities**: check that you accepted permissions during authorization.
- **Missing heart rate**: only appears if activity contains HR data.
- **Still stuck?**  
  → [Strava API Docs](https://developers.strava.com/docs/getting-started/)

---

Made with ❤️ for cyclists, runners, and nerds.
