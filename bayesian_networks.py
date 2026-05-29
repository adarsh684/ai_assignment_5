from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

bn = DiscreteBayesianNetwork([
    ("Rain", "WetGrass"),
    ("Rain", "Traffic"),
    ("Sprinkler", "WetGrass")
])

# Prior probability of Rain
rain_cpd = TabularCPD(
    variable="Rain",
    variable_card=2,
    values=[
        [0.7],   # No Rain
        [0.3]    # Rain
    ]
)

# Prior probability of Sprinkler
sprinkler_cpd = TabularCPD(
    variable="Sprinkler",
    variable_card=2,
    values=[
        [0.6],   # Off
        [0.4]    # On
    ]
)

# WetGrass depends on Rain and Sprinkler
wetgrass_cpd = TabularCPD(
    variable="WetGrass",
    variable_card=2,
    values=[
        [0.99, 0.30, 0.20, 0.01],  # Not Wet
        [0.01, 0.70, 0.80, 0.99]   # Wet
    ],
    evidence=["Rain", "Sprinkler"],
    evidence_card=[2, 2]
)

# Traffic depends on Rain
traffic_cpd = TabularCPD(
    variable="Traffic",
    variable_card=2,
    values=[
        [0.90, 0.25],  # Light Traffic
        [0.10, 0.75]   # Heavy Traffic
    ],
    evidence=["Rain"],
    evidence_card=[2]
)

bn.add_cpds(
    rain_cpd,
    sprinkler_cpd,
    wetgrass_cpd,
    traffic_cpd
)

print("Network Valid:", bn.check_model())

# Inference Engine
infer = VariableElimination(bn)

print("\nProbability of Wet Grass\n")
print(infer.query(variables=["WetGrass"]))

print("\nProbability of Rain given Wet Grass\n")
print(
    infer.query(
        variables=["Rain"],
        evidence={"WetGrass": 1}
    )
)

print("\nProbability of Heavy Traffic given Rain\n")
print(
    infer.query(
        variables=["Traffic"],
        evidence={"Rain": 1}
    )
)