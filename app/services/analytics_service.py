class AnalyticsService:
    def __init__(self, dal):
        self.dal = dal

    def forecast_next_month_visits(self):
        trends = self.dal.monthly_visit_trends()

        if len(trends) < 2:
            return "Not enough data to forecast"

        avg = sum(row.visits for row in trends) / len(trends)
        return round(avg)
