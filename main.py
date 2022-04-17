# Press the green button in the gutter to run the script.
from service.budget_checker import BudgetChecker
from service.command.current_month_budget_command import CurrentMonthBudgetCommand

if __name__ == '__main__':
    BudgetChecker().check(CurrentMonthBudgetCommand.execute())
