import matplotlib.pyplot as plt


def classify_signal(rssi):
    """
    Classify WiFi signal strength based on RSSI value in dBm.
    """

    if rssi >= -50:
        return "Excellent"
    elif rssi >= -60:
        return "Good"
    elif rssi >= -70:
        return "Fair"
    else:
        return "Weak"


def analyze_signals(networks):
    """
    Analyze a list of WiFi networks.

    networks: list of tuples -> [(network_name, rssi), ...]
    """

    results = []

    for name, rssi in networks:
        quality = classify_signal(rssi)

        results.append({
            "name": name,
            "rssi": rssi,
            "quality": quality
        })

    return results


def display_results(results):
    print("\nWiFi Signal Strength Analyzer")
    print("-" * 55)
    print(f"{'Network':<20}{'RSSI (dBm)':<15}{'Quality'}")
    print("-" * 55)

    for result in results:
        print(
            f"{result['name']:<20}"
            f"{result['rssi']:<15}"
            f"{result['quality']}"
        )


def plot_signals(results):
    names = [result["name"] for result in results]
    rssi_values = [result["rssi"] for result in results]

    colors = []

    for rssi in rssi_values:
        if rssi >= -50:
            colors.append("green")
        elif rssi >= -60:
            colors.append("blue")
        elif rssi >= -70:
            colors.append("orange")
        else:
            colors.append("red")

    plt.figure(figsize=(9, 5))
    plt.bar(names, rssi_values, color=colors)

    plt.title("WiFi Signal Strength Analysis")
    plt.xlabel("WiFi Network")
    plt.ylabel("Signal Strength (dBm)")
    plt.axhline(-50, color="green", linestyle="--", alpha=0.5)
    plt.axhline(-60, color="blue", linestyle="--", alpha=0.5)
    plt.axhline(-70, color="orange", linestyle="--", alpha=0.5)

    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig("simulation_output/signal_strength_plot.png")
    plt.show()


if __name__ == "__main__":

    wifi_networks = [
        ("Home_WiFi", -45),
        ("Office_WiFi", -55),
        ("College_WiFi", -65),
        ("Guest_WiFi", -75),
        ("Mobile_Hotspot", -48)
    ]

    results = analyze_signals(wifi_networks)

    display_results(results)
    plot_signals(results)
