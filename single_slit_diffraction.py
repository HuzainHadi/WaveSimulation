import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Diffraction intensity calculation
def diffraction_intensity(a, wavelength, theta):
    """
    Calculate the intensity of the single-slit diffraction pattern.
    a: Slit width (m)
    wavelength: Wavelength of light (m)
    theta: Diffraction angle (radians)
    """
    beta = (np.pi * a * np.sin(theta)) / wavelength
    intensity = (np.sin(beta) / beta) ** 2
    intensity[beta == 0] = 1  # Avoid division by zero
    return intensity

# 2D intensity map calculation
def calculate_2d_intensity(a, wavelength, screen_x, screen_y):
    """
    Calculate the intensity on a 2D screen.
    a: Slit width (m)
    wavelength: Wavelength of light (m)
    screen_x, screen_y: 2D grid coordinates of the screen
    """
    theta = np.arctan2(screen_y, screen_x)  # Angle to each point on the screen
    intensity = diffraction_intensity(a, wavelength, theta)
    return intensity

# Initial parameters
a_initial = 5e-6  # Slit width in meters
wavelength_initial = 500e-9  # Wavelength in meters (500 nm)
theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)  # Angle range in radians

# 2D screen setup
screen_size = 0.01  # Screen size (10 cm)
resolution = 500  # Resolution of the intensity map
x = np.linspace(-screen_size, screen_size, resolution)
y = np.linspace(-screen_size, screen_size, resolution)
screen_x, screen_y = np.meshgrid(x, y)
intensity_2d_initial = calculate_2d_intensity(a_initial, wavelength_initial, screen_x, screen_y)

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plt.subplots_adjust(bottom=0.4)  # Increased bottom margin for more space

# Plot 1D diffraction pattern
intensity_initial = diffraction_intensity(a_initial, wavelength_initial, theta)
line, = ax1.plot(theta, intensity_initial, label='Diffraction Pattern', color='blue')
ax1.set_title("1D Single-Slit Diffraction Pattern", fontsize=14)
ax1.set_xlabel("Angle (radians)")
ax1.set_ylabel("Intensity")
ax1.grid(True)

# Plot 2D intensity map
intensity_map = ax2.imshow(intensity_2d_initial, extent=(-screen_size, screen_size, -screen_size, screen_size), cmap='hot', origin='lower')
ax2.set_title("2D Diffraction Intensity Map", fontsize=14)
ax2.set_xlabel("Screen X (m)")
ax2.set_ylabel("Screen Y (m)")

# Change horizontal axis tick labels to vertical in 2D plot
ax2.tick_params(axis='x', labelrotation=90)

# Add sliders
ax_a = plt.axes([0.15, 0.25, 0.65, 0.03])  # Adjusted positions for extra spacing
ax_lambda = plt.axes([0.15, 0.2, 0.65, 0.03])
slider_a = Slider(ax_a, 'Slit Width (m)', 1e-6, 10e-6, valinit=a_initial, valstep=1e-7)
slider_lambda = Slider(ax_lambda, 'Wavelength (m)', 400e-9, 700e-9, valinit=wavelength_initial, valstep=10e-9)

# Update function
def update(val):
    a = slider_a.val
    wavelength = slider_lambda.val

    # Update 1D diffraction pattern
    intensity = diffraction_intensity(a, wavelength, theta)
    line.set_ydata(intensity)

    # Update 2D intensity map
    intensity_2d = calculate_2d_intensity(a, wavelength, screen_x, screen_y)
    intensity_map.set_data(intensity_2d)

    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_lambda.on_changed(update)

# Show the interactive plot
plt.show()
