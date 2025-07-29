import numpy as np
import matplotlib.pyplot as plt

def evaluate_polar_equation(eq_str, theta, a):
    # converts ^ to **
    eq_str = eq_str.replace("^", "**").strip()
    
    # safer eval context
    local_ns = {
        "np": np,
        "theta": theta,
        "a": a,
        "e": np.e,
        "pi": np.pi
    }
    
    try:
        if eq_str.lower().startswith("r**2") or eq_str.lower().startswith("r^2"):
            rhs = eq_str.split("=")[1].strip()
            r_squared = eval(rhs, local_ns)
            # reserves sign for proper negative handling
            r = np.sqrt(np.abs(r_squared)) * np.sign(r_squared)
        elif eq_str.lower().startswith("r"):
            rhs = eq_str.split("=")[1].strip()
            r = eval(rhs, local_ns)
        else:
            raise ValueError("Equation must begin with 'r =' or 'r^2 ='.")
    except Exception as e:
        raise ValueError(f"Invalid equation: {e}")
    
    return r

def plot_polar(r, theta, eq_str, lower_bound, upper_bound):
  
    # separate positive and negative r values
    r_pos = r[r >= 0]
    theta_pos = theta[r >= 0]

    r_neg = -r[r < 0]  # reflect magnitude
    theta_neg = theta[r < 0] + np.pi  # reflects angle
    # Creates the plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='polar')

    ax.plot(theta_pos, r_pos, label='r ≥ 0', color='blue', linewidth=2)
    ax.plot(theta_neg, r_neg, label='r < 0 (reflected)', color='red', linestyle='dotted', linewidth=2)

    ax.set_title(f"Polar Plot: {eq_str}\nθ ∈ [{lower_bound:.2f}, {upper_bound:.2f}]")
    ax.legend(loc='upper right')

    ax.autoscale_view()
    plt.tight_layout()
    plt.show()

def main():
    print("Enter a polar equation using 'theta' and 'a' (optional).")
    print("Examples:")
    print(" - r = a * np.cos(3 * theta)")
    print(" - r^2 = a * np.sin(2 * theta) + 4")
    print(" - r = a * np.exp(theta)")
    print(" - r = a * theta**2")

    eq_str = input("Equation (r = ... or r^2 = ...): ")
    
    # parameter 'a'
    try:
        a = float(input("Enter value for parameter a (default = 1): ") or 1.0)
    except:
        a = 1.0

    # angle bounds
    try:
        lower_bound = float(input("Enter lower theta bound in radians (default = 0): ") or 0)
        upper_bound = float(input("Enter upper theta bound in radians (default = 2*pi): ") or (2 * np.pi))
    except:
        lower_bound, upper_bound = 0, 2 * np.pi

    # theta values
    theta = np.linspace(lower_bound, upper_bound, 1000)

    try:
        r = evaluate_polar_equation(eq_str, theta, a)
        plot_polar(r, theta, eq_str, lower_bound, upper_bound)
    except Exception as e:
        print("Error:", e)

# good ol' if name main stuff here
if __name__ == "__main__":
    while True:
      # gon repeat till user ends program
        main()
        print("\nNew session started\n")
