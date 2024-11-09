import math


# Property constants for aluminum 6061
ystress = 83  # Yield Strength  (MPa)
young_mod = 69000  # Youngs modulus  (MPa)

# dimensions of angle
a = 0.5  # Cross section length (in)
c = 0.0625  # Thickness (in)
length = 6  # Length (in)

# unit conversion to meters
a = a / 39.37  # m
c = c / 39.37  # m
length = length / 39.37  # m

# cross-sectional area
area = 2 * (a * c) - (c**2)  # m^2

# moment of inertia about the x-axis from the outside origin (m^2)
moment_0 = (c / 3) * ((a * c**2) + (a**3) - (c**3))

# Area moment of inertia around centroid found by parallel axis thereom (m^4)
sec_moment = moment_0 - area * ((1 / area) * ((c / 2) * (a**2 + a * c - c**2))) ** 2

# radius of gyration (of moment of inertia) found by the square root of the area moment of inertia divided the cross-sectional area (m^2)
radius_of_g = (sec_moment / area) ** (1 / 2)

# slenderness ratio found by the length divided by the radius of gyration
slenderness_r = length / radius_of_g

# Johnsons formula used to find the maximum force before buckling in a short column
critical_load_stress = (
    ystress
    - (1 / young_mod) * ((ystress / (2 * math.pi)) * (length / radius_of_g)) ** 2
)  # (MPa)
critical_load_stress = critical_load_stress * 1000000  # convert MPa to Pa
critcal_load = area * critical_load_stress  # Find the critical load in newtons (N)

print(
    f"The critical stress before buckling is {critical_load_stress / (10**6):.2f} MPa"
)
print(f"The critical force before buckling is {critcal_load:.2f} N")
