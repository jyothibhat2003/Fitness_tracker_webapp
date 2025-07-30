# Fitness Tracker Web App

A web application built with **Django** to centrally and efficiently track your workout progress, body weight, caloric intake, and body measurements.

## Key Features

1. **Exercise Tracking with GIFs**

   - Embed custom GIFs generated from YouTube to illustrate each movement.
   - Lazy loading and file optimization for fast performance.

2. **Automated Weight Progression**

   - Smart load-increase suggestions based on completed reps and RPE (Rate of Perceived Exertion).

3. **Body Weight Logging**

   - Record daily or monthly weight and visualize trends with line charts.

4. **Calorie Intake Tracking**

   - Integration options:
     - Python scraping via the `myfitnesspal` library.
     - Manual CSV upload exported from MyFitnessPal and processing with pandas.
     - Nutritionix API (free tier available).

5. **Effort Survey (RPE)**

   - Prompt for perceived exertion (1–10 scale) after each set to fine-tune recommendations.

6. **Monthly Body Measurements**

   - Form to submit measurements (chest, waist, hips, arms, legs).
   - Evolution charts and alerts for significant changes.

## Tech Stack

- **Framework:** Django 4.x
- **ORM & Migrations:** Django ORM, django-environ
- **Templates & Static:** Django templates, Bootstrap 5, Chart.js
- **Data Processing:** pandas, myfitnesspal (optional)
- **Deployment:** Heroku (Gunicorn), GitHub

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd fitness_project
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   venv\Scripts\activate.bat     # Windows CMD
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables** in a `.env` file:
   ```text
   SECRET_KEY=your_secret_key
   DEBUG=True                # switch to False in production
   ALLOWED_HOSTS=localhost   # comma-separated
   DATABASE_URL=sqlite:///db.sqlite3  # or your DATABASE_URL
   ```
5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser** for admin:
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
8. **Open in your browser** at `http://127.0.0.1:8000/`

## Recommended License

We recommend the **MIT License** for this project. It’s a permissive open-source license that allows reuse, modification, and distribution — including for commercial purposes — provided the original copyright notice is retained.

---

Ready to launch your Django-based fitness tracking app! 🚀

