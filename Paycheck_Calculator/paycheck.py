import sys

def calc_paycheck(hours, hourly_wage):
    tax_chunk = hours * hourly_wage * 0.173
    investment_chunk = hours * hourly_wage * 0.08

    print(f"Investment: ${investment_chunk:.2f}")
    return (hours * hourly_wage) - tax_chunk - investment_chunk



if __name__ == "__main__":
    hours = float(sys.argv[1])
    hourly_wage = float(sys.argv[2])
    total = calc_paycheck(hours, hourly_wage)

    print(f"Check: ${total:.2f}")


