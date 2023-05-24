from manim import *

class transitiona(Scene):
    def construct(self):
        equation1 = MathTex(r"y=f(bx+c)")
        equation2 = MathTex(r"y=af(bx+c)").shift(RIGHT * 4)
        arrow = Arrow(start=LEFT, end=RIGHT)
        
        self.play(Write(equation1))
        self.play(equation1.animate.shift(LEFT * 4), run_time = 3)
        self.play(Write(arrow))
        self.play(Write(equation2))