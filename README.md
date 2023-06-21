# Human Liver Microsomal Stability

The Human Liver Microsomal assay takes into account the liver-mediated drug metabolism to assess the stability of a compound in the human body. The NIH-NCATS group took a proprietary dataset of 4300 compounds with its associated HLM (in vitro half-life; unstable ≤  30 min, stable >30 min) and used it to train a classifier.

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
* Interpretation: Probability of a compound being unstable in a HLM assay (half-life ≤ 30min)

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7)
* [Source Code](https://github.com/ncats/ncats-adme/tree/master)
* Ersilia contributor: [pauline-banye](https://github.com/pauline-banye)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos31ve)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00426-7) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!