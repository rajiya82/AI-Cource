import requests
from datetime import datetime
from urllib.parse import quote


def get_weather(city):
    # URL-encode the city to handle spaces and special characters
    url = f"https://wttr.in/{quote(city)}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        area = data["nearest_area"][0]

        location = area["areaName"][0]["value"]
        country = area["country"][0]["value"]
        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        description = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        wind_kmph = current["windspeedKmph"]

        now = datetime.now()

        print(f"\nWeather Report")
        print(f"{'=' * 40}")
        print(f"Location  : {location}, {country}")
        print(f"Date/Time : {now.strftime('%d %b %Y, %H:%M')}")
        print(f"Condition : {description}")
        print(f"Temp      : {temp_c}\u00b0C (feels like {feels_like}\u00b0C)")
        print(f"Humidity  : {humidity}%")
        print(f"Wind      : {wind_kmph} km/h")

        # 3-Day Forecast
        forecast = data.get("weather", [])
        print("\n3-Day Forecast")
        print(f"{'-' * 40}")

        if not forecast:
            print("Forecast unavailable")
        else:
            # Determine today's date and select future forecast days (exclude today)
            today_date = datetime.now().date()
            future_days = []
            for d in forecast:
                date_str = d.get("date", "")
                try:
                    d_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except Exception:
                    # skip entries with unparsable dates
                    continue
                if d_date > today_date:
                    future_days.append((d, d_date))

            if not future_days:
                print("No future forecast available")
            else:
                for day, d_date in future_days[:3]:
                    date_label = d_date.strftime("%a %d %b %Y")

                    hi = day.get("maxtempC", "N/A")
                    lo = day.get("mintempC", "N/A")
                    # try to convert temps to integers for nicer output
                    try:
                        hi = f"{int(hi)}"
                    except Exception:
                        pass
                    try:
                        lo = f"{int(lo)}"
                    except Exception:
                        pass

                    desc = "N/A"
                    hourly = day.get("hourly") or []
                    # preferred midday description is at index 4
                    try:
                        desc = hourly[4]["weatherDesc"][0]["value"]
                    except Exception:
                        # fallback: middle hourly entry
                        if hourly:
                            mid = hourly[len(hourly) // 2]
                            try:
                                desc = mid["weatherDesc"][0]["value"]
                            except Exception:
                                desc = "N/A"

                    print(f"{date_label}: {desc} — High {hi}\u00b0C / Low {lo}\u00b0C")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except (KeyError, IndexError) as e:
        print(f"Error parsing weather data: {e}")


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
