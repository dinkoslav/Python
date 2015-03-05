def on_budget(books, budget):
    dict = {
            "books_on_budget": 0,
            "loan": 0
            }
    books = sorted(books)
    for book in books:
        if book <= budget:
            dict["books_on_budget"] = dict["books_on_budget"] + 1
            budget = budget - book
        else:
            dict["loan"] = dict["loan"] + book
    if dict["loan"] > budget:
        dict["loan"] = dict["loan"] - budget
        
    return dict




# books = [0, 10, 100, 5, 3, 8, 25]
# budget = 35

# books = [0, 0, 0]
# budget = 10

books = [50, 60, 100]
budget = 20

books_info = on_budget(books, budget)
print(books_info)

