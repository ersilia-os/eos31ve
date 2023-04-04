# Human liver microsomal stability

Prediction of human liver microsomal stability is key for the screening of drugs in the early stage of drug discovery. The liver is the main organ for metabolizing drugs in humans and testing its metabolic stability is essential for the early detection of viable drug compounds. Tge Human Liver Microsomal (HLM) stability is a good approximation of a compound's stability in the human body. NCATS has collected a dataset of 4300 compounds ((t1/2 <= 30 min; unstable, t1/2 > 30 min; stable).

## Identifiers

* EOS model ID: `eos31ve`
* Slug: `ncats-hlm`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of a compound being stable in HLM (half-life >30min)

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/17683964/)
* [Source Code](https://github.com/ncats/ncats-adme)
* Ersilia contributor: [Masroor07](https://github.com/masroor07)

## Citation

If you use this model, please cite the [original authors](https://pubmed.ncbi.nlm.nih.gov/17683964/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under an MIT license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!