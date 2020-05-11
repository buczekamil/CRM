from datetime import date


def footer(request):
    return {'date': date.today(),
            'version': 1.1,
            'currency': 'EUR'
            }