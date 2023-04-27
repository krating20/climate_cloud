



def date_change(date):
    date_str = date
    date_str_without_dashes = date_str.replace("-", "")
    return date_str_without_dashes
print(date_change("2022-01-04"))