"""
Section 7 exercise
"""


def calculate_income_after_taxes(gross_income, state):

    state_tax = {"CA": 10, "NY": 9, "TX": 8, "NJ": 6}
    net = gross_income - (gross_income * .10)

    if state in state_tax:
        net = net - (gross_income * state_tax[state] / 100)
        print(f"Your net income after all the taxes is {net}")
        return net
    else:
        print(f"{state} State is not on the list.")
        return None


gross_income_input = int(input("Enter your gross income: "))
designated_state = str(input("Enter your State: "))


calculate_income_after_taxes(gross_income_input, designated_state)

