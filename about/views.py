from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the about page

    **Template:**

    :template:`about/about.html`

    **Context**

    ``about``
        An instance of :model:`about.About`
    """


    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
                'Collaboration request received, thank you! I will endeavour to reply to you within 2 working days.'
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )