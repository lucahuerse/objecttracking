import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

pitch = Pitch(pitch_color='grass', line_color='white', stripe=False)
fig, ax = pitch.draw(figsize=(8, 4))

plt.show()

