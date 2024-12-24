# GiftHubApp

GiftHubApp is a unique web platform designed to inspire thoughtful gifting by sharing real-world gift ideas. Users can post, browse, and organize gifts for various occasions, making it easier to choose the perfect gift.

## Features

### User Features
- **User Registration and Authentication**
  - Secure user registration system with hashed password storage.
  - Login functionality with detailed error handling.
  
- **User Profiles**
  - Custom user fields: age and gender.
  - Personalized experience for gift exploration.

### Gift Management
- **Post Gift Ideas**
  - Add details like title, description, and image uploads.
  - Categorize gifts by tags and occasions.

- **Explore and Search Gifts**
  - Browse gift ideas shared by others.
  - Search and filter by tags, sender, receiver, or occasions.

### Social and Sharing Features
- **Gift Inspiration**
  - Discover trending gifts and curated lists.
  - Save ideas for future occasions.

## Installation

### Prerequisites
- Python (3.8 or higher)
- Pip (Python package manager)
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gifthubapp.git
   cd gifthubapp
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`.

## Usage

1. **Register an Account**: Create an account using the `/register/` endpoint or the registration page.
2. **Log In**: Authenticate using the `/login/` endpoint.
3. **Post a Gift**: Share a gift idea with a title, description, and image.
4. **Explore Gifts**: Browse and filter gifts shared by others for inspiration using `gifts/`.

## Contribution

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a meaningful message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.


## NOTE
- This is just backend API, Frontend is built in another repo