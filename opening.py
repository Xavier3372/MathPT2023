from manim import *

class opening(Scene):
    def construct(self):
        axes1 = Axes(x_range=[-4, 5, 1], y_range=[0, 21, 1],x_length=5,y_length=3, axis_config = {"include_tip": False, "include_numbers" : False})
        axis1_labels = axes1.get_axis_labels(x_label="x", y_label="y")
        graph1 = axes1.plot(lambda x : x**2, color = YELLOW, x_range=[-4,4])
        equation1 = MathTex(r"y=f(x)")
        equation1.next_to(axes1, UP * 3)
        graphgroup1 = VGroup(equation1, graph1, axis1_labels, axes1)

        arrow = Arrow(start=LEFT, end=RIGHT)

        axes2 = Axes(x_range=[-4, 5, 1], y_range=[0, 21, 1],x_length=5,y_length=3, axis_config = {"include_tip": False, "include_numbers" : False}).shift(RIGHT * 4)
        axis2_labels = axes2.get_axis_labels(x_label="x", y_label="y")
        graph2 = axes1.plot(lambda x : 2*(x**2)+3, color = YELLOW, x_range=[-3,3]).shift(RIGHT * 4)
        equation2 = MathTex(r"y=af(bx+c)+d")
        equation2.next_to(axes2, UP * 3)

        self.play(Write(equation1))
        self.play(DrawBorderThenFill(axes1), Write(axis1_labels))
        self.play(Create(graph1))
        self.play(graphgroup1.animate.shift(LEFT*4), run_time = 3)
        self.play(Write(arrow))
        self.play(Write(equation2))
        self.play(DrawBorderThenFill(axes2), Write(axis2_labels))
        self.play(Create(graph2))