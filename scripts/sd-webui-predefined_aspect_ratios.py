import contextlib
import gradio as gr
import modules.scripts as scripts
from pathlib import Path
from modules.ui_components import ToolButton
from math import gcd

class ARButton(ToolButton):
    def __init__(self, ar=1.0, **kwargs):
        super().__init__(**kwargs)
        self.ar = ar

    def apply(self, w, h):
        if self.ar > 1.0:  # fix height, change width
            w = self.ar * h
        elif self.ar < 1.0:  # fix width, change height
            h = w / self.ar
        else:  # set minimum dimension to both
            min_dim = min([w, h])
            w, h = min_dim, min_dim
        return list(map(round, [w, h]))

    #def reset(self, w, h):
    #    return [self.res, self.res]

class AspectRatioScript(scripts.Script):
    def title(self):
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        self.aspect_ratios = (1.0, 3/2, 4/3, 16/9)
        self.aspect_ratio_labels = ("1:1", "3:2", "4:3", "16:9")
        with gr.Column(
            elem_id=f'{"img" if is_img2img else "txt"}2img_container_aspect_ratio'
        ):
            with gr.Row(
                elem_id=f'{"img" if is_img2img else "txt"}2img_row_aspect_ratio'
            ):
                gr.HTML(
                    visible=True,
                    elem_id="arc_empty_space",
                )
                # Aspect ratio buttons.
                btns = [
                    ARButton(ar=ar, value=label)
                    for ar, label in zip(
                        self.aspect_ratios,
                        self.aspect_ratio_labels,
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
                            outputs=resolution,
                        )
            # Dummy components needed for JS function
            dummy_text1 = gr.Text(visible=False)
            dummy_text2 = gr.Text(visible=False)
            dummy_text3 = gr.Text(visible=False)
            dummy_text4 = gr.Text(visible=False)
            
    # Function after_component()
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
