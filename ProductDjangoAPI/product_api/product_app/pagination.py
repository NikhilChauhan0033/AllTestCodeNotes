from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'current_page'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        """
        Custom pagination:
        - returns empty list and message if current page > total pages
        """
        page_size = self.get_page_size(request) or self.page_size
        paginator = self.django_paginator_class(queryset, page_size)

        try:
            page_number = int(request.query_params.get(self.page_query_param, 1))
        except ValueError:
            page_number = 1

        total_count = paginator.count
        total_pages = math.ceil(total_count / page_size)

        if page_number > total_pages and total_pages != 0:
            # Out of range: empty page
            self.page = []
            self.request = request
            self.total_pages = total_pages
            self.page_size_actual = page_size
            self.current_page = page_number
            return []

        try:
            self.page = paginator.page(page_number)
        except:
            # fallback: empty list
            self.page = []
        self.request = request
        self.total_pages = total_pages
        self.page_size_actual = page_size
        self.current_page = page_number
        return list(self.page)

    def get_paginated_response(self, data):
        response_data = {
            "count": getattr(self, "total_count", getattr(self.page, 'paginator', None) and self.page.paginator.count or 0),
            "total_pages": getattr(self, "total_pages", 0),
            "current_page": getattr(self, "current_page", 1),
            "page_size": getattr(self, "page_size_actual", self.page_size),
            "results": data,
        }

        # Add message if results are empty (out-of-range page)
        if not data:
            response_data["message"] = "Data not found"

        return Response(response_data)
