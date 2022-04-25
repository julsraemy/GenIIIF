# IIIF Collections Generator
The IIIF ([International Image Interoperability Framework](https://iiif.io/)) Collections Generator (GenIIIF) has been created in the context of the seminar _Angewandte Programmierprojekte_ at the University of Basel and also for the needs of the Participatory Knowledge Practices in Analogue and Digital Image Archives (PIA) project.

## Rationale
At the moment, the PIA infrastructure, though the deployment of the Simple Image Presentation Interface ([SIPI](https://sipi.io/)), supports the IIIF Image API 3.0 as well the IIIF Presentation API 3.0 to some extent where [IIIF Manifests have been generated](https://github.com/Participatory-Image-Archives/pia-iiif-manifest-host) on the basis of existing digital surrogates from the Swiss Society for Folklore Studies (SSFS) such as `https://iiif.participatory-archives.ch/14759/manifest.json`. 

The purpose of GenIIIF is for (savvy) end users to create custom IIIF Collections.

## IIIF-compliant resources
IIIF-compliant resources are serialised in [JSON-LD](https://json-ld.org/). From the different types (cf. [Defined Types of the IIIF Data Model](https://iiif.io/api/presentation/3.0/#21-defined-types)), there are two important ones (`Manifest` and `Collection`: 

- `Manifest` are the equivalent of a compound object and contain the descriptive metadata as well as the structure, described with `Ranges`, of how the object is composed by pointing to image-based content (images and audiovisual assets) embedded or painted onto an abstract space called a `Canvas` - either static content available online or content that is dereferenced from a digital service compliant with the IIIF Image APIs (V2.1 or V3) can be included.
- `Collection` is an ordered list of Manifests or Collections which looks like this: 

```
{
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "https://example.com/collection.json",
    "type": "Collection",
    "label": {
      "de": [
        "Label Collection of Manifests"
      ]
    },
    "summary": {
        "en": [
          "IIIF Collection of Manifests"
        ]
      },
    "items": [
      {
        "id": "https://example.com/001/manifest.json",
        "type": "Manifest",
        "label": {
          "de": [
            "Label Manifest 1"
          ]
        }
      },
      {
        "id": "https://example.com/002/manifest.json",
        "type": "Manifest",
        "label": {
          "de": [
            "Label Manifest 2"
          ]
        }
      },
            {
        "id": "https://example.com/003/manifest.json",
        "type": "Manifest",
        "label": {
          "de": [
            "Label Manifest 3"
          ]
        }
      }
    ]
  }
```

## Scope
Adaptation of Leander Seige's [iiifcurator](https://github.com/leanderseige/iiifcurator) which can handle the Presentation API V3 (only V2 at the moment).

## References
- [iiifcurator](https://github.com/leanderseige/iiifcurator)
- [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
- [Presentation API Validator](https://presentation-validator.iiif.io/)
- [IIIF Fixtures Repository](https://fixtures.iiif.io/)
- [The IIIF Cookbook](https://iiif.io/api/cookbook/)
- [iiif-prezi3](https://github.com/iiif-prezi/iiif-prezi3)

## Citation
Raemy, J. A. (2022). GenIIIF (Version 0.1.0) [Computer software]. [![DOI](https://zenodo.org/badge/461769496.svg)](https://zenodo.org/badge/latestdoi/461769496)
