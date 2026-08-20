WiFi Signal Strength Analyzer 📶
Overview

WiFi Signal Strength Analyzer is a Python-based project that analyzes the Received Signal Strength Indicator (RSSI) of WiFi networks. It classifies the signal as Excellent, Good, Fair, or Weak and provides a graphical representation of the signal strength.

Features
📶 WiFi RSSI signal analysis
📊 Signal quality classification
🧪 Automated testbench
✅ Unit testing
📈 Signal-strength visualization
🐍 Developed using Python
Signal Classification
RSSI Value	Signal Quality
-50 dBm or higher	Excellent
-51 to -60 dBm	Good
-61 to -70 dBm	Fair
Below -70 dBm	Weak

Note: RSSI values are negative in typical WiFi measurements. A value closer to 0 dBm generally represents a stronger signal.

Project Structure
wifi-signal-strength-analyzer/
│
├── README.md
├── wifi_signal_analyzer.py
├── testbench.py
├── test_wifi_signal_analyzer.py
├── requirements.txt
├── .gitignore
└── simulation_output/
    └── signal_strength_plot.png

Requirements
Python 3.x
Matplotlib

Install the required library using:

pip install -r requirements.txt

How to Run
Run the WiFi analyzer
python wifi_signal_analyzer.py


The program analyzes sample WiFi networks and generates a signal-strength graph.

Run the testbench
python testbench.py


The testbench checks different RSSI values and displays their corresponding signal quality.

Run unit tests
python -m unittest test_wifi_signal_analyzer.py

Example Input
Home_WiFi        -45 dBm
Office_WiFi      -55 dBm
College_WiFi     -65 dBm
Guest_WiFi       -75 dBm
Mobile_Hotspot   -48 dBm

Example Output
Network             RSSI (dBm)     Quality
-------------------------------------------------------
Home_WiFi           -45            Excellent
Office_WiFi         -55            Good
College_WiFi        -65            Fair
Guest_WiFi          -75            Weak
Mobile_Hotspot      -48            Excellent

Simulation

The project uses simulated RSSI values to represent different WiFi signal conditions.

The generated graph is saved in:

simulation_output/signal_strength_plot.png

Testing

The testbench verifies:

Excellent signal classification
Good signal classification
Fair signal classification
Weak signal classification
Boundary values at -50 dBm, -60 dBm, and -70 dBm
Applications

This project can be used for:

WiFi network monitoring
Network performance analysis
Wireless communication experiments
Signal-strength visualization
Academic mini-projects
Future Improvements
Scan real WiFi networks automatically
Display SSID, channel, and frequency
Add a real-time signal-strength monitor
Create a graphical user interface
Store signal measurements in CSV files
Add signal-strength history graphs
Conclusion

The WiFi Signal Strength Analyzer provides a simple way to understand and visualize wireless signal quality using RSSI values. The combination of Python programming, simulation, testbench, and visualization makes it suitable for learning and academic projects.

Author

WiFi Signal Strength Analyzer Project

Built with Python 🐍
