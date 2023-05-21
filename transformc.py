from manim import *

class transformc(Scene):
    def construct(self):
        c = ValueTracker(0)
        nplane=NumberPlane(y_range=[-5, 10, 1])
        axis_labels = nplane.get_axis_labels(x_label="x", y_label="y")
        graph = nplane.plot(lambda x : (x+c.get_value())**2, color = YELLOW)
        graph.add_updater(lambda func : func.become(nplane.plot(lambda x : (x+c.get_value())**2,color = YELLOW)))
        equation = MathTex(f"y=f(x+({round(c.get_value(),1)}))").next_to(graph, DOWN)  
        equation.add_updater(lambda e: e.become(MathTex(f"y=f(x+({round(c.get_value(), 1)}))").next_to(graph, DOWN)  ))


        self.play(Create(nplane), Write(axis_labels))
        self.play(Create(graph))
        self.play(Write(equation))
        self.play(c.animate.set_value(5),run_time=5)
        self.play(c.animate.set_value(-5),run_time=10)




