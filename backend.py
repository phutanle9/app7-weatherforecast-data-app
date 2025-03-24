import requests

API_KEY="f9103b0df151f9ad0c8fb6598fec5a46"
def get_data(place, forecast_days=None, kind=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filterd_data = data['list']
    nr_values= 8* forecast_days
    filterd_data = filterd_data[:nr_values]
    if kind =="Temperature":
        filterd_data = [dict['main']['temp'] for dict in filterd_data]
    if kind == "Sky":
        filterd_data = [dict['main'][0]['main'] for dict in filterd_data]

    return filterd_data

if __name__ == "__main__":
    print((get_data(place="Tokyo",forecast_days=3,kind="Temperature")))