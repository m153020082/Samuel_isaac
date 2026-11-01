import numpy as np
import omni.timeline
from isaacsim.sensors.experimental.physics import ContactSensor, IMUSensor

# Instantiate sensors
contact_sensor = ContactSensor("/World/RobotFoot/Contact_Sensor")
imu_sensor = IMUSensor("/World/RobotFoot/Imu_Sensor")

timeline = omni.timeline.get_timeline_interface()
timeline.play()

force_history = []
accel_history = []

# Collect data over time steps
for frame in range(200):
    omni.kit.app.get_app().update()
    
    # Read Contact Normal Force (Z-axis force spike)
    contact_data = contact_sensor.get_sensor_reading()
    force_magnitude = contact_data.value
    force_history.append(force_magnitude)
    
    # Read IMU Linear Acceleration (X, Y, Z)
    imu_data = imu_sensor.get_sensor_reading()
    accel_history.append(imu_data.lin_acc)

# Convert to arrays for vibration spectral analysis (FFT)
force_array = np.array(force_history)
accel_array = np.array(accel_history)

# Fast Fourier Transform (FFT) to identify dominant vibration frequencies
freqs = np.fft.fftfreq(len(accel_array[:, 2]), d=1/60.0) # assuming 60Hz physics step
fft_vals = np.abs(np.fft.fft(accel_array[:, 2]))