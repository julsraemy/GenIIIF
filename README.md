# Gen IIIF
The IIIF ([International Image Interoperability Framework](https://iiif.io/)) Resources Generator (Gen IIIF) has been created in the context of the seminar _Angewandte Programmierprojekte_ at the University of Basel and also for the needs of the Participatory Knowledge Practices in Analogue and Digital Image Archives (PIA) project.

## Rationale
At the moment, the PIA infrastructure, though the deployment of the Simple Image Presentation Interface ([SIPI](https://sipi.io/)), supports the IIIF Image API 3.0 but the idea is to deploy further IIIF APIs, above all the IIIF Presentation API 3.0 in oder to display the digital resources (objects and collections) in IIIF-compliant viewers such as Mirador or the Universal Viewer. 
If a couple of IIIF Manifests were manually created for showcase purposes, a semi-automatic way to create those IIIF resources needs to be found.

## IIIF-compliant resources
IIIF-compliant resources are serialised in [JSON-LD](https://json-ld.org/). From the different types (cf. Data Model below), there are two important ones (`Manifest` and `Collection`): 

- `Manifest` are the equivalent of a compound object and contain the descriptive metadata as well as the structure, descrived with `Ranges`, of how the object is composed by pointing to image-based content (images and audiovisual assets) embedded in an abstract space called a `Canvas` - either static content or deferencing to a digital service compliant with the IIIF Image APIs (V2 or 3) can be included.
- `Collection` is an ordered list of Manifests or Collections. 

![IIIF Data Model](https://iiif.io/api/assets/images/data-model.png)

## Scope
### Use cases
Gen IIIF will handle these four straightforward use cases:

1. Manifest with a single image
2. Manifest with a series of images
3. Collection of manifests
4. Collection of collections (top-level collection)

For each use case, [fixtures](fixtures/fixtures.md) and [templates](templates/templates.md) will be generated.

### Method
The conceived method to create IIIF-compliant resources is to create a form on a minimalist graphical user interface (GUI) that end users would have to fill out.

Another alternative methods that could be created is to extract the metadata from a CSV or a database.

### Usage of Gen IIIF
TBD

#### Dependencies
[Tkinter](https://realpython.com/python-gui-tkinter/)

#### Steps
TBD

#### Examples
TBD

## References
- [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
- [Presentation API Validator](https://presentation-validator.iiif.io/)
- [IIIF Fixtures Repository](https://fixtures.iiif.io/)
- [The IIIF Cookbook](https://iiif.io/api/cookbook/)
- [iiif-prezi3](https://github.com/iiif-prezi/iiif-prezi3)
