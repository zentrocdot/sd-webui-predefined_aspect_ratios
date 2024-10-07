# Extension for the AUTOMATIC1111 Web UI

<p align="justify">sd-webui-predefined_aspect_ratios is an <i>Extension</i> for the <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111/stable-diffusion-webui</a>, which is adding buttons to the web UI for the selection of predefined aspect ratios.</p>

## Preface

<p align="justify">The existing solutions [3,4,5] are to complex for my personal needs. This is a version with just buttons of a predefined set of aspect ratios. They cover the most common aspect ratios used.</p>

## Selector Buttons for Predefined Aspect Ratios

<p align="justify">The base resolution is 512 pixel. This is the lowest values, which will be calculated. Minimal value of height or width is 512 pixel.</p>

Following aspect ratios are implemented:

**No specific Orientation**

* 1:1 → 512 x 512 pixel

**Orientation Landscape**

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

* 16:10 → 819 x 512 pixel → (Factor 1,599609375) 

**Orientation Portrait**

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

## What the Extension Does

After installation one will find a button panel within the web UI.

<a target="_blank" href=""><img src="button_panel_new.png" alt="button panel"></a>

## Known Problems

After installation of the Extension it could be that the web UI has to be reloaded from the browser that the Extension can be used.

## To-Do

Nothing to-do yet.

# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://buymeacoffee.com/zentrocdot/stable-diffusion-aspect-ratios

[3] https://github.com/alemelis/sd-webui-ar

[4] https://github.com/altoiddealer/--sd-webui-ar-plusplus

[5] https://github.com/xhoxye/sd-webui-ar_xhox



