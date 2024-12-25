# **Single-Slit Diffraction Simulation**

This project simulates the **diffraction pattern** produced by a single slit when light or other waves pass through it. The program provides both **1D visualization** of the intensity pattern and a **2D heatmap** of the intensity distribution on a screen.

## **Features**

- **1D Diffraction Pattern**:
  - Visualize the intensity distribution as a function of diffraction angle.
  - Observe changes in the pattern with adjustable parameters.
- **2D Intensity Heatmap**:

  - Simulate the diffraction intensity on a 2D screen using a heatmap.
  - Observe how the pattern changes dynamically with user input.

- **Interactive Parameters**:
  - Adjust **slit width** and **wavelength** using sliders to explore their effects on diffraction.

## **How It Works**

The program uses the following physics principles and mathematical equations:

1. **Intensity Calculation**:
   The intensity of the diffraction pattern is given by:
   \[
   I(\theta) = \left( \frac{\sin(\beta)}{\beta} \right)^2, \quad \beta = \frac{\pi a \sin\theta}{\lambda}
   \]
   where:

   - \( a \): Slit width
   - \( \lambda \): Wavelength
   - \( \theta \): Diffraction angle

2. **Heatmap Calculation**:
   Intensity values are computed for a 2D grid of points on a screen, representing the light intensity distribution.

## **Requirements**

Make sure you have the following dependencies installed:

- **Python 3.7+**
- **NumPy**
- **Matplotlib**

You can install the dependencies with the following command:

```bash
pip install numpy matplotlib
```

## **Usage**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/single-slit-diffraction.git
   cd single-slit-diffraction
   ```
2. Run the program:

   ```bash
   python single_slit_diffraction.py
   ```

3. Adjust the sliders for:

   - **Slit Width** (\( a \))
   - **Wavelength** (\( \lambda \))

4. Observe the changes in:
   - The **1D diffraction intensity plot**.
   - The **2D heatmap of the diffraction pattern**.

## **Screenshots**

### **1D Diffraction Pattern**

![1D Diffraction Pattern](attachemnt:1D_plot.png)

### **2D Intensity Heatmap**

![2D Heatmap](attachment:2D_plot.png)

## **Physics Background**

This program demonstrates the phenomenon of **diffraction**, which occurs when a wave encounters an obstacle or a slit comparable in size to its wavelength. The single-slit diffraction pattern is an interference effect described by the Huygens-Fresnel principle.

## **Future Extensions**

Possible enhancements to the program include:

- Adding support for **double-slit diffraction**.
- Implementing **color visualization** for different wavelengths.
- Exporting plots as **image files**.

## **Contributing**

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## **Acknowledgements**

Thanks to [Matplotlib](https://matplotlib.org/) and [NumPy](https://numpy.org/) for providing powerful tools for data visualization and numerical computation. And of course, special thanks to [ChatGPT](https://chatgpt.com/) for assisting me.
