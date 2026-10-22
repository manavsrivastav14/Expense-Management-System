from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List

import db_helper

from pydantic import BaseModel

class DateRange(BaseModel):
    start_date: date
    end_date: date

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()

# Run backend with command: uvicorn server:app --reload

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

    # return f"Received get_expense request for {expense_date}"

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    # previous_existing_expenses = db_helper.fetch_expenses_for_date(expense_date)
    # if previous_existing_expenses:
    #     db_helper.delete_expense_for_date(expense_date)
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

@app.post("/analytics/category")
def get_analytics_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch expense data from database")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = round((row['total']/total)*100 if total !=0 else 0,2)

        breakdown[row['category']] = {
            'total': row['total'],
            'percentage':f"{percentage}%"
        }
    return breakdown

@app.get("/analytics/months")
def get_analytics_months():
    data = db_helper.fetch_all_expenses_and_group_by_months()

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch expense data from database")

    return data
