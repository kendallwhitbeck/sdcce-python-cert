"""Experimenting with locale module"""
import locale

print(locale.getlocale())  # get & print current locale

# print(locale.localeconv())  # print TODO
locale.strcoll('f\xe4n', 'faan')  # compare a string containing an umlaut
print('f\xe4n')

# Print getlocale for locale.LC_ALL
locale.setlocale(locale.LC_ALL)
print(f"locale.setlocale(locale.LC_ALL): {locale.getlocale()}")

locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale())  # use and print user's preferred locale

# set the locale to British English (United Kingdom)
# locale.setlocale(locale.LC_ALL, 'en_EN')

# Format a currency value w/ appropriate symbol name
currency = 1234.56
# formatted_currency = locale.currency(currency, grouping=True)
# print(locale.getlocale())


# Set locale to Germany (German)
locale.setlocale(locale.LC_ALL, 'de_DE')
print(locale.getlocale())  # use and print user's preferred locale


# using locale module to list days of the week in german

