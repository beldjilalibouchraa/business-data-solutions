# Sales Data Cleaning Example

## What This Does
Cleans messy sales data:
1. Standardizes customer names to Title Case
2. Removes $ symbols from amounts
3. Converts regions to uppercase
4. Exports clean Excel file

## Files
- `messy_sales.csv` - Original messy data
- `cleaner.py` - Python cleaning script  
- `cleaned.xlsx` - Clean result (open in Excel)

## How to Run
```bash
pip install pandas openpyxl
python cleaner.py
