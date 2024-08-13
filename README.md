# Bank Simulation GUI

## Overview

The **Bank Simulation GUI** is a Python application using Tkinter that simulates basic banking functionalities. This project includes a graphical user interface (GUI) for user account management, including sign-up and sign-in features. Users can create accounts, sign in, and manage their balances.

**Note:** This project is a work in progress, and major changes to the GUI design and functionality may occur.

## Features

1. **Welcome Page:**
   - Username and password entry fields.
   - A "Log In" button to access the main menu.
   - A "Sign Up" button to open a new sign-up window.

2. **Sign-Up Window:**
   - Entry fields for username, password, and confirm password.
   - Validation checks to ensure all fields are filled, passwords match, and username is unique.
   - Stores user information in an `accounts.txt` file.

3. **Main Menu:**
   - Options to create a deposit, withdraw money, check balance, or exit (not yet implemented in this version).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/Campeon254/Bank-Simulation](https://github.com/Campeon254/Bank-Simulation)
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd bank-simulation
   ```

3. **Ensure you have Python 3.x installed.**

4. **Install Tkinter (if not already installed):**
   Tkinter is included with Python standard library, but if you encounter issues, you can install it using your package manager (e.g., `sudo apt-get install python3-tk` for Debian-based systems).

## Usage

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Main Window:**
   - Enter your username and password.
   - Click "Log In" to access the main menu (to be implemented).
   - Click "Sign Up" to open the sign-up window.

3. **Sign-Up Window:**
   - Enter a username, password, and confirm password.
   - Click "Submit" to create a new account.

4. **Account Storage:**
   - User information is stored in `accounts.txt` in the format `username:password:balance`.

## File Structure

- `main.py`: Main application file containing the Tkinter GUI code.
- `accounts.txt`: File to store user credentials and balances.
- `README.md`: This file.

## Future Enhancements

- Implement functionality for depositing, withdrawing, and checking balance.
- Add error handling and security features (e.g., password hashing).
- Improve GUI design and user experience.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please ensure your code adheres to the project's style guidelines and includes appropriate documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
