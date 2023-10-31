from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import reverse

from django.views.generic import ListView, DetailView

from .models import Profile, ProfileAvatar
from .forms import ProfileForm


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    model = Profile
    template_name_suffix = "_update_form"
    form_class = ProfileForm

    def test_func(self):
        if self.request.user.is_staff or self.request.user.profile == self.get_object():
            return True

    def get_success_url(self):
        return reverse(
            "myauth:profiles-list",
            # kwargs={"pk": self.object.id}
            # kwargs={"pk": self.get_object().user.id},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProfileAvatar.objects.create(
                profile=self.object,
                image=image,
            )
        return response


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"
    fields = "user", "bio", "avatar"
    model = Profile


class ProfileListView(ListView):
    template_name = 'myauth/profiles-list.html'
    context_object_name = "profiles"
    queryset = Profile.objects.all()


class ProfileDetailsView(DetailView):
    template_name = "myauth/profile-details.html"
    model = Profile
    context_object_name = "profile"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})
