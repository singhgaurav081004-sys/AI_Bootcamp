
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Text for the word cloud
text = """
Artificial Intelligence Machine Learning Python Programming Coding Technology
Innovation Data Science Algorithms Robotics Automation Deep Learning Neural Networks
Computer Science Software Development Problem Solving Creativity Research Education
Future Digital Transformation Cybersecurity Cloud Computing Applications Projects
Hackathons Skills Learning Programming Java C++ SQL Web Development
"""

# Create the word cloud
wordcloud = WordCloud(
    width=1600,
    height=900,
    background_color="white",
    collocations=False,
    margin=8
).generate(text)

# Display the word cloud
plt.figure(figsize=(16, 9))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

# Save the word cloud in JPG format
plt.savefig(
    "ai_technology_wordcloud.jpg",
    format="jpg",
    dpi=200,
    bbox_inches="tight"
)

# Show the word cloud
plt.show()
