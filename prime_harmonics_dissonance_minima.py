import numpy as np
import matplotlib.pyplot as plt

# ===== Sethares roughness =====
def roughness(f1, a1, f2, a2):
    """
    Computes sensory dissonance between two sine partials
    using Sethares (1993) Plomp-Levelt-inspired model.
    """
    f_min = min(f1, f2)
    s = 0.24 / (0.021 * f_min + 19.0)
    x = abs(f1 - f2)
    return a1 * a2 * (np.exp(-3.5 * s * x) - np.exp(-5.75 * s * x))

# ===== Prime checker =====
def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True

# ===== Generate prime harmonics =====
def generate_prime_harmonics(f0, max_harmonic=19, amp_decay_power=0.3):
    
    primes = [p for p in range(2, max_harmonic + 1) if is_prime(p)]
    freqs = np.array([f0 * p for p in primes], dtype=float)
    amps = 1.0 / (np.array(primes, dtype=float) ** amp_decay_power)
    return freqs, amps

# ===== Total dissonance =====
def total_dissonance(f1, f2, max_harmonic=19, amp_decay_power=0.3):
    freqs1, amps1 = generate_prime_harmonics(f1, max_harmonic, amp_decay_power)
    freqs2, amps2 = generate_prime_harmonics(f2, max_harmonic, amp_decay_power)
    total = 0.0
    for i in range(len(freqs1)):
        for j in range(len(freqs2)):
            total += roughness(freqs1[i], amps1[i], freqs2[j], amps2[j])
    return total

# ===== Annotate valleys with prime ratios =====
def prime_ratios(max_harmonic=19):
    primes = [p for p in range(2, max_harmonic + 1) if is_prime(p)]
    ratios = []
    for p1 in primes:
        for p2 in primes:
            ratio = p1 / p2
            if 1.0 <= ratio <= 2.0:
                ratios.append((ratio, f"{p1}:{p2}"))
    # Sort and remove near-duplicates
    ratios.sort(key=lambda x: x[0])
    unique = []
    seen = []
    for r, label in ratios:
        if not any(abs(r - s) < 0.005 for s in seen):  # avoid close duplicates
            unique.append((r, label))
            seen.append(r)
    return unique

# ===== Main sweep =====
f1 = 440.0
ratios = np.logspace(0, np.log10(2), 800)
dissonances = [total_dissonance(f1, f1 * r, max_harmonic=19, amp_decay_power=0.3) for r in ratios]

# ===== Plot =====
plt.figure(figsize=(11, 6))
plt.semilogx(ratios, dissonances, color='teal')
plt.xlabel("Frequency ratio f2/f1 (log scale)")
plt.ylabel("Sensory dissonance (a.u.)")
plt.title("Sethares Sensory Dissonance — Prime Harmonics up to 19th\nBase f1 = {:.1f} Hz".format(f1))
plt.grid(True, which='both', ls='--', alpha=0.6)
plt.xlim(1.0, 2.0)

# ===== Annotate prime harmonic ratios =====
for r, label in prime_ratios(max_harmonic=19):
    idx = (np.abs(ratios - r)).argmin()
    y = dissonances[idx]
    plt.plot(r, y, 'ro', markersize=4)
    plt.text(r, y + 0.02 * max(dissonances), label,
             ha='center', va='bottom', fontsize=8, rotation=0)

plt.show()