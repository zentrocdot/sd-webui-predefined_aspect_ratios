import contextlib
import gradio as gr
import modules.scripts as scripts
from pathlib import Path
from modules.ui_components import ToolButton
from math import gcd

aspect_ratios_dir = scripts.basedir()

switch_values_symbol = "\U000021C5"
get_dimensions_symbol = "\u2B07\ufe0f"
get_image_dimensions_symbol = "\U0001F5BC"

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

    def reset(self, w, h):
        return [self.res, self.res]

def write_js_titles_file(button_titles):
    filename = Path(aspect_ratios_dir, "javascript", "button_titles.js")
    content = [
        "// Do not put custom titles here. This file is overwritten each time the web UI is started.\n"
    ]
    content.append("ar_button_titles = {\n")
    counter = 0
    while counter < len(button_titles[0]):
        content.append(
            f'    "{button_titles[0][counter]}" : "{button_titles[1][counter]}",\n'
        )
        counter = counter + 1
    content.append("}")
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(content)

class AspectRatioScript(scripts.Script):
    def title(self):
        return "Aspect Ratio Selector"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
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
                
                self.aspect_ratios = [
                   "1:1, 1.0 # 1:1 ratio based on minimum dimension\n",
                   "3:2, 3/2 # Set width based on 3:2 ratio to height\n",
                   "4:3, 4/3 # Set width based on 4:3 ratio to height\n",
                   "16:9, 16/9 # Set width based on 16:9 ratio to height",
                ]
                self.aspect_ratio_labels = [
                   "1:1",
                   "3:2",
                   "4:3",
                   "16:9",
                ]
                self.res = ["512,512", "512,768"]
                self.res_labels = ["512,512", "512,768"]
                # Aspect Ratio buttons
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
            # Write button_titles.js with labels and comments read from aspect ratios and resolutions files
            #button_titles = [self.aspect_ratio_labels + self.res_labels]
            #self.aspect_ratio_comments = ["1", "2", "3", "4"]
            #self.res_comments = ["1", "2", "3", "4"]
            #button_titles.append(self.aspect_ratio_comments + self.res_comments)
            #write_js_titles_file(button_titles)
            # dummy components needed for JS function
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
