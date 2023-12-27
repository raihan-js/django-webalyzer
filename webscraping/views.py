# webscraping/views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import WebsiteForm  # Import the WebsiteForm from forms.py

def analyze_website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website_url = form.cleaned_data['website_url']
            try:
                response = requests.get(website_url)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Check if Bootstrap is used by looking for its CSS classes
                bootstrap = 'No'
                for link in soup.find_all('link'):
                    if 'bootstrap' in link.get('href', '').lower():
                        bootstrap = 'Yes'
                        break

                # Check if jQuery is used by looking for its script tag
                jquery = 'No'
                for script in soup.find_all('script'):
                    if 'jquery' in script.get('src', '').lower():
                        jquery = 'Yes'
                        break

                # Create a dictionary to pass data to the template
                website_data = {
                    'bootstrap': bootstrap,
                    'jquery': jquery,
                }
            except requests.exceptions.RequestException:
                website_data = "Error fetching website data"
    else:
        form = WebsiteForm()
        website_data = ""

    return render(request, 'webscraping/analyze_website.html', {'form': form, 'website_data': website_data})
