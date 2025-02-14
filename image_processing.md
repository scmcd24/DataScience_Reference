# Image Processing

#### Interpolation Methods
- Adaptive vs non-adaptive
- Non-Adaptive Methods (increasing in terms of complexity):
    - Nearest Neighbor:
        - Current point value is the value of the nearest pixel
        - Each pixel gets bigger (?)
        - Applicable to discrete and continuous data (value of the cells is unchanged)
        - Benefit: the output values are guaranteed to be real values in your dataset

    - Bilinear:
        - AKA Rook's case contiguity
        - Considers the closest 2x2 pixels around the current image 
        - Current pixel value is a weighted average of those 4 pixels
        - Continuous data only (spatial autocorrelation?)
        - Peaks/valleys may be underestimated

    - Bicubic interpolation / Cubic convolution / Cubic spline:
        - AKA Queen's case contiguity
        - Considers the closest 4x4 pixels around the current image 
        - Current pixel value is a weighted average of those 16 pixels
        - Closer pixels are given higher weighting
        - Continuous data only
        - Peaks/valleys may be overestimated

- Source: 
    - https://www.cambridgeincolour.com/tutorials/image-interpolation.htm#google_vignette
    - https://desktop.arcgis.com/en/arcmap/latest/extensions/spatial-analyst/performing-analysis/cell-size-and-resampling-in-analysis.htm#:~:text=In%20the%20default%20case%2C%20the,only%20applicable%20to%20continuous%20data.
    - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mdpi.com%2F2076-3417%2F12%2F22%2F11652&psig=AOvVaw1p480cQ0HjzOEj5Suy-j8l&ust=1739652816995000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNjJ6vOFxIsDFQAAAAAdAAAAABAE
    - https://gis.stackexchange.com/questions/267433/pros-and-cons-of-using-bilinear-interpolation-and-cubic-convolution-when-dealing 

- Dump:
    - Bishop's contiguity? hexagon?
    - From wikipedia: Bicubic interpolation can be accomplished using either Lagrange polynomials, cubic splines, or cubic convolution algorithm. (???)
    - diff Bicubic interpolation / Cubic convolution / Cubic spline
    - Rook's better for edge detection/image segmentation, bishops's for texure analysis (textures are diagonal?)