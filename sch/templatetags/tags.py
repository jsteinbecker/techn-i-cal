from django import template
import datetime as dt


register = template.Library()


@register.simple_tag
def secToHours(seconds):
    return seconds.total_seconds() / 3600

#***** BUTTON // GO TO THIS WEEK *****#
@register.inclusion_tag("this_week.html")
def goToThisWeek ():
    today = dt.date.today()
    return {
        'year': today.year,
        'week': today.isocalendar()[1]
    }

#***** BADGE // N DAYS AWAY *****#
@register.inclusion_tag("n_days_away.html")
def nDaysAway (date):
    today = dt.date.today()
    return {
        'n': (date - today).days
    }

@register.inclusion_tag("n_days_away_small.html")
def nDaysAwaySmall (date):
    today = dt.date.today()
    return {
        'n': (date - today).days
    }

@register.inclusion_tag("LeftArrow.svg")
def backArrow (width="20px", height="20px", fill="#e1e1e1",fillB="#acffde"):
    return {'width': width,'height': height,'fill': fill, 'fillB': fillB}

@register.inclusion_tag("RightArrow.svg")
def forwardArrow (width="20px", height="20px", fill="#e1e1e1",fillB="#acffde"):
    return {'width': width,'height': height,'fill': fill, 'fillB': fillB}

@register.inclusion_tag("Lock.svg")
def lockIcon (width="20px", height="20px", fill="#e1e1e1"):
    return {'width': width,'height': height,'fill': fill}

@register.inclusion_tag("SupportStaff.svg")
def fillTemplateIcon (width="30px", height="30px", fill="#e1e1e1"):
    return {'width': width,'height': height,'fill': fill}

@register.inclusion_tag("FlowRate Logo.svg")
def logoIcon (width="90px", height="90px"):
    return {'width': width,'height': height}