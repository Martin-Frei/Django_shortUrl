from django.shortcuts import render, redirect, get_object_or_404
from short.models import shortUrl
from short.forms import shortUrlForm
import random

# Create your views here.


def getUrl(request):
    context = {}
    if request.method == "POST":
        form = shortUrlForm(request.POST)
        if form.is_valid():
            long_url = request.POST["longUrl"]
            #url_obj = form.save(commit=False)
            short_url = "".join(
                random.sample("abcdefcghijklmnopqrstuvwxyz", 5)
            )
            # url_obj.save()
            shortUrl.objects.create(longUrl = long_url,shortUrlField = short_url ) # Insert the new object in the table 
            context["newShortUrl"] = short_url

    all_urls = shortUrl.objects.all().order_by("-id")  # Neueste zuerst
    context["all_urls"] = all_urls

    return render(request, "urlShort.html", context)


#def redirect_to_url(request, short_code):
    #url_obj = get_object_or_404(shortUrl, shortUrlField=short_code)
    #return redirect(url_obj.longUrl)


# import the model 
# population.modelname.create(fields= value, fieldname = value)

# selct 
# population.object.all()  getting every record 
# population.object.filter(age>30)
# population.object.filter(name =" NAME")
# population.object.filter(age<30. income= '1m')

# updating the Data chaning teh income 
# population.object.filter(name =" NAME").update(income='1T')
# first fetch the object,than chance teh value

# delete.filter)name="NAME".delede()
# #model.objects. create or .filter .update .delete

# signup logout
# login sceen => form: Name age date diagnose
# a tabel with all diagnoses with login 
# App:
# userhandling
# regardkeeping track of user
 
