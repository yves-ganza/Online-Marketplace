# Online Marketplace

Welcome to the Online Marketplace project! This application allows sellers to list their items for sale and buyers to contact them directly through the platform.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contributing](#contributing)

## Features

- **User Authentication & Authorization**: Secure management of seller and buyer accounts.
- **Item Listings**: Sellers can add, update, and delete items for sale.
- **User Profiles**: Each user has a profile that displays their information and listings.
- **Messaging System**: Buyers can directly contact sellers through the app.
- **Responsive Design**: The front-end is designed with HTML, CSS, and Tailwind CSS for a seamless user experience.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yves-ganza/online-marketplace.git
   cd online-marketplace
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required packages
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```
4. Set up PostgreSQL database and update the settings in `settings.py`.
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create superuser(optional):
   ```bash
   python manage.py createsuperuser
   ```
7. Run development server:
   ```bash
   python manage.py runserver
   ```
8. Access the application in your browser

## Usage

Once the application is running, users can register as buyers or sellers. Sellers can add items to their listings, while buyers can browse items and message sellers for inquiries.

## Technologies Used

* Backend: Python, Django
* Database: PostgreSQL
* Frontend: HTML, CSS, Tailwind CSS
* Authentication: Django's built-in authentication system

## License
This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

