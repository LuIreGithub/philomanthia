
import numpy as np
import matplotlib.pyplot as plt


def simulate_clt(sample_size=30, repetitions=10000):
    # Simulate repeated samples of dice rolls
    samples = np.random.randint(
        1, 7, size=(repetitions, sample_size)
    )

    # Calculate the mean of each sample
    sample_means = np.mean(samples, axis=1)

    # Theoretical parameters of a fair die
    mu = 3.5
    sigma = np.sqrt(35 / 12)

    # Standard deviation of the sample mean
    standard_error = sigma / np.sqrt(sample_size)

    # Theoretical normal density
    x = np.linspace(
        mu - 4 * standard_error,
        mu + 4 * standard_error,
        1000
    )

    y = (
        1 / (standard_error * np.sqrt(2 * np.pi))
        * np.exp(-0.5 * ((x - mu) / standard_error) ** 2)
    )

    # Plot the simulated sample means
    plt.hist(
        sample_means,
        bins=40,
        density=True,
        alpha=0.6,
        label="Sample means"
    )

    # Plot the theoretical normal approximation
    plt.plot(x, y, color="red", label="Normal approximation")

    plt.xlabel("Sample mean")
    plt.ylabel("Probability density")
    plt.title(f"Central Limit Theorem (n={sample_size})")
    plt.legend()
    plt.show()
