# analyzer.py - analysis logic for the CLI Data Analyzer 
def analyze_numbers(numbers):
    # Return count, min, max, sum, average in a dictionary
    if not numbers:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "sum": 0,
            "average": None
        }
    
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }