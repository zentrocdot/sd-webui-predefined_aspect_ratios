# Extension for the AUTOMATIC1111 Web UI

Extension for the [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which is adding buttons for the selection of predefined aspect ratios from within the web UI.

## Preface

The existing solutions [3,4,5] are to complex for my personal needs. This is a version with just buttons of a predefined set of aspect ratios. They cover the most common aspect ratios used.

## Selector Buttons for Predefined Aspect Ratios

Following aspect ratios are implemented:

No specific Orientation

* 1:1 → 512 x 512 pixel

Orientation Landscape

* 2:1 → 1024 x 512 pixel → (Factor 2) 

* 3:2 → 768 x 512 pixel → (Factor 1.5)

* 4:3 → 683 x 512 pixel → (Factor 1.33)

* 5:3 → 853 x 512 pixel → (Factor 1.67) 

* 5:4 → 640 x 512 pixel → (Factor 1.25) 

* 6:5 → 614 x 512 pixel → (Factor 1.2) 

* 7:5 → 717 x 512 pixel → (Factor 1.4) 

* 14:9 → 796 x 512 pixel → (Factor 1.56) 

* 15:9 → 853 x 512 pixel → (Factor 1.66) 

* 16:9 → 910 x 512 pixel → (Factor 1.78)

* 16:10 → 819 x 640 pixel → (Factor 1.6) 

### Orientation Portrait

* 1:2 → 512 x 1024 pixel → (Factor 0.5) 

* 2:3 → 512 x 768 pixel → (Factor 0,666666667)

* 3:4 → 512 x 683 pixel → (Factor 0,749633968)

* 3:5 → 512 x 853 pixel → (Factor 0,600234467) 

* 4:5 → 512 x 640 pixel → (Factor 0.8) 

* 5:6 → 512 x 614 pixel → (Factor 0.833333333) 

* 5:7 → 512 x 717 pixel → (Factor 0,714086471) 

* 9:14 → 512 x 796 pixel → (Factor 0.642857143)

* 9:15 → 512 x 910 pixel → (Factor 0.6)

* 9:16 → 512 x 819 pixel → (Factor 0.5625)

* 10:16 → 512 x 1024 pixel → (Factor 0.625)

# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://buymeacoffee.com/zentrocdot/stable-diffusion-aspect-ratios

[3] https://github.com/alemelis/sd-webui-ar

[4] https://github.com/altoiddealer/--sd-webui-ar-plusplus

[5] https://github.com/xhoxye/sd-webui-ar_xhox



