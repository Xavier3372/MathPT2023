from manim import *
import numpy as np

class Graph(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 5, 1], y_range=[0, 21, 1],x_length=10,y_length=5, axis_config = {"include_tip": False, "include_numbers" : False})
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x : x**2, color = YELLOW, x_range=[-4,4])
        equation = MathTex(r"y=x^2")
        equation.next_to(axes, UP * 3)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Write(equation))
        self.play(Create(graph))