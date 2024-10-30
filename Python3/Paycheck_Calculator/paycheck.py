import sys

def calc_paycheck(hours):
    hourly_wage = 25
    tax_chunk = hours * hourly_wage * 0.173
    investment_chunk = hours * hourly_wage * 0.08

    return (hours * hourly_wage) - tax_chunk - investment_chunk


if __name__ == "__main__":
    hours = int(sys.argv[1])
    total = calc_paycheck(hours)

    print(f"${total:.2f}")


