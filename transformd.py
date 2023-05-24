from manim import *

class transformd(Scene):
    def construct(self):
        d = ValueTracker(0)
        nplane=NumberPlane(y_range=[-5, 10, 1])
        axis_labels = nplane.get_axis_labels(x_label="x", y_label="y")
        graph = nplane.plot(lambda x : (x**2)+d.get_value(), color = YELLOW)
        graph.add_updater(lambda func : func.become(nplane.plot(lambda x : (x**2)+d.get_value(),color = YELLOW)))
        equation = MathTex(f"y=f(x)+{round(d.get_value(),1)}").move_to([0,-3.5,0], aligned_edge=DOWN)
        equation.add_updater(lambda e: e.become(MathTex(f"y=f(x)+{round(d.get_value(),1)}").move_to([0,-3.5,0], aligned_edge=DOWN)))


        self.play(Create(nplane), Write(axis_labels))
        self.play(Create(graph))
        self.play(Write(equation))
        self.play(d.animate.set_value(5),run_time=5)
        self.play(d.animate.set_value(-5),run_time=10)