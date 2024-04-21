# ATM app simulator

This is a simple ATM simulator built using Streamlit, a Python library for creating web applications.

## Features

- Simulates basic ATM functionalities such as checking balance, depositing money, and withdrawing money.
- Users can enter their card number and PIN to access their account.
- Users can choose from different options presented in the UI to perform ATM operations.

## Installation

1. Clone this repository:

    ```
    git clone <repo>
    ```

2. Install the required dependencies:

    ```
    pip install streamlit
    ```

3. Run the Streamlit app:

    ```
    streamlit run atm_app.py
    ```

4. Access the app in your browser at the provided URL (typically http://localhost:8501).

## Usage

1. Enter your card number in the input field provided.
2. Enter your PIN in the text box and press Enter.
3. Once the PIN is accepted, you will be presented with options to check balance, deposit money, or withdraw money.
4. Select the desired option and follow the instructions on the screen.


## Bank Accounts

The following bank accounts are available in the simulator:

1. Card Number: 1234, PIN: 4321, Initial Balance: $1000
2. Card Number: 5678, PIN: 8765, Initial Balance: $1500
3. Card Number: 9012, PIN: 2109, Initial Balance: $2000
4. Card Number: 3456, PIN: 6543, Initial Balance: $2500
5. Card Number: 7890, PIN: 0987, Initial Balance: $3000
6. Card Number: 2345, PIN: 5432, Initial Balance: $3500
7. Card Number: 6789, PIN: 9876, Initial Balance: $4000
8. Card Number: 0123, PIN: 3210, Initial Balance: $4500
9. Card Number: 4567, PIN: 7654, Initial Balance: $5000
10. Card Number: 8901, PIN: 1098, Initial Balance: $5500

## Example usage


1. Checking the balance:

![Image Alt Text](/imgs/streamlit1.png)

2. Depositing amount

![Image Alt Text](/imgs/streamlit2.png)

3. Withdrawing amount

![Image Alt Text](/imgs/streamlit3.png)


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
