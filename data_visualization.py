import matplotlib.pyplot as plt

# Plot temperature, humidity, and wind speed from the weather DataFrame.
def plot_weather_data(df):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Location')
    ax1.set_ylabel('Temperature (°C)', color='tab:red')
    ax1.bar(df['location'], df['temperature'], color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Humidity (%)', color='tab:blue')
    ax2.bar(df['location'], df['humidity'], color='tab:blue', alpha=0.5)
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    ax3 = ax1.twinx()
    ax3.set_ylabel('Wind Speed (m/s)', color='tab:green')
    ax3.bar(df['location'], df['wind_speed'], color='tab:green', alpha=0.3)
    ax3.tick_params(axis='y', labelcolor='tab:green')
    ax3.spines['right'].set_position(('outward', 60))

    fig.tight_layout()
    plt.show()
