#Regular expressions
#Concept of unit tests - iterate through tests of your modular functions
#Writing functionally as opposed to procedurally allows for modularity
#Spaces matter in regular expressions
#The concept of the "greedy" algorithm - * is an example
#In the "big data" era, people are better about delivering structured text files
#Regular expressions are useful to search through such structured text

import re

regex = r'^(\w+)\^'

test1 = 'CXE13_ARATH^CXE13_ARATH^Q:93-266,H:4-63^45%ID^E:2.23e-09^RecName: Full=Probable carboxylesterase 13;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis HIBC6_ARATH^HIBC6_ARATH^Q:2-289,H:322-417^64.583%ID^E:4.82e-37^RecName: Full=3-hydroxyisobutyryl-CoA hydrolase-like protein 3, mitochondrial;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis JMJ25_ARATH^JMJ25_ARATH^Q:2-481,H:683-825^48.148%ID^E:2.91e-38^RecName: Full=Lysine-specific demethylase JMJ25;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis HSP81_ORYSJ^HSP81_ORYSJ^Q:1-150,H:650-699^96%ID^E:4.42e-25^RecName: Full=Heat shock protein 81-1;^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; Liliopsida; Poales; Poaceae; BOP clade; Oryzoideae; Oryzeae; Oryzinae; Oryza'

test2 = 'ERL1_ARATH^ERL1_ARATH^Q:1-216,H:56-128^41.892%ID^E:1.08e-09^RecName: Full=LRR receptor-like serine/threonine-protein kinase ERL1 {ECO:0000303|PubMed:14985254};^Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta; Spermatophyta; Magnoliophyta; eudicotyledons; Gunneridae; Pentapetalae; rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis'

result = re.search(regex, test1)

print(result)

groups = result.groups()

#This is a powerful technique for searching huge text files
#Now find all the sections between the carats AFTER the GO section

regex2 = r'(GO:\d+\^)(\w+)'

test3 = 'GO:1904115^cellular_component^axon cytoplasmGO:0005737^cellular_component^cytoplasmGO:0031410^cellular_component^cytoplasmic vesicleGO:0005829^cellular_component^cytosolGO:0005789^cellular_component^endoplasmic reticulum membraneGO:0071782^cellular_component^endoplasmic reticulum tubular networkGO:0005768^cellular_component^endosomeGO:0070062^cellular_component^extracellular exosomeGO:0005811^cellular_component^lipid dropletGO:0005874^cellular_component^microtubuleGO:0005815^cellular_component^microtubule organizing centerGO:0030496^cellular_component^midbodyGO:0031965^cellular_component^nuclear membraneGO:0005654^cellular_component^nucleoplasmGO:0005634^cellular_component^nucleusGO:0048471^cellular_component^perinuclear region of cytoplasmGO:0005819^cellular_component^spindleGO:0043014^molecular_function^alpha-tubulin bindingGO:0005524^molecular_function^ATP bindingGO:0048487^molecular_function^beta-tubulin bindingGO:0008017^molecular_function^microtubule bindingGO:0008568^molecular_function^microtubule-severing ATPase activityGO:0008089^biological_process^anterograde axonal transportGO:0019896^biological_process^axonal transport of mitochondrionGO:0030154^biological_process^cell differentiationGO:0032506^biological_process^cytokinetic processGO:0061640^biological_process^cytoskeleton-dependent cytokinesisGO:0006888^biological_process^ER to Golgi vesicle-mediated transportGO:0010458^biological_process^exit from mitosisGO:0090148^biological_process^membrane fissionGO:0008152^biological_process^metabolic processGO:0001578^biological_process^microtubule bundle formationGO:0051013^biological_process^microtubule severingGO:0000281^biological_process^mitotic cytokinesisGO:0051228^biological_process^mitotic spindle disassemblyGO:0007399^biological_process^nervous system developmentGO:0006998^biological_process^nuclear envelope organizationGO:0031468^biological_process^nuclear envelope reassemblyGO:0032467^biological_process^positive regulation of cytokinesisGO:0034214^biological_process^protein hexamerizationGO:0051260^biological_process^protein homooligomerization`GO:0051230^biological_process^spindle disassembly'

newResult = re.findall(regex2, test3)

print(newResult)

for t in newResult:
    for j in t:
        print j
        
#Homework - Practice 2