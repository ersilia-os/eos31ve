# Human Liver Microsomal Stability

Indicates whether a compound is likely to be cleared rapidly by human liver microsomes, the subcellular fraction carrying cytochrome P450 activity and the usual first checkpoint for metabolic stability. Compounds with a half-life at or below 30 minutes count as unstable. The classifier is one of the ADME@NCATS predictors, built from an in-house NCATS collection of roughly 4,300 compounds with measured microsomal half-lives. Microsomes carry phase I oxidation only, so cytosolic enzymes and conjugative routes stay invisible to this endpoint.

This model was incorporated on 2023-03-27.Last packaged on 2025-10-16.

## Information
### Identifiers
- **Ersilia Identifier:** `eos31ve`
- **Slug:** `ncats-hlm`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Metabolism`, `ADME`, `Microsomal stability`, `Half-life`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability that a compound is unstable in human liver microsomes, meaning a half-life of 30 minutes or less.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hlm_proba1 | float | high | Probability of being metabolized by human liver microsomes |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos31ve](https://hub.docker.com/r/ersiliaos/eos31ve)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos31ve.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos31ve.zip)

### Resource Consumption
- **Model Size (Mb):** `85`
- **Environment Size (Mb):** `2461`
- **Image Size (Mb):** `2596.84`

**Computational Performance (seconds):**
- 10 inputs: `28.97`
- 100 inputs: `19.09`
- 10000 inputs: `127.17`

### References
- **Source Code**: [https://github.com/ncats/ncats-adme/tree/master](https://github.com/ncats/ncats-adme/tree/master)
- **Publication**: [https://doi.org/10.1186/s13321-020-00426-7](https://doi.org/10.1186/s13321-020-00426-7)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [pauline-banye](https://github.com/pauline-banye)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos31ve
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos31ve
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
