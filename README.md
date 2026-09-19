# SkyPulse - Smart Weather Dashboard

SkyPulse is a modern weather dashboard built using Python and Streamlit. It provides real-time weather information, hourly forecasts, and a five-day forecast for any searched city.

The application uses the Open-Meteo API to retrieve weather data and presents it through a modern dark-themed interface with animated elements and interactive weather cards.

## Features

- Real-time weather information
- City-based weather search
- Current temperature and feels-like temperature
- Weather condition and weather icons
- Humidity information
- Wind speed and wind gusts
- Precipitation information
- Atmospheric pressure
- Visibility information
- UV Index
- Hourly weather forecast
- Five-day weather forecast
- Rain probability
- Sunrise and sunset timings
- Celsius and Fahrenheit support
- Smart weather insights
- Animated user interface
- Responsive weather dashboard
- Cached API requests for improved performance

## Tech Stack

- Python
- Streamlit
- Open-Meteo API
- Requests
- HTML
- CSS

## Project Structure

```text
Weatherpulse/
│── app.py
│── requirements.txt
│── .gitignore
└── README.md
## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Weatherpulse.git
cd Weatherpulse
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## API

SkyPulse uses the Open-Meteo API for weather information.

The application uses the Open-Meteo Geocoding API to find the latitude and longitude of a searched city.

```text
https://geocoding-api.open-meteo.com/v1/search
```

The Open-Meteo Forecast API is then used to retrieve current, hourly, and daily weather information.

```text
https://api.open-meteo.com/v1/forecast
```

No API key is required for the Open-Meteo services used in this project.

## Weather Information

The dashboard provides the following information:

### Current Weather

- City and country
- Current temperature
- Feels-like temperature
- Weather condition
- Humidity
- Wind speed
- Precipitation
- Atmospheric pressure
- UV Index

### Hourly Forecast

The hourly forecast provides upcoming:

- Time
- Temperature
- Weather condition
- Rain probability

### Five-Day Forecast

The five-day forecast displays:

- Day
- Date
- Maximum temperature
- Minimum temperature
- Weather condition
- Rain probability

### Additional Information

The application also provides:

- Visibility
- Wind gusts
- UV exposure status
- Sunrise
- Sunset
- Smart weather insights

## Temperature Units

SkyPulse supports both Celsius and Fahrenheit.

The Fahrenheit conversion is calculated using:

```text
°F = (°C × 9/5) + 32
```

Users can switch between Celsius and Fahrenheit from the sidebar.
