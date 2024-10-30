def calc_paycheck(hours):
    hourly_wage = 25
    tax_chunk = hours * hourly_wage * 0.173
    investment_chunk = hours * hourly_wage * 0.08

    return (hours * hourly_wage) - tax_chunk - investment_chunk

total = calc_paycheck(42)

print(f"${total}")
