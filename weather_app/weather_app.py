import requests
from tkinter import *
from tkinter import messagebox
from math import ceil

# This is the main window with the icon and background images.
main = Tk()
main.geometry('325x500')
# Making the window size by default
main.resizable(0, 0)
# Background of the App
background_img = PhotoImage(file='background.png')
background_label = Label(main, image=background_img)
background_label.place(x=0, y=0)
# The title and icon of the window
main.title("Weather App")
icon_photo = PhotoImage(file="icon.png")
main.iconphoto(False, icon_photo)

# Writing the function which will show the weather of the chosen city
city_value = StringVar()


def weather_func():
    # Using your personal api key, from OpenWeatherMap
    api_key = 'e32886abd55eb5f590bb004f36b7cd10'
    city = city_value.get()
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key
    response = requests.get(url)
    weather = response.json()

    output_weather.configure(state=NORMAL)
    # This will clear the text field for every new city you search
    output_weather.delete("1.0", "end")

    # If the 'cod' is 200, that means we successfully got the data for the weather
    if weather['cod'] == 200:
        kelvin = 273.15
        name_of_city = weather['name']
        country = weather['sys']['country']
        temp = ceil(weather['main']['temp'] - kelvin)  # here we convert to celsius
        feels_like_temp = ceil(weather['main']['feels_like'] - kelvin)
        humidity = weather['main']['humidity']
        wind_speed = int(weather['wind']['speed'] * 3.6)  # 3.6 is to convert from m/s to km/h
        description = weather['weather'][0]['description']
        pressure = weather['main']['pressure']

        # This will give us the information which will be seen in the output_weather text field
        weathers = f"""The weather in {name_of_city}, {country} is:
- Current temperature: {temp} °C
- Fells like: {feels_like_temp}°C
- Wind speed: {wind_speed} km/h
- Humidity: {humidity}%
- Pressure: {pressure} hPa
- Additional info: {description}
"""
        # This will display the weather info in the text field
        output_weather.insert(INSERT, weathers)
        # This makes the text field disabled, so you cant write in it
        output_weather.configure(state=DISABLED)

    else:
        messagebox.showerror('Weather Error', 'Please enter a valid City Name! :)')


# This we use for closing the app with the exit_button
def exit_app():
    main.destroy()


# Here is the front end part of the code
first_label = Label(main, text='Enter City:', bd=2, font='Arial 14  bold', bg='#E3AAB0').pack(pady=30)
enter_city = Entry(main, textvariable=city_value, bd=5, width=20).pack()
show_result = Button(main, command=weather_func, bd=3, bg='#D8C2D7', activebackground='#BAC0FF',
                     text='Show Weather').pack(pady=18)
output_weather = Text(main, font='Arial 10', bd='5', width=28, height=10)
output_weather.configure(state=DISABLED)
output_weather.pack(pady=0)
exit_button = Button(main, command=exit_app, width=7, bd=3, bg='#D8C2D7', fg='black', font='Arial 10 ',
                     activebackground='#BAC0FF', text='EXIT').pack(pady=60)

main.mainloop()
