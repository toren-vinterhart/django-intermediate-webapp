from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """Simple pagination: If we want Simple pagination uncomment these 3 lines and comment custom settings
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
    """

    # custom settings
    page_size = 2

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous:": self.get_previous_link(),
                },
                "total_objects": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
