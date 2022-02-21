# Gen IIIF
The IIIF ([International Image Interoperability Framework](https://iiif.io/)) Resources Generator (Gen IIIF) has been created in the context of the seminar _Angewandte Programmierprojekte_ at the University of Basel and also for the needs of the Participatory Knowledge Practices in Analgue and Digital Image Archives (PIA) project.

## Rationale
At the moment, the PIA infrastructure, though the deployment of the Simple Image Presentation Interface ([SIPI](https://sipi.io/)), supports the IIIF Image API 3.0 but the idea is to deploy further IIIF APIs, above all the IIIF Presentation API 3.0 in oder to display the digital resources (objects and collections) in IIIF-compliant viewers such as Mirador or the Universal Viewer. 
If a couple of IIIF Manifests were manually created for showcase purposes, a semi-automatic way to create those IIIF resources need to be found.

## Use cases
Gen IIIF will handle these four easy use cases:

- Manifest with a single image
- Manifest with a series of images
- Collection of manifests
- Collection of collections (top-level collection)

## References
- [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
- [Presentation API Validator](https://presentation-validator.iiif.io/)
- [IIIF Fixtures Repository](https://fixtures.iiif.io/)
- [The IIIF Cookbook](https://iiif.io/api/cookbook/)
- [iiif-prezi3](https://github.com/iiif-prezi/iiif-prezi3)