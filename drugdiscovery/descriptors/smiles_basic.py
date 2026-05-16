import re
from dataclasses import dataclass

import pandas as pd


HBA_ATOMS = {"N", "O", "S"}


@dataclass
class BasicSmilesDescriptors:
    hbd: int
    hba: int
    rotatable_bonds: int
    tpsa: float


def count_atoms(smiles: str, atoms: set[str]) -> int:
    """
    Count simple atom tokens in a SMILES string.

    This is an approximate parser intended for early DrugDiscovery-Py workflows.
    It does not fully handle all SMILES grammar, stereochemistry, charges, or
    aromaticity edge cases.
    """
    if not isinstance(smiles, str):
        return 0

    tokens = re.findall(r"Cl|Br|[A-Z][a-z]?|[cnosp]", smiles)
    normalized = [token.upper() if len(token) == 1 else token for token in tokens]

    return sum(1 for token in normalized if token in atoms)


def estimate_hba(smiles: str) -> int:
    """Estimate hydrogen bond acceptors from simple heteroatom counts."""
    return count_atoms(smiles, HBA_ATOMS)


def estimate_hbd(smiles: str) -> int:
    """
    Estimate hydrogen bond donors from simple N/O/[nH] patterns.

    This is deliberately approximate and should not be interpreted as a
    cheminformatics-grade descriptor.
    """
    if not isinstance(smiles, str):
        return 0

    count = 0
    count += len(re.findall(r"\[nH\]|\[NH[0-9]?\]|\[OH[0-9]?\]", smiles))
    count += len(re.findall(r"(?<!\[)[NO](?![a-z])", smiles))

    return count


def estimate_rotatable_bonds(smiles: str) -> int:
    """
    Estimate rotatable bonds from simple linker patterns.

    This is a rough approximation and is not a full rotatable-bond perception
    algorithm.
    """
    if not isinstance(smiles, str):
        return 0

    explicit_single = smiles.count("-")

    linker_patterns = [
        r"C[NOS]",
        r"[NOS]C",
        r"CC",
        r"Cc",
        r"cC",
    ]

    inferred = sum(len(re.findall(pattern, smiles)) for pattern in linker_patterns)

    return max(0, int(round((explicit_single + inferred) * 0.5)))


def estimate_tpsa(smiles: str) -> float:
    """
    Estimate TPSA using a simple heteroatom fragment approximation.

    Approximate contributions:
    - N: 12 Å²
    - O: 17 Å²
    - S: 25 Å²
    """
    if not isinstance(smiles, str):
        return 0.0

    n_count = count_atoms(smiles, {"N"})
    o_count = count_atoms(smiles, {"O"})
    s_count = count_atoms(smiles, {"S"})

    return round((12.0 * n_count) + (17.0 * o_count) + (25.0 * s_count), 2)


def calculate_basic_smiles_descriptors(smiles: str) -> BasicSmilesDescriptors:
    """Calculate approximate basic descriptors from SMILES."""
    return BasicSmilesDescriptors(
        hbd=estimate_hbd(smiles),
        hba=estimate_hba(smiles),
        rotatable_bonds=estimate_rotatable_bonds(smiles),
        tpsa=estimate_tpsa(smiles),
    )


def add_basic_smiles_descriptors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing hbd, hba, tpsa, and rotatable_bonds values using approximate
    SMILES-based estimators.

    Existing non-missing values are preserved.
    """
    if "smiles" not in df.columns:
        raise ValueError("Cannot calculate descriptors: missing 'smiles' column.")

    result = df.copy()

    for column in ["hbd", "hba", "tpsa", "rotatable_bonds"]:
        if column not in result.columns:
            result[column] = pd.NA

    calculated = result["smiles"].apply(calculate_basic_smiles_descriptors)

    descriptor_map = {
        "hbd": lambda item: item.hbd,
        "hba": lambda item: item.hba,
        "tpsa": lambda item: item.tpsa,
        "rotatable_bonds": lambda item: item.rotatable_bonds,
    }

    for column, extractor in descriptor_map.items():
        missing_mask = result[column].isna()

        if missing_mask.any():
            result.loc[missing_mask, column] = (
                calculated.loc[missing_mask].apply(extractor).to_list()
            )

    return result
