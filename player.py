from pathlib import Path
from typing import List
import arcade


def get_animation_frames(filename: Path) -> List[arcade.Texture]:
    # open the image at the given filename
    frames = arcade.load_textures(
        file_name=filename,
        image_location_list=[
            [0, 0, 16, 32],
            [16, 0, 16, 32],
            [32, 0, 16, 32],
            [48, 0, 16, 32],
        ],
    )
    return frames


class Player:
    def __init__(self):
        self.sprite = arcade.Sprite(filename="./resources/player/running.png", scale=1)
        self.animation_counter = 0
        self.running_frames = get_animation_frames(
            filename="./resources/player/running.png"
        )
        self.idle_frames = [self.running_frames[0]]

        self.animation_mapping = {
            "idle": {"frames": self.idle_frames, "rate": 0.2},
            "running": {"frames": self.running_frames, "rate": 0.05},
        }
        self.set_animation(animation_name="running")

    def set_animation(self, animation_name: str):
        self.current_animation = animation_name
        self.current_animation_frames = self.animation_mapping[animation_name]["frames"]
        self.current_animation_rate = self.animation_mapping[animation_name]["rate"]
        self.sprite.textures = self.current_animation_frames
        self.animation_counter = 0
        self.animation_index = 0

        # set the texture to the first frame
        self.sprite.set_texture(
            self.animation_index % len(self.current_animation_frames)
        )

    def update_animation(self, delta_time: float):
        self.animation_counter += delta_time
        if self.animation_counter > self.current_animation_rate:
            self.animation_counter = 0
            self.animation_index += 1
            self.sprite.set_texture(
                self.animation_index % len(self.current_animation_frames)
            )
            self.sprite.update()

    def on_update(self, delta_time: float):
        self.update_animation(delta_time=delta_time)


if __name__ == "__main__":
    frames = get_animation_frames(filename="./resources/player/running.png")
    breakpoint()
