from django import template

register = template.Library()

def rupiah_format(value):
    try:
        value = int(value)
        return f"Rp{value:,.0f}".replace(",", ".")
    except (ValueError, TypeError):
        return value

register.filter('rupiah', rupiah_format)
