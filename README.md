# GenIIIF
The IIIF ([International Image Interoperability Framework](https://iiif.io/)) Resources Generator (GenIIIF) has been created in the context of the seminar _Angewandte Programmierprojekte_ at the University of Basel and also for the needs of the Participatory Knowledge Practices in Analogue and Digital Image Archives (PIA) project.

## Rationale
At the moment, the PIA infrastructure, though the deployment of the Simple Image Presentation Interface ([SIPI](https://sipi.io/)), supports the IIIF Image API 3.0 but the idea is to deploy further IIIF APIs, above all the IIIF Presentation API 3.0 in oder to display the digital resources (objects and collections) in IIIF-compliant viewers such as Mirador or the Universal Viewer. 
If a couple of IIIF Manifests were manually created for showcase purposes, a semi-automatic way to create those IIIF resources needs to be found.

## IIIF-compliant resources
IIIF-compliant resources are serialised in [JSON-LD](https://json-ld.org/). From the different types (cf. Data Model below), there are two important ones (`Manifest` and `Collection`): 

- `Manifest` are the equivalent of a compound object and contain the descriptive metadata as well as the structure, described with `Ranges`, of how the object is composed by pointing to image-based content (images and audiovisual assets) embedded or painted onto an abstract space called a `Canvas` - either static content available online or content that is dereferenced from a digital service compliant with the IIIF Image APIs (V2.1 or V3) can be included.
- `Collection` is an ordered list of Manifests or Collections. 

![IIIF Data Model](https://iiif.io/api/assets/images/data-model.png)

## Scope
### Use cases
GenIIIF will handle these four straightforward use cases:

1. Manifest with a single image
2. Manifest with a series of images
3. Collection of manifests
4. Collection of collections (top-level collection)

For each use case, [fixtures](fixtures/fixtures.md) and [templates](templates/templates.md) will be generated.

### Methods
#### Simple GUI
The main method to create IIIF-compliant resources is to create a form on a minimalist graphical user interface (GUI) that end users would have to fill out. 

##### IIIF Manifest

Following the wording of [the IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/#52-manifest), the form for use cases 1 and 2, concerning to the generation of IIIF Manifests, is broken into the following parts.

1. Metadata about the IIIF resource (`context`, `id`, `type`)
2. Descriptive Metadata about the object
3. Presentation information (such as `viewing Direction`)
4. Rights Information (`rights`, `requiredStatement`, `logo`)
5. Related links (`homepage`, `seeAlso`, `rendering`, `start`, etc.)
6. List of Canvases (`items`)

##### IIIF Collection
TBD

#### Extraction of structured metadata
A second alternative method which will be later created is to extract the (descriptive, structural and legal) metadata from a CSV or a database.

### Usage of GenIIIF
TBD

#### Dependencies
[Tkinter](https://realpython.com/python-gui-tkinter/)

To install the requirements:

```bash
pip3 install -r requirements.txt
```

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