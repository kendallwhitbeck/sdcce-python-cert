import locale

loc = locale.getlocale()  # get current locale
print(loc)
print(locale.localeconv())
locale.setlocale(locale.LC_ALL)
locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
locale.setlocale(locale.LC_ALL, loc)  # restore saved locale

# Set the locale to British English (United Kingdom)
#locale.setlocale(locale.LC_ALL, 'en_EN')
# Format a currency value with the appropriate symbol
formatted_currency = locale.currency(1234.56, grouping=True)
print("{:.2f}".format(3.1456))
print(formatted_currency)
# Convert an amount from one currency to another based on exchange rates
amount_in_euros = 1000.00
#get_exchange_rate()
exchange_rate_usd_to_eur = 1.18
amount_in_usd = amount_in_euros * exchange_rate_usd_to_eur
formatted_amount_in_usd = locale.currency(amount_in_usd, grouping=True)
print(formatted_amount_in_usd)