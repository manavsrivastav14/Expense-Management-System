# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for backend.
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
   -- NOTE: starting from root directory
   ```commandline
   cd backend/
   uvicorn server:app --reload
   ```

4. **Run the Streamlit app:**:
   -- NOTE: starting from root directory
   ```commandline
    streamlit run frontend/app.py
   ```

## Screenshots of project Interface
<img width="1047" height="761" alt="Adding Expense" src="https://github.com/user-attachments/assets/0fec7361-fd82-48d8-b278-b03bd79a97ac" />
<img width="520" height="692" alt="Analysis by Category " src="https://github.com/user-attachments/assets/b2c099da-54c0-4c85-baab-85da9e30d65b" />
<img width="482" height="502" alt="Analysis By Month" src="https://github.com/user-attachments/assets/4050623f-d393-4a3d-b1f4-8d2187bb9391" />



