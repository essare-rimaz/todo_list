run with
`fastapi dev .\todolist_app\backend\main.py`

# SCOPE
## expenses
Not necessarily to hold ALL my expenses (though it would be pretty cool).

The goal is to have a financial dashboard which would break down my available money for each month.
The expenses will probably remain the same for most of the time, but perhaps their amount will change. So I would like to be able to either tell to an expense that it has an end-date or perhaps, when I update the expense it is not removed, but instead another instance is created.

The basic functionality is to have an idea of how much money I need each month - essentialy my fixed expenses.
#TODO in order for this to have any value, I need to know how much is my income!
#TODO it would also be beneficial if I could use a banking API to sort my transactions into: regular incomes, one-off incomes (people paying me back for shopping for example), fixed expenses...
#TODO I could also add functionality which would keep the amount of money I need for tax purposes...
#TODO for anything finance-related, I will probably have to go through https://www.csas.cz/cs/internetove-bankovnictvi/api-multibanking 

## inventory
the main purpose is for me to have a source of data for warranty expirations and the underlying data for expensive items - mainly electronics, furniture and other more expensive items

## owes
- basically just a journal for who owes me money (and whom I owe money)
- could theoretically be part of the expenses/incomes dashboard

## projects & todos
https://www.youtube.com/watch?v=Efo7nIUF2JY

- main idea is to have a whiteboard with todos which are somehow clustered, but also archived so that I can have some progress and also have a recap of all the things I did (and in which area)

- For handling the drag-and-drop functionality, libraries such as React DnD or interact.js can be useful. https://interactjs.io/ or perhaps HTML5 Drag-and-Drop API? interact.js looks better
- Libraries like Redux or the Context API in React can help manage state efficiently. (things like undo, redo)
- Decide how you will save the state of the board, so users don't lose their configurations when they reload the page. Options include local storage, session storage, or a database backend if you need permanent storage.

### drag and drop
https://www.youtube.com/watch?v=fhnHA7PWq0g

## reminders / countdowns
- reminders such as deadlines, bdays or appointements
- reminder can ALSO be a countdown (if box is ticked I guess)

- countdown is meant for things like how long since a date or how long till a date (typically how long till one month expires)

# TODO
## Authentication
- move hard values to some config/secret
- turn the hashes into hashes with salt
- rename /token to /register endpoint for better readability

## Expenses
- only allow certain values in `frequency` parameters (yearly, monthly...) https://fastapi.tiangolo.com/tutorial/path-params/#create-an-enum-class

## Todos
the default project for when there is none could be `backlog`