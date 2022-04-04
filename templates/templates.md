# Templates
## IIIF Manifest
### Sketch
The main template to generate IIIF Manifests will roughly look like the photo below.

![20220404_083410](https://user-images.githubusercontent.com/17925031/161487513-6788338f-2c43-436d-ae9c-2d8b6cebf275.jpg)

### Form

Following the wording of [the IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/#52-manifest), the form for use cases 1 and 2, concerning to the generation of IIIF Manifests, is broken into the following components (the numbering of the above sketch is not consistent):

1. Metadata about the IIIF resource (`context`, `id`, `type`)
2. Summary (`summary`)
3. Descriptive Metadata about the object
4. Rights Information (`rights`, `requiredStatement`)
5. Related links (`logo`,`homepage`, `seeAlso`, `provider`, `rendering`, `start`)
6. Presentation information (`viewing Direction`, `navDate`, `thumbnail`)
7. List of Canvases (`items` + `id`, `type`, `label` for each resource - see below)

_The `Canvas` represents an individual page or view and acts as a central point for assembling the different content resources that make up the display._

Here is a detailed view of the [first fixture/use case](https://github.com/julsraemy/GenIIIF/blob/main/fixtures/SGV_single_image_manifest.json#L226):

```
    {
      "id": "https://pia-something.ch/iiif/boilerplate01/canvas/p1",
      "type": "Canvas",
      "label": {
    "none": [
      "SGV_12N_00001"
    ]
  },
      "height": 4190,
      "width": 4252,
      "items": [
        {
          "id": "https://pia-iiif.dhlab.unibas.ch/server/SGV_12N_00001/canvas/p1",
          "type": "Canvas",
          "label": {
          "none": [
            "SGV_12N_00001"
          ]
        },
          "height": 4252,
          "width": 4190,
          "items": [
            {
              "id": "https://pia-iiif.dhlab.unibas.ch/server/SGV_12N_00001/canvas/p1/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://pia-iiif.dhlab.unibas.ch/server/SGV_12N_00001/annotation/p0001-image",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://pia-iiif.dhlab.unibas.ch/SGV_12/SGV_12N_00001.jp2/full/max/0/default.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 4252,
                    "width": 4190,
                    "service": [
                      {
                        "id": "https://pia-iiif.dhlab.unibas.ch/SGV_12/SGV_12N_00001.jp2",
                        "type": "ImageService3",
                        "profile": "level2"
                      }
                    ]
                  },
                  "target": "https://pia-iiif.dhlab.unibas.ch/server/SGV_12N_00001/canvas/p1/1"
                }
              ]
            }
          ]
        }
      ]
    }
```

## IIIF Collection
The form for use cases 3 and 4 will have the following components:

1. Metadata about the IIIF resource (`context`, `id`, `type`)
2. Summary (`summary`)
3. Related links (`logo`, `provider`)
4. List of Manifests/Collections (`items` + `id`, `type`, `label` for each resource)
