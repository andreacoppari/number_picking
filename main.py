import matplotlib.pyplot as plt
from collections import defaultdict

# === Configurable Parameters ===

# How far to go (n = 1 to MAX_N)
MAX_N = 9999998

# Maximum sum of the digits (it will overflow, set to MAX_N for no limit)
MAX_SUM = 10000

# If True, draw only final plot; if False, update in real-time
DRAW_AT_END_ONLY = True

# ===============================

digit_sum_counts = defaultdict(int)

if not DRAW_AT_END_ONLY:
    plt.ion()
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
    
    # Plot histogram bars
    bars = ax.bar(keys, values, color='skyblue')

    # Add custom labels below bars
    for bar, label in zip(bars, keys):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            -max(values) * 0.05,  # Slightly below zero
            str(label),
            ha='center',
            va='top',
            fontsize=9
        )

    # Hide x-axis ticks and line
    ax.set_xticks([])
    ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)

    # Mean red line
    mean_x = compute_mean(data)
    ax.axvline(mean_x, color='red', linestyle='--', linewidth=2, label=f"Mean = {mean_x:.2f}")

    ax.set_title("Distribution of Digit Sums")
    ax.set_ylabel("Occurrences")
    ax.legend()
    plt.draw()
    if not DRAW_AT_END_ONLY:
        plt.pause(0.01)

def main():
    for n in range(1, MAX_N + 1):
        digit_sum = sum_of_digits(n)
        digit_sum_counts[digit_sum % MAX_SUM] += 1
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