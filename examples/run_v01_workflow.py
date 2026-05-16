import drugdiscovery as dd


library = dd.load_library("examples/example_ligands.csv")
ranked = dd.rank_hits(library)

ranked.to_csv("examples/ranked_hits.csv", index=False)

print(ranked[[
    "compound_id",
    "docking_score",
    "ligand_efficiency",
    "lipinski_pass",
    "veber_pass",
    "priority_score",
]])
