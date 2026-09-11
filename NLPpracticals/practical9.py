import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime


# ==========================================
# CONFIGURATION
# ==========================================

API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5"


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Real-Time Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🌤️ Real-Time Weather Dashboard")

st.caption(
    "Live weather data using OpenWeather API"
)


# ==========================================
# CITY INPUT
# ==========================================

city = st.text_input(
    "Enter City Name",
    value="Mumbai"
)


# ==========================================
# GET CURRENT WEATHER
# ==========================================

def get_current_weather(city):

    url = f"{BASE_URL}/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code == 200:

        return response.json()

    else:

        return None


# ==========================================
# GET FORECAST
# ==========================================

def get_forecast(lat, lon):

    url = f"{BASE_URL}/forecast"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code == 200:

        return response.json()

    return None


# ==========================================
# SEARCH BUTTON
# ==========================================

if st.button("🔍 Get Weather"):

    weather = get_current_weather(city)

    if weather is None:

        st.error(
            "City not found or API request failed."
        )

    else:

        # ==================================
        # CURRENT WEATHER
        # ==================================

        st.success(
            f"Weather data received for {city}"
        )

        temperature = weather["main"]["temp"]

        feels_like = weather["main"]["feels_like"]

        humidity = weather["main"]["humidity"]

        pressure = weather["main"]["pressure"]

        wind_speed = weather["wind"]["speed"]

        visibility = weather.get(
            "visibility",
            0
        ) / 1000

        clouds = weather["clouds"]["all"]

        description = weather["weather"][0]["description"]

        icon = weather["weather"][0]["icon"]


        # ==================================
        # LOCATION
        # ==================================

        st.subheader(
            f"📍 {weather['name']}, {weather['sys']['country']}"
        )


        # ==================================
        # MAIN WEATHER
        # ==================================

        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "🌡️ Temperature",
                f"{temperature:.1f} °C"
            )


        with col2:

            st.write(
                f"### 🌤️ {description.title()}"
            )

            st.image(
                f"https://openweathermap.org/img/wn/{icon}@2x.png",
                width=100
            )


        # ==================================
        # WEATHER CARDS
        # ==================================

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "💧 Humidity",
                f"{humidity}%"
            )


        with col2:

            st.metric(
                "💨 Wind Speed",
                f"{wind_speed} m/s"
            )


        with col3:

            st.metric(
                "🔵 Pressure",
                f"{pressure} hPa"
            )


        with col4:

            st.metric(
                "👁️ Visibility",
                f"{visibility:.1f} km"
            )


        # ==================================
        # ADDITIONAL INFORMATION
        # ==================================

        st.divider()

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "🌡️ Feels Like",
                f"{feels_like:.1f} °C"
            )


        with col2:

            st.metric(
                "☁️ Cloudiness",
                f"{clouds}%"
            )


        with col3:

            current_time = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            st.metric(
                "🕐 Last Updated",
                current_time
            )


        # ==================================
        # FORECAST
        # ==================================

        forecast = get_forecast(
            weather["coord"]["lat"],
            weather["coord"]["lon"]
        )


        if forecast:

            st.divider()

            st.subheader(
                "🌡️ Temperature Forecast"
            )


            # First 8 forecast records
            forecast_data = forecast["list"][:8]


            dates = []

            temperatures = []


            for item in forecast_data:

                date = datetime.fromtimestamp(
                    item["dt"]
                )

                dates.append(
                    date.strftime("%d %b %H:%M")
                )

                temperatures.append(
                    item["main"]["temp"]
                )


            df = pd.DataFrame({

                "Time": dates,

                "Temperature": temperatures

            })


            # ==================================
            # LINE CHART
            # ==================================

            fig = px.line(

                df,

                x="Time",

                y="Temperature",

                markers=True,

                title="Temperature Trend"

            )


            fig.update_layout(

                xaxis_title="Time",

                yaxis_title="Temperature (°C)"

            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


            # ==================================
            # FORECAST TABLE
            # ==================================

            st.subheader(
                "📊 Forecast Data"
            )


            st.dataframe(
                df,
                use_container_width=True
            )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Weather data provided by OpenWeather API"
)