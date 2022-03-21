from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View, CreateView, UpdateView
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.urls import reverse_lazy
from .forms import AdminForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
user = get_user_model()


class AdminListView(ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = 'account/admin_list.html'


class AdminCrateView(CreateView):
    form_class = AdminForm
    template_name = 'account/admin_create.html'
    success_url = reverse_lazy("account:admin_list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_admin = True
        user.save()
        return super(AdminCrateView, self).form_valid(form)


class AdminUserDeleteView(View):
    def get(self, id):
        admin_user = get_object_or_404(user, id=id)
        admin_user.delete()
        return redirect('account:admin_list')


class AdminUserUpdateView(UpdateView):
    form_class = AdminForm
    template_name = 'account/admin_update.html'
    success_url = reverse_lazy("account:admin_list")
    slug_field = 'id'
    slug_url_kwarg = 'id'


class UserLoginView(View):
    form_class =LoginForm
    template_name = "account/login.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, national_code=cd['national_code'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('')
            return redirect('')
        return render(request, self.template_name, {"form": self.form_class})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("")
