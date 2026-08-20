from wifi_signal_analyzer import analyze_signals, display_results


def run_testbench():

    test_data = [
        ("Excellent_Network", -40),
        ("Good_Network", -55),
        ("Fair_Network", -65),
        ("Weak_Network", -80),
        ("Boundary_50", -50),
        ("Boundary_60", -60),
        ("Boundary_70", -70)
    ]

    print("=" * 60)
    print("       WiFi SIGNAL STRENGTH ANALYZER TESTBENCH")
    print("=" * 60)

    results = analyze_signals(test_data)

    display_results(results)

    print("\nTestbench completed successfully.")


if __name__ == "__main__":
    run_testbench()
