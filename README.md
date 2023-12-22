# Laptop Recommendation Service

This project is a Laptop Recommendation Service that assists users in choosing the most suitable laptop based on their usage and budget preferences.  

## About

The Laptop Recommendation Service is designed to provide personalized laptop recommendations for different usage scenarios such as gaming, design, desk work, and engineering. It takes into account the user's specified price range and usage type to make relevant suggestions.


## Table of Contents

- [Authors](#authors)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)



# Authors

- Mohamed Habib Jaouadi
- Mouhib Mani

# Getting Started

## Prerequisites

Make sure you have the following installed:

- Python (version x.x.x)
- Flask (version x.x.x)
- Pandas (version x.x.x)
- Experta (version x.x.x) [if any other dependencies are required, list them here]

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/laptop-recommendation.git
   ```

2. Navigate to the project directory:

    ```bash
    cd laptop-recommendation
    ```

3. Install dependencies:

    ```bash
    pip install experta
    pip install flask
    pip install pandas
    ```

## Usage
1. Run the Flask application: `python app.py`
2. Open your web browser and go to `http://localhost:5000/` to access the Laptop Recommendation Service.
3. Fill in the form with your preferred usage and budget to get personalized laptop recommendations.

# Project Structure
- `app.py`: The main Flask application file.
- `recommendation_system/`: Contains the recommendation engine and rules.
- `models/`: Includes the `Dataset` class for handling the dataset.
- `templates/`: HTML templates for the web interface.

# Dependencies
- Flask 
- Pandas 
- Experta
