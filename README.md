# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
2. **Install dependencies:**:
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**:
   Note - Starting from root directory
4. ```commandline
   cd backend
   uvicorn server:app --reload
   ```

5. **Run the Streamlit app:**:
   Note - Starting from root directory
   ```commandline
    streamlit run frontend/app.py
   ```

## Screenshots of project Interface
