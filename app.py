import streamlit as st
import requests
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SkyPulse | Smart Weather",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 180, 255, 0.15), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(100, 80, 255, 0.12), transparent 25%),
        linear-gradient(135deg, #020617, #071426, #020617);
    color: white;
}

header {
    background: transparent !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

section[data-testid="stSidebar"] {
    background: rgba(3, 10, 24, 0.97);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] > div {
    padding-top: 20px;
}

/* Brand */

.brand {
    text-align: center;
    padding: 15px 5px 30px;
}

.brand-icon {
    font-size: 50px;
    animation: float 3s infinite ease-in-out;
}

.brand-title {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(90deg,#ffffff,#5bd6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-subtitle {
    color: #7f91aa;
    font-size: 12px;
    margin-top: 5px;
}

@keyframes float {
    0%,100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-10px);
    }
}

/* Hero */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 300px;
    padding: 38px;
    border-radius: 30px;
    margin-bottom: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(20, 55, 95, 0.85),
            rgba(5, 15, 32, 0.95)
        );

    border: 1px solid rgba(255,255,255,0.09);
    box-shadow: 0 25px 80px rgba(0,0,0,0.35);
}

/* Stars */

.star {
    position: absolute;
    width: 4px;
    height: 4px;
    background: white;
    border-radius: 50%;
    animation: twinkle 3s infinite ease-in-out;
}

.star1 { top: 20%; left: 70%; }
.star2 { top: 60%; left: 80%; animation-delay: 1s; }
.star3 { top: 30%; left: 90%; animation-delay: 2s; }
.star4 { top: 75%; left: 65%; animation-delay: .5s; }
.star5 { top: 15%; left: 50%; animation-delay: 1.5s; }

@keyframes twinkle {
    0%,100% {
        opacity: .2;
        transform: scale(1);
    }
    50% {
        opacity: 1;
        transform: scale(2);
    }
}

.location {
    color: #91a3bb;
    font-size: 14px;
}

.temperature {
    font-size: 88px;
    line-height: 1;
    font-weight: 800;
    letter-spacing: -5px;
}

.condition {
    font-size: 20px;
    font-weight: 600;
    margin-top: 15px;
}

.feels {
    color: #91a3bb;
    margin-top: 8px;
}

.weather-icon {
    font-size: 110px;
    animation: weatherFloat 4s infinite ease-in-out;
}

@keyframes weatherFloat {
    0%,100% {
        transform: translateY(0) rotate(0deg);
    }
    50% {
        transform: translateY(-15px) rotate(5deg);
    }
}

/* Section */

.section-title {
    font-size: 21px;
    font-weight: 700;
    margin: 25px 0 15px;
}

/* Metric */

.metric {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    min-height: 135px;
    transition: .3s;
}

.metric:hover {
    transform: translateY(-7px);
    border-color: rgba(80,210,255,.4);
    background: rgba(255,255,255,.08);
}

.metric-icon {
    font-size: 28px;
}

.metric-title {
    color: #8192aa;
    font-size: 12px;
    margin-top: 10px;
}

.metric-value {
    font-size: 24px;
    font-weight: 700;
    margin-top: 5px;
}

/* Hourly */

.hourly {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    padding-bottom: 10px;
}

.hour-card {
    min-width: 105px;
    padding: 18px 12px;
    text-align: center;
    border-radius: 18px;
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.08);
    transition: .3s;
}

.hour-card:hover {
    transform: translateY(-6px);
    background: rgba(50,180,255,.1);
}

.hour-time {
    color: #8495ac;
    font-size: 12px;
}

.hour-icon {
    font-size: 30px;
    margin: 12px 0;
}

.hour-temp {
    font-weight: 700;
    font-size: 18px;
}

.rain {
    color: #55cdfc;
    font-size: 11px;
    margin-top: 7px;
}

/* Forecast */

.forecast {
    text-align: center;
    padding: 20px 12px;
    border-radius: 20px;
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.08);
    transition: .3s;
}

.forecast:hover {
    transform: translateY(-7px);
    border-color: rgba(80,210,255,.35);
}

.forecast-icon {
    font-size: 40px;
    margin: 15px 0;
}

.forecast-date {
    color: #75869d;
    font-size: 11px;
    margin-top: 5px;
}

.forecast-desc {
    color: #8495ac;
    font-size: 11px;
    margin-top: 7px;
}

/* Detail */

.detail {
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 20px;
    padding: 24px;
}

.detail-row {
    display: flex;
    justify-content: space-between;
    padding: 13px 0;
    border-bottom: 1px solid rgba(255,255,255,.06);
}

.detail-row:last-child {
    border-bottom: none;
}

.detail-label {
    color: #8192aa;
}

/* Insight */

.insight {
    background: linear-gradient(
        135deg,
        rgba(40,130,255,.15),
        rgba(60,210,255,.04)
    );
    border: 1px solid rgba(90,205,255,.18);
    border-radius: 20px;
    padding: 25px;
}

.insight-text {
    color: #a8b9cf;
    line-height: 1.7;
    margin-top: 10px;
}

/* Daylight */

.daylight {
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.08);
}

.day-icon {
    font-size: 42px;
}

.day-label {
    color: #8192aa;
    font-size: 12px;
    margin-top: 8px;
}

.day-time {
    font-size: 22px;
    font-weight: 700;
    margin-top: 5px;
}

/* Footer */

.footer {
    text-align: center;
    color: #60738d;
    padding: 35px 0 15px;
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# WEATHER CODES
# =========================================================

WEATHER_CODES = {
    0: ("☀️", "Clear Sky"),
    1: ("🌤️", "Mainly Clear"),
    2: ("⛅", "Partly Cloudy"),
    3: ("☁️", "Overcast"),
    45: ("🌫️", "Fog"),
    48: ("🌫️", "Rime Fog"),
    51: ("🌦️", "Light Drizzle"),
    53: ("🌦️", "Drizzle"),
    55: ("🌧️", "Heavy Drizzle"),
    61: ("🌧️", "Light Rain"),
    63: ("🌧️", "Rain"),
    65: ("🌧️", "Heavy Rain"),
    71: ("🌨️", "Light Snow"),
    73: ("🌨️", "Snow"),
    75: ("❄️", "Heavy Snow"),
    80: ("🌦️", "Rain Showers"),
    81: ("🌧️", "Rain Showers"),
    82: ("⛈️", "Heavy Showers"),
    95: ("⛈️", "Thunderstorm"),
    96: ("⛈️", "Thunderstorm"),
    99: ("⛈️", "Heavy Thunderstorm")
}


def weather_info(code):
    return WEATHER_CODES.get(code, ("🌤️", "Unknown"))


# =========================================================
# API
# =========================================================

@st.cache_data(ttl=600)
def get_weather(city):

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_response = requests.get(
        geo_url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return None

    location = geo_data["results"][0]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": ",".join([
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "precipitation",
                "weather_code",
                "wind_speed_10m",
                "wind_gusts_10m",
                "surface_pressure",
                "visibility",
                "uv_index"
            ]),
            "hourly": ",".join([
                "temperature_2m",
                "precipitation_probability",
                "weather_code"
            ]),
            "daily": ",".join([
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_probability_max",
                "sunrise",
                "sunset"
            ]),
            "forecast_days": 6,
            "timezone": "auto"
        },
        timeout=15
    )

    weather_response.raise_for_status()

    return location, weather_response.json()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.html("""
    <div class="brand">
        <div class="brand-icon">☁️</div>
        <div class="brand-title">SkyPulse</div>
        <div class="brand-subtitle">
            Smart Weather Dashboard
        </div>
    </div>
    """)

    st.markdown("### 🧭 Navigation")

    st.markdown("""
    <div class="menu-item">🏠 Dashboard</div>
    <div class="menu-item">📅 Forecast</div>
    <div class="menu-item">🗺️ Weather Map</div>
    <div class="menu-item">❤️ Favorites</div>
    """, unsafe_allow_html=True)

    st.divider()

    city = st.text_input(
        "Search City",
        value="Chennai",
        placeholder="Enter city name..."
    )

    unit = st.radio(
        "Temperature",
        ["°C", "°F"],
        horizontal=True
    )

    st.divider()

    st.info(
        "SkyPulse gives real-time weather information "
        "using Open-Meteo."
    )


# =========================================================
# GET DATA
# =========================================================

if not city.strip():
    st.warning("Please enter a city name.")
    st.stop()

try:
    result = get_weather(city.strip())

except Exception as e:
    st.error("Unable to load weather data.")
    st.error(str(e))
    st.stop()

if result is None:
    st.error("City not found. Please enter a valid city.")
    st.stop()


location, weather = result

current = weather["current"]
hourly = weather["hourly"]
daily = weather["daily"]

city_name = location.get("name", city)
country = location.get("country", "")

temperature = current["temperature_2m"]
feels = current["apparent_temperature"]

if unit == "°F":
    temperature_display = temperature * 9 / 5 + 32
    feels_display = feels * 9 / 5 + 32
else:
    temperature_display = temperature
    feels_display = feels

icon, condition = weather_info(current["weather_code"])

humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]
gust = current["wind_gusts_10m"]
rain = current["precipitation"]
pressure = current["surface_pressure"]
visibility = current.get("visibility", 0)
uv = current.get("uv_index", 0)

# =========================================================
# HERO
# =========================================================

today = datetime.now().strftime("%A, %d %B %Y")

st.html(f"""
<div class="hero">

    <div class="star star1"></div>
    <div class="star star2"></div>
    <div class="star star3"></div>
    <div class="star star4"></div>
    <div class="star star5"></div>

    <div class="location">
        📍 {city_name}, {country}
        &nbsp; • &nbsp;
        {today}
    </div>

    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-top:35px;
    ">

        <div>

            <div class="temperature">
                {temperature_display:.0f}°
            </div>

            <div class="condition">
                {icon} {condition}
            </div>

            <div class="feels">
                Feels like {feels_display:.0f}{unit}
            </div>

        </div>

        <div class="weather-icon">
            {icon}
        </div>

    </div>

</div>
""")

# =========================================================
# OVERVIEW
# =========================================================

st.html('<div class="section-title">Weather Overview</div>')

metrics = [
    ("💧", "Humidity", f"{humidity}%"),
    ("💨", "Wind Speed", f"{wind:.0f} km/h"),
    ("🌧️", "Precipitation", f"{rain:.1f} mm"),
    ("◉", "Pressure", f"{pressure:.0f} hPa"),
    ("☀️", "UV Index", f"{uv:.1f}")
]

cols = st.columns(5)

for col, item in zip(cols, metrics):

    with col:

        st.html(f"""
        <div class="metric">

            <div class="metric-icon">
                {item[0]}
            </div>

            <div class="metric-title">
                {item[1]}
            </div>

            <div class="metric-value">
                {item[2]}
            </div>

        </div>
        """)


# =========================================================
# HOURLY
# =========================================================

st.html('<div class="section-title">Hourly Forecast</div>')

current_time = current["time"]

start_index = 0

for i, value in enumerate(hourly["time"]):
    if value >= current_time:
        start_index = i
        break

hour_html = '<div class="hourly">'

for i in range(
    start_index,
    min(start_index + 12, len(hourly["time"]))
):

    time_value = hourly["time"][i]

    hour = datetime.fromisoformat(
        time_value
    ).strftime("%I %p")

    temp = hourly["temperature_2m"][i]

    if unit == "°F":
        temp = temp * 9 / 5 + 32

    rain_probability = hourly[
        "precipitation_probability"
    ][i]

    hour_icon, _ = weather_info(
        hourly["weather_code"][i]
    )

    hour_html += f"""
    <div class="hour-card">

        <div class="hour-time">
            {hour}
        </div>

        <div class="hour-icon">
            {hour_icon}
        </div>

        <div class="hour-temp">
            {temp:.0f}°
        </div>

        <div class="rain">
            💧 {rain_probability}%
        </div>

    </div>
    """

hour_html += "</div>"

st.html(hour_html)


# =========================================================
# 5 DAY FORECAST
# =========================================================

st.html('<div class="section-title">5-Day Forecast</div>')

forecast_cols = st.columns(5)

for col, i in zip(
    forecast_cols,
    range(1, 6)
):

    date_value = datetime.fromisoformat(
        daily["time"][i]
    )

    day = date_value.strftime("%a")
    date = date_value.strftime("%d %b")

    max_temp = daily["temperature_2m_max"][i]
    min_temp = daily["temperature_2m_min"][i]

    if unit == "°F":
        max_temp = max_temp * 9 / 5 + 32
        min_temp = min_temp * 9 / 5 + 32

    probability = daily[
        "precipitation_probability_max"
    ][i]

    forecast_icon, description = weather_info(
        daily["weather_code"][i]
    )

    with col:

        st.html(f"""
        <div class="forecast">

            <b>{day}</b>

            <div class="forecast-date">
                {date}
            </div>

            <div class="forecast-icon">
                {forecast_icon}
            </div>

            <div>
                <b>{max_temp:.0f}°</b>
                &nbsp;/&nbsp;
                {min_temp:.0f}°
            </div>

            <div class="forecast-desc">
                {description}
            </div>

            <div class="rain">
                💧 {probability}% rain
            </div>

        </div>
        """)


# =========================================================
# WEATHER DETAILS
# =========================================================

st.html('<div class="section-title">Weather Details</div>')

left, right = st.columns(2)

with left:

    st.html(f"""
    <div class="detail">

        <h3>🌎 Atmospheric Data</h3>

        <div class="detail-row">
            <span class="detail-label">Visibility</span>
            <b>{visibility / 1000:.1f} km</b>
        </div>

        <div class="detail-row">
            <span class="detail-label">Wind Gusts</span>
            <b>{gust:.0f} km/h</b>
        </div>

        <div class="detail-row">
            <span class="detail-label">Humidity</span>
            <b>{humidity}%</b>
        </div>

        <div class="detail-row">
            <span class="detail-label">Pressure</span>
            <b>{pressure:.0f} hPa</b>
        </div>

        <div class="detail-row">
            <span class="detail-label">UV Index</span>
            <b>{uv:.1f}</b>
        </div>

    </div>
    """)

with right:

    if uv <= 2:
        uv_status = "Low"
    elif uv <= 5:
        uv_status = "Moderate"
    elif uv <= 7:
        uv_status = "High"
    elif uv <= 10:
        uv_status = "Very High"
    else:
        uv_status = "Extreme"

    uv_width = min((uv / 12) * 100, 100)

    st.html(f"""
    <div class="detail">

        <h3>☀️ UV Exposure</h3>

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div>

                <div style="
                    color:#8192aa;
                    font-size:13px;
                ">
                    Current UV Index
                </div>

                <div style="
                    font-size:36px;
                    font-weight:800;
                ">
                    {uv:.1f}
                </div>

            </div>

            <div style="
                color:#69d5ff;
                font-weight:700;
            ">
                {uv_status}
            </div>

        </div>

        <div style="
            width:100%;
            height:8px;
            background:rgba(255,255,255,.08);
            border-radius:20px;
            margin-top:20px;
        ">

            <div style="
                width:{uv_width:.0f}%;
                height:100%;
                border-radius:20px;
                background:linear-gradient(
                    90deg,#42d6ff,#7c6cff
                );
            "></div>

        </div>

        <p style="
            color:#71839c;
            font-size:12px;
        ">
            UV protection is recommended during strong sunlight.
        </p>

    </div>
    """)


# =========================================================
# SMART INSIGHT
# =========================================================

st.html('<div class="section-title">SkyPulse Insight</div>')

if rain > 0:
    insight = "Rain is currently being reported. Keep an umbrella nearby."
elif uv >= 6:
    insight = "UV levels are high. Consider limiting prolonged direct sunlight."
elif temperature >= 35:
    insight = "It is quite warm today. Stay hydrated and take breaks from direct sunlight."
elif humidity >= 80:
    insight = "Humidity is high. Outdoor conditions may feel warmer than the actual temperature."
else:
    insight = "Weather conditions look comfortable. It is a good time to plan outdoor activities."

st.html(f"""
<div class="insight">

    <div style="
        font-size:18px;
        font-weight:700;
    ">
        ✨ Smart Weather Insight
    </div>

    <div class="insight-text">
        {insight}
    </div>

    <div style="
        margin-top:18px;
        color:#63d4ff;
        font-size:13px;
    ">
        Powered by real-time Open-Meteo data
    </div>

</div>
""")


# =========================================================
# DAYLIGHT
# =========================================================

st.html('<div class="section-title">Daylight</div>')

sunrise = datetime.fromisoformat(
    daily["sunrise"][0]
).strftime("%I:%M %p")

sunset = datetime.fromisoformat(
    daily["sunset"][0]
).strftime("%I:%M %p")

day_cols = st.columns(2)

with day_cols[0]:

    st.html(f"""
    <div class="daylight">

        <div class="day-icon">
            🌅
        </div>

        <div class="day-label">
            Sunrise
        </div>

        <div class="day-time">
            {sunrise}
        </div>

    </div>
    """)

with day_cols[1]:

    st.html(f"""
    <div class="daylight">

        <div class="day-icon">
            🌇
        </div>

        <div class="day-label">
            Sunset
        </div>

        <div class="day-time">
            {sunset}
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    SkyPulse Smart Weather Dashboard
    <br><br>
    Real-time weather data powered by Open-Meteo

</div>
""")