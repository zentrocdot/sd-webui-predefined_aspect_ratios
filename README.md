# Extension for the AUTOMATIC1111 Web UI
#### :arrow_right: sd-webui-predefined_aspect_ratios

<p align="justify">sd-webui-predefined_aspect_ratios is an <i>Extension</i> for the <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111/stable-diffusion-webui</a>, which is adding buttons to the web UI for the selection of predefined <i>aspect ratios</i>.</p>

---

## Preface

<p align="justify">The existing solutions [3,4,5] were much to complex for my personal needs. I have therefore decided to use this case to programme an <i>Extension</i> for learning purposes. The result of my first efforts can be found here. The presented version does nothing else, than adding a panel with predefined aspect ratios to the web UI. The predefined <i>aspect ratios</i> cover the most common ones in use.</p>

<p align="justify">At times I was of the opinion that this <i>Extension</i> is not quite as helpful as I thought. I have since changed my mind and use it very often. My opinion was influenced by the <i>AUTOMATIC1111</i> contributors, who consider my extension to be too trivial and not helpful.</p>

## User Case

<p align="justify">The <i>Extension</i> was developed for use with <i>SD 1.5</i>. The assumptions subsequently presented are basses on my experiences with <i>AUTOMATIC1111</i> and <i>SD 1.5</i>. As technology is constantly advancing, there is no guarantee that these assumptions will hold in the long term.</p>

## Assumptions

<p align="justify">There are one rule when creating AI images, which is crucial. An Ai generated immage should be as small as possible. But, the resolution for the image to be created should not be smaller than 512 pixel in one of the both possible directions. For the <i>Extension</i> one resolution is all the time 512 pixel. The quotient of the divison from the chosen <i>aspect ratio</i> may be a floating point number. Height or witdth my be rounded values.</p>

## Selector Buttons for Predefined Aspect Ratios

<p align="justify">Following <i>aspect ratios</i> are implemented:</p>

**No specific (square) Orientation**

* 1:1 → 512 x 512 pixel

**Orientation Landscape**

* 2:1 → 1024 x 512 pixel → (Factor 2)
  
* 3:1 → 1536 x 512 pixel → (Factor 3)
  
* 4:1 → 2048 x 512 pixel → (Factor 4)

* 3:2 → 768 x 512 pixel → (Factor 1.5)

* 4:3 → 683 x 512 pixel → (Factor 1,333984375)

* 5:3 → 853 x 512 pixel → (Factor 1,666015625) 

* 5:4 → 640 x 512 pixel → (Factor 1.25) 

* 6:5 → 614 x 512 pixel → (Factor 1,19921875) 

* 7:5 → 717 x 512 pixel → (Factor 1,400390625)

* 8:3 → 1365 x 512 pixel → (Factor 2,666666667)

* 14:9 → 796 x 512 pixel → (Factor 1,5546875) 

* 15:9 → 853 x 512 pixel → (Factor 1,666015625) 

* 16:9 → 910 x 512 pixel → (Factor 1,77734375)

**Orientation Portrait**

* 1:2 → 512 x 1024 pixel → (Factor 0.5)

* 1:3 → 512 x 1536 pixel → (Factor 0,333333333)

* 1:4 → 512 x 2048 pixel → (Factor 0,25)

* 2:3 → 512 x 768 pixel → (Factor 0,666666667)

* 3:4 → 512 x 683 pixel → (Factor 0,749633968)

* 3:5 → 512 x 853 pixel → (Factor 0,600234467)

* 3:8 → 512 x 1365 pixel → (Factor 0,375)

* 4:5 → 512 x 640 pixel → (Factor 0.8) 

* 5:6 → 512 x 614 pixel → (Factor 0,833876221) 

* 5:7 → 512 x 717 pixel → (Factor 0,714086471) 

* 9:14 → 512 x 796 pixel → (Factor 0,64321608)

* 9:15 → 512 x 853 pixel → (Factor 0,600234467)

* 9:16 → 512 x 910 pixel → (Factor 0,562637363)

## Exception to the rule

<p align="justify">The aspect ratios</p>

+ 8:3
+ 3:8

<p align="justify">are not one of common aspect ratios. I added this both aspect ratio due to the fact, that a banner at OpenSea needs a aspect ratio of 8:3.</p>

## What the Extension Does

<p align="justify">After installation one will find a button panel within the web UI which looks like the next one.</p>

<a target="_blank" href=""><img src="./images/button_panel_new.png" alt="button panel"></a>

<i>Figure 1: Exemplary appearance of the opened extension panel</i>

## Installation

<p align="justify">Go to tab <b>Extensions</b>. Then go to tab <b>Install from URL</b>. Put in the ínstallation link in the text field <b>URL for extension's git repository</b>. Finally press button <b>Install</b>. Successful installation is displayed in the footer.</p>

The installation link, which can be used in <i>AUTOMATIC1111</i> is as follows:

```
https://github.com/zentrocdot/sd-webui-predefined_aspect_ratios
```

Click on the overlapping squares on the right side of the last code block to copy the installation link.

## Known Problems

<p align="justify">After installation of the Extension it could be that the web UI has to be reloaded from the browser that the Extension can be used. I haven't noticed this problem recently</p>

## Related Tools

<p align="justify">I wrote some tools for dealing with aspect ratios. These tool can be found at 
<a href="https://github.com/zentrocdot/artificial-intelligence-tools/tree/main/misc">Aspect Ratio Tools</a>.</p>

## To-Do

<p align="justify">The code of the <i>Extension</i> needs to be sanitized and optimised. The reason is simple, as I have used existing concepts and approaches.</p>

<p align="justify">Since I am using my own extension more and more, a revision of the documentation is necessary.</p>

## Collection of Other Aspect Ratios

* 1.19:1 = 19:16
* 1.25:1 = 5:4
* 1.3:1
* 1.33:1 = 4:3 = 12:9
* 1.37:1 = 48:35
* 1.41:1
* 1.5:1 = 3:2
* 1.59:1
* 1.60:1 = 16:10 = 8:5
* 1.66:1 = 15:9 = 5:3
* 1.75:1 = 7:4
* 1.77:1 = 16:9
* 1.78:1
* 1.85:1
* 2.35:1
* 2.37:1
* 2.38:1
* 2.39:1
* 2.40:1
* 2.59:1 to 2.65:1
* 2.35:1 to 2.66:1
* 2.75:1 
* 2.76:1
* 3.2:1
* 3.55:1 = 32:9
* 3.58:1
* 3.6:1 = 18:5
* 12:5
* 18:5
* 18:9
* 19.5:9
* 20:9
* 21:9
* 22:9
* 32:9
* 36:10
* 256:135

<p align="justify">The previous list does not claim to be complete. The list from Extension sd-webui-aspect_ratios-dd is more complete.</p>

# Credits

<p align="justify">By studying some existing Extensions, I was very quickly able to understand how to write this Extension. My thanks go to the following:</p>

+ alemelis [3]
+ altoiddealer [4]
+ xhoxye [5]
  
# References

[1] https://github.com/AUTOMATIC1111/stable-diffusion-webui

[2] https://buymeacoffee.com/zentrocdot/stable-diffusion-aspect-ratios

[3] https://github.com/alemelis/sd-webui-ar

[4] https://github.com/altoiddealer/--sd-webui-ar-plusplus

[5] https://github.com/xhoxye/sd-webui-ar_xhox

[6] https://github.com/zentrocdot/artificial-intelligence-tools/tree/main/misc
