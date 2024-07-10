# Beans Search App

Welcome to the Beans Search App! This application helps you find the best Tully's Coffee beans based on your preferences. Simply enter your prompt, and our AI will recommend the perfect Tully's beans for you.

## Features

- **User-Friendly Interface**: Enter a prompt describing your taste preferences or coffee needs.
- **AI Recommendations**: Get personalized Tully's Coffee bean suggestions powered by OpenAI.

## Getting Started

Follow these steps to get the app up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- OpenAI API Key

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/geen100/beans_seach.git
    cd beans_seach
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API Key**:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API Key to the `.env` file:
      ```
      OPENAI_API_KEY=your_api_key_here
      ```

### Usage

1. **Run the application**:
    ```bash
    flask run
    ```

2. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

3. **Get Recommendations**:
    - Enter your coffee preferences in the prompt box.
    - Click the "Search" button to get your personalized Tully's Coffee bean recommendations.
