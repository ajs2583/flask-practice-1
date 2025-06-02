# Flask Practice App

This is a basic Flask app built for practice. It includes simple routes that:

- Render a home page
- Predict a person's age and gender based on their name using external APIs
- Display blog posts from a mock API

## How to Run

1. Install Flask and Requests:

    ```bash
    pip install flask requests
    ```

2. Run the server:

    ```bash
    python server.py
    ```

3. Open your browser and go to:

    ```
    http://127.0.0.1:5000/
    ```

## Routes

- `/` – Home page
- `/guess/<name>` – Predicts age and gender
- `/blog/<num>` – Shows mock blog posts

---

Just a fun little practice project!
