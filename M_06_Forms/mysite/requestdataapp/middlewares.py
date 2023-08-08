from time import time

from django.core.exceptions import PermissionDenied
from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("request count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")


# class CountRequestsFromUser:
#
#     def __init__(self, get_response):
#         self.users_requests = dict()
#         self.time_last_request = 0
#         self.get_response = get_response
#
#     def control_time(self):
#         now_time = time()
#         return now_time
#
#     def get_user_ip(self, request: HttpRequest):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def __call__(self, request: HttpRequest):
#         print('Start call func')
#         response = self.get_response(request)
#         user_ip = self.get_user_ip(request)
#         time_now = self.control_time()
#
#         if self.users_requests.get(user_ip):
#             if time_now - self.users_requests[user_ip] < 1:
#                 print(f'Error. Time difference {time_now - self.users_requests[user_ip]}')
#                 raise PermissionDenied
#         self.users_requests[user_ip] = time_now
#         print(f'User id {user_ip} time request {time_now}')
#
#         return response