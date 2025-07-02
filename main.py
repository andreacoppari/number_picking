import matplotlib.pyplot as plt
from collections import defaultdict

# === Configurable Parameters ===
MAX_N = 1998         # How far to go (n = 1 to MAX_N)
DRAW_AT_END_ONLY = True  # If True, draw only final plot; if False, update in real-time

# Initialize the histogram counter
digit_sum_counts = defaultdict(int)

# Create the plot
if not DRAW_AT_END_ONLY:
    plt.ion()  # Turn on interactive mode only if drawing live
fig, ax = plt.subplots()

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def compute_mean(data):
    total_count = sum(data.values())
    if total_count == 0:
        return 0
    weighted_sum = sum(k * v for k, v in data.items())
    return weighted_sum / total_count

def update_plot(data):
    ax.clear()
    keys = sorted(data.keys())
    values = [data[k] for k in keys]
    
    # Plot histogram
    ax.bar(keys, values, color='skyblue')

    # Compute and draw the red line at the mean
    mean_x = compute_mean(data)
    ax.axvline(mean_x, color='red', linestyle='--', linewidth=2, label=f"Mean = {mean_x}")

    # Labels and legend
    ax.set_title("Distribution of Digit Sums")
    ax.set_xlabel("Digit Sum")
    ax.set_ylabel("Occurrences")
    ax.legend()
    plt.draw()
    if not DRAW_AT_END_ONLY:
        plt.pause(0.01)

def main():
    for n in range(1, MAX_N + 1):
        digit_sum = sum_of_digits(n)
        digit_sum_counts[digit_sum] += 1
        if not DRAW_AT_END_ONLY:
            update_plot(digit_sum_counts)

    if DRAW_AT_END_ONLY:
        update_plot(digit_sum_counts)
        plt.show()
    else:
        plt.ioff()
        plt.show()

    print(f"Finished processing up to n = {MAX_N}")

if __name__ == "__main__":
    main()
