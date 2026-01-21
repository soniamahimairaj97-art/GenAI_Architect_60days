import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_msg = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = "Key is attched at th end of the code paste that, removed here for security reason"  # Paste your key here 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temp': round(data['main']['temp']),
                'desc': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            error_msg = "City not found. Please try again."

    return render_template('weather.html', weather=weather_data, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)

    #API Key 46da03b57f7ffde73379125d950d2d7e

