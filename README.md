# Polar Equation Grapher

This is a Python-based command-line tool that allows you to **visualize polar equations** of the form:

- `r = f(θ)`  
- `r² = f(θ)`

It supports complex expressions, includes handling for **negative radius values** (dashed lines), and allows you to tweak parameters easily. Ideal for students, teachers, or anyone studying polar coordinates or mathematical curves!

---

## Features

- Plots any polar equation involving `r` or `r²`
- Automatically reflects and styles negative radius values with dotted lines
- Uses `numpy` for fast evaluation and `matplotlib` for smooth polar plots
- Interactive CLI that supports continuous plotting sessions
- Handles equations using `^`, `np`, `theta`, `a`, and constants like `e`, `π`

---

## Installation

Make sure you have Python installed (3.6+ recommended).

Install the required packages:

```bash
pip install numpy matplotlib
````

---

## Usage

Run the script:

```bash
python polar_grapher.py
```

Then follow the prompts to input your equation and parameters.

### Example Inputs

* `r = a * np.cos(3 * theta)`
* `r = a * np.exp(theta)`
* `r = a * theta**2`
* `r^2 = a * np.sin(2 * theta) + 4`

You'll also be prompted for:

* A value for `a` (default = 1)
* Lower and upper bounds for `θ` (default = `0` to `2π`)

---

## Notes

* Use `theta` for the angle variable and `a` as your parameter.
* You can use any valid NumPy functions like `np.sin`, `np.exp`, etc.
* Use `^` or `**` for exponentiation. `^` will be auto-converted.
* Negative `r` values are shown as **dotted red lines**, reflected across the origin.

---

## Looping Feature

The program runs in a loop by default, so you can graph multiple equations in one session. Just close the window or press `Ctrl+C` to stop.

---
