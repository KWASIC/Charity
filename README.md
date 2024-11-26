# Africa Charity Website

A Django-based charity website focused on facilitating donations for education, healthcare, and food initiatives in Africa.

## Features

- Donation system for multiple causes
- Project showcase for each category (Education, Healthcare, Food)
- Impact tracking and transparency
- Secure payment integration
- Mobile-responsive design

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `charity/` - Main Django project directory
- `donations/` - App handling donation logic
- `projects/` - App managing charity projects
- `static/` - Static files (CSS, JavaScript, Images)
- `templates/` - HTML templates
