import random
import os
from PIL import Image, ImageFont, ImageDraw

from helper import dir_walk, generate_color
from .MemeEngineInterface import MemeEngineInterface


class MemeEngine(MemeEngineInterface):

    @staticmethod
    def load_img(path):
        return Image.open(path)

    @staticmethod
    def resize_img(img, width=500):
        w, h = img.size
        ratio = width / w
        return img.resize(width, int(h * ratio), Image.NEAREST)

    @staticmethod
    def assign_font():
        font_dir = './_data/fonts'
        font_path = random.choice(dir_walk(font_dir))
        return ImageFont.truetype(font_path, size=20, encoding='utf-8')

    def synthesis_new_img(self, image, text):
        draw = ImageDraw.Draw(image)
        w, h = image.size

        color = (generate_color())
        font = self.assign_font()

        draw.text(
            (w / 16, h / 8),
            text=text,
            fill=color,
            font=font
        )

        return image

    def save_file(self, image):
        image_output_name = f"meme_{random.randint(0, 100)}.jpg"
        output_path = os.path.join(self.output_dir, image_output_name)
        image.save(output_path)
        print(f'image saved in {output_path}')
        return output_path

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        try:
            self.can_ingest(img_path)
            img = self.load_img(img_path)
            img = self.resize_img(img)
            text = f"{text} - {author}"
            new_img = self.synthesis_new_img(img, text)
            return self.save_file(new_img)
        except Exception as e:
            print(e)
