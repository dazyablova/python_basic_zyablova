import datetime as dt
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Record


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def get_today_stats(self):
        today = dt.date.today()
        return sum(record.amount for record in self.records if record.date == today)

    def add_record(self, record):
        self.records.append(record)

    def get_week_stats(self):
        today = dt.date.today()
        date_week_ago = today - dt.timedelta(days=7)
        return sum(
            record.amount for record in self.records if date_week_ago < record.date <= today
        )

    def get_remained(self):
        remained = self.limit - self.get_today_stats()
        return remained


class Record:
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()

    def __str__(self):
        return f"Record({self.amount}, {self.date}, {self.comment})"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        g_rem = self.get_remained()
        if g_rem <= 0:
            return "Превышение лимита калорий"
        return f"Недостаточно калорий, рекомендуется добрать не более {g_rem} кКал"


def home(request):
    context = {}
    return render(request, "home.html", context)


class RecordListView(ListView):
    model = Record
    template_name = "record_list.html"
    context_object_name = "records"


class RecordDetailView(DetailView):
    model = Record
    template_name = "record_detail.html"
    context_object_name = "record"