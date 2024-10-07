# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=attribute-defined-outside-init
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error
# pylint: disable=consider-using-from-import

import contextlib
import gradio as gr
import modules.scripts as scripts
from modules.ui_components import ToolButton

class ARButton(ToolButton):
    '''Class for calculating the new Width and new Height for
       use in the web UI from the chosen aspect ratio.
    '''   
    def __init__(self, ar=1.0, **kwargs):
        '''Class init method.'''
        super().__init__(**kwargs)
        self.ar = ar

    def apply(self, w, h):
        '''Class method apply.'''
        # Initialise height and width.
        w = 512
        h = 512
        # Calculate new width and height.
        if self.ar > 1.0:  # fixed height, change width
            w = self.ar * h
        elif self.ar < 1.0:  # fixed width, change height
            h = w / self.ar
        else:  # set minimum dimension to both
            min_dim = min([w, h])
            w, h = min_dim, min_dim
        # Create a new list.    
        retlst = list(map(round, [w, h]))
        # Return the calculated values for width and heigt.    
        #return list(map(round, [w, h]))
        return retlst

    def reset(self, w, h):
        '''Class method reset.'''
        return [self.res, self.res]

class AspectRatioScript(scripts.Script):
    def title(self):
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        self.aspect_ratios = (1.0, 2.0, 3/2, 4/3, 5/3, 5/4, 6/5, 7/5, 14/9, 15/9, 16/9, 16/10, 
                                   0.5, 2/3, 3/4, 3/5, 4/5, 5/6, 5/7, 9/14, 9/15, 9/16, 10/16)
        self.aspect_ratio_labels = ("1:1", "2:1", "3:2", "4:3", "5:3", "5:4", "6:5", "7:5", "14:9", "15:9", "16:9", "16:10",
                                           "1:2", "2:3", "3:4", "3:5", "4:5", "5:6", "5:7", "9:14", "9:15", "9:16", "10:16")
        with gr.Column(
            elem_id=f'{"img" if is_img2img else "txt"}2img_container_aspect_ratio'
        ):
            with gr.Row(
                elem_id=f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
            ):
                # Aspect ratio buttons.
                btns = [
                    ARButton(ar=ar, value=label)
                    for ar, label in zip(
                        self.aspect_ratios,
                        self.aspect_ratio_labels
                    )
                ]
                with contextlib.suppress(AttributeError):
                    for b in btns:
                        if is_img2img:
                            resolution = [self.i2i_w, self.i2i_h]
                        else:
                            resolution = [self.t2i_w, self.t2i_h]
                        b.click(
                            b.apply,
                            inputs=resolution,
                            outputs=resolution
                        )
                        with gr.Row(
                elem_id=f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
            ):
                # Aspect ratio buttons.
                btns = [
                    ARButton(ar=ar, value=label)
                    for ar, label in zip(
                        self.aspect_ratios,
                        self.aspect_ratio_labels
                    )
                ]
                with contextlib.suppress(AttributeError):
                    for b in btns:
                        if is_img2img:
                            resolution = [self.i2i_w, self.i2i_h]
                        else:
                            resolution = [self.t2i_w, self.t2i_h]
                        b.click(
                            b.apply,
                            inputs=resolution,
                            outputs=resolution
                        )
            
    # User defined function after_component()
    def after_component(self, component, **kwargs):
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
