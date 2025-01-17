# Techn-i-cal

Techn-i-cal is a pharmacy scheduling software designed to help manage employee schedules, shifts, and preferences. It provides an easy-to-use interface for creating and managing schedules, tracking employee availability, and handling PTO requests.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/jsteinbecker/techn-i-cal.git
   cd techn-i-cal
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file in the root directory of the project and add the following variables:
   ```
   OAI_API_KEY=<your_openai_api_key>
   DEEPGRAM_API_KEY=<your_deepgram_api_key>
   DJANGO_SETTINGS_MODULE=techn_i_cal.settings
   SECRET_KEY=<your_secret_key>
   DATABASE_URL=<your_database_url>
   ```

5. Apply the database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage Instructions

1. Access the admin panel:
   Open your web browser and go to `http://127.0.0.1:8000/admin`. Log in with the superuser credentials you created earlier.

2. Add employees, shifts, and other necessary data:
   Use the admin panel to add employees, shifts, and other necessary data for your scheduling needs.

3. Create and manage schedules:
   Use the provided interface to create and manage schedules, track employee availability, and handle PTO requests.

4. Monitor and adjust schedules as needed:
   Regularly monitor the schedules and make adjustments as needed to ensure optimal staffing and employee satisfaction.
