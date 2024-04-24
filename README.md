### Coding Challenge Manager with Fraud Detection

This Django project is a web-based application designed to manage user authentication, user registration, and host a series of coding challenges. The project also features a leaderboard system and fraud detection mechanism. Users can register, login, solve programming questions, and their scores are updated on a leaderboard accordingly. If fraudulent activity is detected, the user is redirected to a fraud page and logged out.

### Features

- **User Authentication:** Support for user login and logout functionality.
- **User Registration:** Allows new users to create an account by providing basic information like username, first name, last name, and password.
- **Coding Challenges:** Users can access and solve programming challenges. Each solution is tested against pre-defined test cases.
- **Leaderboard:** Displays the top scores in descending order, showcasing the best performances.
- **Fraud Detection:** Detects and handles fraudulent attempts by users during the participation in challenges.
- **Dynamic Content Handling:** The application dynamically handles content such as questions and test cases for challenges.

### Technology Stack

- **Python:** The primary programming language used.
- **Django:** The web framework for building the web application.
- **SQLite:** Default database used by Django for storing user data and challenge details.
- **HTML/CSS:** Used for designing and structuring the web pages.
- **JavaScript (optional):** Could be integrated for enhancing front-end interactivity.

### Setup and Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/krishnateja-81/contest
   ```

2. **Create a Virtual Environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the Database:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server:**
   ```
   python manage.py runserver
   ```

6. **Access the Application:**
   Open a browser and go to `http://127.0.0.1:8000/`.

### Pages and Routes

- **Login Page (`/login/`):** Handles user authentication.
- **Register Page (`/register/`):** Allows new users to register.
- **Landing Page (`/landing/`):** Main page after login, displays dynamic content.
- **Questions Page (`/questions/`):** Lists all the coding questions available.
- **Leaderboard Page (`/leaderboard/`):** Displays the leaderboard.
- **Fraud Page (`/fraud/`):** Informs the user about detected fraudulent activity.

### Security and Performance Considerations

- Ensure that user data is securely handled to prevent common vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).
- Use Django’s built-in decorators and functionalities to manage user sessions and authenticate requests.
- Optimize database queries to improve the performance of the application, especially when scaling up.

### Conclusion

This project is an excellent starting point for developers looking to understand user management, dynamic content handling, and basic game mechanics within a web application context using Django. It also provides a solid foundation for extending features such as adding more complex challenge mechanisms or integrating advanced fraud detection systems.
