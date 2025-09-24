# main.py
import datetime
from constants import (
    KI_VALUES,
    IONIZATION_THRESHOLDS,
    IRON_ATOMIC_WEIGHT,
    IRON_MOLAR_VOLUME,
    ENERGY_COEFFICIENT,
    MAGNETIC_MOMENT_CONSTANT,
    AVOGADRO_NUMBER,
    IRON_MASS_FRACTION,
    REFERENCE_SCALING_CONSTANT
)


def print_header():
    now = datetime.datetime.now()
    print("===============================================")
    print(" Magnetic Moment Calculation Script")
    print(f" Date: {now.date()} Time: {now.strftime('%H:%M:%S')}")
    print("===============================================\n")


def calculate_critical_density(a: float, c: float) -> float:
    """Compute critical density s = a / c"""
    return a / c


def radius_of_action(c: float) -> float:
    """Compute radius of action b = 0.5 * (5 * c)^(1/3)"""
    return 0.5 * ((5 * c) ** (1 / 3))


def energy_from_radius(b: float, coefficient: float) -> float:
    """Compute energy e = coefficient / b"""
    return coefficient / b


def generate_energy_phases(e0: float, max_phase: int = 14):
    cube_root_2 = 2 ** (1 / 3)
    phases = []

    # Phase 1
    E1 = e0 * (cube_root_2 ** 1)
    phases.append((1, round(E1, 4), 1.0))

    for i in range(2, max_phase + 1):
        Ei = e0 * (cube_root_2 ** i)
        mult = Ei / E1
        phases.append((i, round(Ei, 4), round(mult, 4)))

    return phases


def check_ionization(e0: float, shell: str, electrons_in_shell: int):
    E_shell = e0 * electrons_in_shell
    threshold = IONIZATION_THRESHOLDS.get(shell.upper())
    if threshold is None:
        raise ValueError(f"No threshold defined for shell '{shell}'")
    exceeded = E_shell > threshold
    return round(E_shell, 4), threshold, exceeded


def calculate_magnetic_moment(i_phase: int):
    if i_phase < 0 or i_phase >= len(KI_VALUES):
        raise ValueError(f"Invalid i_phase {i_phase}. Must be between 0 and {len(KI_VALUES) - 1}")

    ki = KI_VALUES[i_phase]
    sixth_root_vm = IRON_MOLAR_VOLUME ** (1 / 6)
    ratio = sixth_root_vm / IRON_ATOMIC_WEIGHT
    mu_1 = MAGNETIC_MOMENT_CONSTANT * ratio * ki
    mu_total = (AVOGADRO_NUMBER * mu_1 * IRON_MASS_FRACTION * REFERENCE_SCALING_CONSTANT) / IRON_ATOMIC_WEIGHT

    print("=== Magnetic Moment Calculation Details ===")
    print(f"i_phase index: {i_phase}")
    print(f"KI value (ki): {ki}")
    print(f"IRON_MOLAR_VOLUME^(1/6): {sixth_root_vm:.6e}")
    print(f"Ratio (sixth_root_vm / IRON_ATOMIC_WEIGHT): {ratio:.6e}")
    print(f"MAGNETIC_MOMENT_CONSTANT: {MAGNETIC_MOMENT_CONSTANT:.6e}")
    print(f"mu_1 = MAGNETIC_MOMENT_CONSTANT * ratio * ki = {mu_1:.6e}")
    print(f"AVOGADRO_NUMBER: {AVOGADRO_NUMBER:.6e}")
    print(f"IRON_MASS_FRACTION: {IRON_MASS_FRACTION:.6e}")
    print(f"REFERENCE_SCALING_CONSTANT: {REFERENCE_SCALING_CONSTANT:.6e}")
    print(f"IRON_ATOMIC_WEIGHT: {IRON_ATOMIC_WEIGHT:.6e}")
    print(f"mu_total = (AVOGADRO_NUMBER * mu_1 * IRON_MASS_FRACTION * REFERENCE_SCALING_CONSTANT) / IRON_ATOMIC_WEIGHT = {mu_total:.6e}")

    return mu_1, mu_total



def display_energy_phases(phases):
    print("\nSummary of Energy Phases (i=1 to i=N):")
    print(f"{'Phase i':>8} | {'Energy E_i':>12} | {'Multiplier to E1':>20}")
    print("-" * 45)
    for i, energy, mult in phases:
        print(f"{i:>8} | {energy:>12.4f} | {mult:>20.4f}")
    print("-" * 45 + "\n")


def main():
    print_header()

    s = calculate_critical_density(IRON_ATOMIC_WEIGHT, IRON_MOLAR_VOLUME)
    print(f"Step 1: Critical density s = a / c = {s:.4f}")

    ratio_detail = 0.3333
    s2 = round(s * ratio_detail, 4)
    print(f"Step 2: s2 = s * {ratio_detail} = {s2:.4f}")

    b = radius_of_action(IRON_MOLAR_VOLUME)
    print(f"Radius of action b = 0.5 * (5 * c)^(1/3) = {b:.4f}")

    e0 = energy_from_radius(b, ENERGY_COEFFICIENT)
    print(f"Energy corresponding to radius of action: e0 = {e0:.4f}")

    phases = generate_energy_phases(e0, max_phase=14)
    display_energy_phases(phases)

    for shell, electrons in [("N", 2), ("M", 14), ("L", 8), ("K", 2)]:
        E_shell, threshold, exceeded = check_ionization(e0, shell, electrons)
        print(f"Ionization check for shell {shell} (electrons={electrons}):")
        print(f" Computed energy: {E_shell}")
        print(f" Threshold: {threshold}")
        print(f" Exceeded: {exceeded}\n")

    i_phase = 6
    mu_1, mu_total = calculate_magnetic_moment(i_phase)
    print(f"Magnetic moment per atom (phase {i_phase}): {mu_1:.3e} (erg/Gauss)")
    print(f"Magnetic moment total (phase {i_phase}): {mu_total:.3e} (erg/Gauss)")


if __name__ == "__main__":
    main()
