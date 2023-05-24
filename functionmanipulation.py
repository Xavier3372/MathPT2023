from manim import *

class functionmanipulation(Scene):
    def construct(self):
        equation1 = MathTex("2", "y","-","1"," ="," 4", "f((3-x)/2)")
        equation2 = MathTex("2","y"," ="," 4", "f((3-x)/2)","+","1")
        equation3 = MathTex("y"," ="," 2", "f((3-x)/2)","+","1/","2")
        equation4 = MathTex("y"," ="," 2", "f((-x+3)/2)","+","1/","2")
        
        self.play(Write(equation1))
        self.play(TransformMatchingTex(equation1, equation2))
        Wait(3)
        self.play(TransformMatchingTex(equation2, equation3))
        Wait(3)
        self.play(TransformMatchingTex(equation3, equation4))
       