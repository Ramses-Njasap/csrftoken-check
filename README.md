# CSRF Token Case Sensitivity Test

## Overview

This project is a simple Django application designed to test whether Django is case sensitive concerning the CSRF token header name. The project includes a Django backend that runs on port 8000 and a pure HTML frontend served on port 8001.

## Installation

### Prerequisites

- Python 3.x
- Django

### Setting Up the Django Backend

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    On windows

    ```bash
    venv\Scripts\activate
    ```

    On MacOs/Linux

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Start the Django Development Server**
    ```bash
    python3 manage.py runserver
    ```

    This runs on PORT 8000, if using a different port change the PORT in the html file as well


### Running the HTML Frontend

1. **Navigate To The Html (test.html) Directory**
    ```bash
    cd your-repo/csrftoken/csrftoken
    ```

2. **Serve the HTML File**
    ```bash
    python -m http.server <PORT>
    python -m http.server 8001
    ```

3. **Serve The Html File**
    Open:
    http://localhost:<PORT>/
    http://localhost:8001/