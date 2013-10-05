from django.shortcuts import render
from django.http import HttpResponseRedirect
from s3.models import AwsForm
import boto


def home(request):
      if not request.session.has_key("AWS_KEY"):
         if request.method == 'POST':
            form = AwsForm(request.POST)
            if form.is_valid():
                try:
                    conn = boto.connect_s3(form.cleaned_data["AWS_KEY"], form.cleaned_data["AWS_SECRET"])
                    bucket_list = conn.get_all_buckets()
                except:
                    error = "Invalid Credentials. Please Try again."
                    return render(request, 's3/home.html', {
                            'form': form,
                            'error': error,
                    })
                request.session['AWS_KEY'] = form.cleaned_data["AWS_KEY"]
                request.session['AWS_SECRET'] = form.cleaned_data["AWS_SECRET"]
                bucket_list = [i.name  for i in bucket_list]
                request.session['bucket_list'] = bucket_list
                return render(request, 's3/buckets.html', {
                    'bucket_list': bucket_list,
                })
         else:
            form = AwsForm() # An unbound form

         return render(request, 's3/home.html', {
            'form': form,
         })
      else:
           return render(request, 's3/buckets.html', {
                    'bucket_list': request.session['bucket_list'],
           })


def bucket(request):
    AWS_KEY = request.session['AWS_KEY']
    AWS_SECRET = request.session['AWS_SECRET']
    if AWS_KEY and AWS_SECRET:
        conn = boto.connect_s3(AWS_KEY, AWS_SECRET)
        bucket_name = request.path.split('/')[-1]
        key_list = conn.get_bucket(request.path.split('/')[-1])
        key_list = [{ "name": some_key.name,"size": some_key.size, "last_modified": some_key.last_modified,  "download_url": conn.generate_url(600, 'GET', bucket=bucket_name, key= some_key.name, force_http=True)} for some_key in key_list ]
        return render(request, 's3/buckets.html', {
                    'bucket_list': request.session['bucket_list'],
                    'key_list': key_list,
                    'bucketname':bucket_name
                })
    else:
        return HttpResponseRedirect("/")

def clear(request):
    if request.session:
        request.session.flush()
    return HttpResponseRedirect("/")





