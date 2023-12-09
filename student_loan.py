# interest rates for plan 5
interest_current = 1.075
interest_max = 1.135
repayment_time_years = 40
money_to_pay_off = 0
m_l = 9125
y_val = 9250 + m_l
eou_val = 0
for i in range(4):
    y_val_int = y_val * interest_current
    eoy_val = y_val_int + y_val
    eou_val += eoy_val

print(eou_val)

# am_val = (eou_val * interest_current) + 12500


def beat_student_loan(interest_rate, cur_loan_val, yearly_paying, nine_per_pay):
    for year in range(40):
        new_cur_loan_val = (cur_loan_val * interest_rate) - yearly_paying - nine_per_pay
        if new_cur_loan_val < 0:
            print(year * (yearly_paying + nine_per_pay))
            return print(f"you will pay off your loan in {year} years")
        else:
            cur_loan_val = new_cur_loan_val
    return print("you will never pay off your loan")


beat_student_loan(1.075, 152512.5, 0, 765)
