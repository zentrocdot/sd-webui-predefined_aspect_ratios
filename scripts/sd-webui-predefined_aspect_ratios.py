#!/usr/bin/python3
'''sd-webui-predefined_aspect_ratios
Extension for AUTOMATIC1111
Version 0.0.0.8

The linter pylint was used to check the programme code.
'''
# pylint: disable=import-error
# pylint: disable=consider-using-from-import
# pylint: disable=attribute-defined-outside-init
# pylint: disable=too-few-public-methods
# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-argument

# Import the Python modules.
import contextlib
import gradio as gr
import modules.scripts as scripts
from modules.ui_components import ToolButton
from modules.ui_components import InputAccordion

# Define module variables.
_width = 512
_height = 512

# Define private values and labels for landscape orientation.
#_ar_values_0 = (2/1, 3/1, 3/2, 4/1, 4/3, 5/3, 5/4,
#                6/5, 7/5, 8/3, 12/5, 14/9, 16/9)
_ar_labels_0 = ("2:1", "3:1", "3:2", "4:1", "4:3", "5:3", "5:4",
                "6:5", "7:5", "8:3", "12:5", "14:9", "16:9")

_ar_values_0 = ()
for ele in _ar_labels_0:
    try:      
        print(ele)
        templist = ele.split(":")
        print(templist)
        fval = float(templist[0]) / float(templist[1])       
        _ar_values_0 = _ar_values_0 + (fval, )
    except:
        print("*** Could not parse: " + str(ele))  

# Define private values and labels for portrait orientation.
_ar_values_1 = (0.5, 1/3, 1/4, 2/3, 3/4, 3/5, 3/8, 4/5,
                5/6, 5/7, 5/12, 9/14, 9/16)
_ar_labels_1 = ("1:2", "1:3", "1:4", "2:3", "3:4", "3:5", "3:8", "4:5",
                "5:6", "5:7", "5:12", "9:14", "9:16")

# Define class AspectRatioButton.
class AspectRatioButton(ToolButton):
    '''Class for calculating the new Width and new Height for
       use in the web UI from the chosen Aspect Ratio.
    '''
    def __init__(self, ar=1.0, **kwargs):
        '''Class method __init__.'''
        super().__init__(**kwargs)
        self.ar = ar

    def apply(self, wx, hy):
        '''Class method apply.

           Arguments wx, hy are not in use yet.
           wx and hy are the values, which are
           currently selected in the web UI.
        '''
        # Initialise width and height using the private variables.
        w = _width
        h = _height
        # Calculate new width and height.
        if self.ar > 1.0:  # fixed height, change width
            w = self.ar * h
        elif self.ar < 1.0:  # fixed width, change height
            h = w / self.ar
        else:  # set minimum dimension to both variables
            min_dim = min([w, h])
            w, h = min_dim, min_dim
        # Round the values of w and h and create a list.
        retlst = list(map(round, [w, h]))
        # Return the list with the width and the height.
        return retlst

# Define class AspectRatioScript.
class AspectRatioScript(scripts.Script):
    '''Class for selecting the aspect ratio.'''

    def title(self):
        '''Class method title.'''
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        '''Class method show.'''
        return scripts.AlwaysVisible

    def image_resolution(self, is_img2img):
        '''Get the image resolution.'''
        if is_img2img:
            imgres = [self.i2i_w, self.i2i_h]
        else:
            imgres = [self.t2i_w, self.t2i_h]
        return imgres

    def ui(self, is_img2img):
        '''Class method ui.'''
        # Set the format strings.
        css0 = f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
        css1 = elem_id=f'{"img" if is_img2img else "txt"}2img_container_aspect_ratio'
        # Create a column.
        with gr.Column(elem_id=css1):
            # Create an InputAccordion.
            with InputAccordion(open=True, label='Predefined Aspect Ratios', visible=True, value=False):
                # Create first row.
                with gr.Row(elem_id=css0):
                    # Aspect ratio button line 0.
                    btns = [AspectRatioButton(ar=1.0, value="1:1")]
                    with contextlib.suppress(AttributeError):
                        for b in btns:
                            imgres = self.image_resolution(is_img2img)
                            b.click(b.apply, inputs=imgres, outputs=imgres)
                # Create second row.
                with gr.Row(elem_id=css0):
                    # Aspect ratio buttons line 1.
                    btns = [
                        AspectRatioButton(ar=ar, value=label)
                        for ar, label in zip(
                            _ar_values_0,
                            _ar_labels_0
                        )
                    ]
                    with contextlib.suppress(AttributeError):
                        for b in btns:
                            imgres = self.image_resolution(is_img2img)
                            b.click(b.apply, inputs=imgres, outputs=imgres)
                # Create third row.
                with gr.Row(elem_id=css0):
                    # Aspect ratio buttons line 2.
                    btns = [
                        AspectRatioButton(ar=ar, value=label)
                        for ar, label in zip(
                            _ar_values_1,
                            _ar_labels_1
                        )
                    ]
                    with contextlib.suppress(AttributeError):
                        for b in btns:
                            imgres = self.image_resolution(is_img2img)
                            b.click(b.apply, inputs=imgres, outputs=imgres)
    
    # Class method after_component.
    def after_component(self, component, **kwargs):
        '''Class method after_component.

           The if entries are sorted by web UI feature.
        '''
        if kwargs.get("elem_id") == "txt2img_width":
            self.t2i_w = component
        if kwargs.get("elem_id") == "txt2img_height":
            self.t2i_h = component
        if kwargs.get("elem_id") == "img2img_width":
            self.i2i_w = component
        if kwargs.get("elem_id") == "img2img_height":
            self.i2i_h = component
        if kwargs.get("elem_id") == "img2img_image":
            self.image = [component]
        if kwargs.get("elem_id") == "img2img_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img2maskimg":
            self.image.append(component)
        if kwargs.get("elem_id") == "inpaint_sketch":
            self.image.append(component)
        if kwargs.get("elem_id") == "img_inpaint_base":
            self.image.append(component)
