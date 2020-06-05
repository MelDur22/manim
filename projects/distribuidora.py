from big_ol_pile_of_manim_imports import *

class Surface(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
            "u_min": 0,
            "v_min": 0,
            "u_max": 4,
            "v_max": 4.5,
        }

        ParametricSurface.__init__(self, self.function, **kwargs)
    
    def function(self, a, b):
        """Max tipo A = 40, {:10} = 4 = a
        Max tipo B = 45, {:10} = 4.5 = b
        a*3 + b*4 <= 180, {:10} = a*3 + b*4 <= 18         | 40 * 3 + 45 * 4 <= 180, {:10} 4 * 3 + 4.5 * 4 <= 18
        a*3 + b*2 <= 120, {:10} = a*3 + b*2 <= 12         | 40 * 3 + 45 * 2 <= 120, {:10} 4 * 3 + 4.5 * 2 <= 12

        c = a*6000 + b*5000, {:1000} = c = a*0.6 + b*0.5 | 40 * 6000 + 45 * 5000, {:1000} & {:10} 4 * 0.6 + 4.5 * 0.5
        -------------------------------------------------------------------------------------------------------------
        Ratio a & b = 1:10
        Ratio c = 1:1000 * ratio_a * ratio_b = 1:100000
        """
        restriccion_light = ((a * 3 + b * 4) // 18.1 + 3) % 2 #Si se cumple la restriccion, devuelve 1, si no, devuelve 0
        restriccion_normal = ((a * 3 + b * 2) // 12.1 + 3) % 2 #Si se cumple la restriccion, devuelve 1, si no, devuelve 0
        c = (a * 0.6 + b * 0.5) * restriccion_light * restriccion_normal
        return np.array([a, b, c])

class main(ThreeDScene):
    """
    Problema de la distribuidora
    En una distribuidora de bebidas se dispone de 180 bebidas Coca Light y 120 de bebidas Normales
    Los refrescos se venden en paquetes de dos tipos: A y B
    Los paquetes de tipo A contienen 3 bebidas Coca Light y 3 bebidas Normales. Los paquetes tipo B contienen 4 bebidas Coca Light y 2 bebidas Normales.
    El vendedor gana 6000 pesos por cada paquete que venda de tipo A y 5000 pesos por cada uno que vende de tipo B.
    El vendedor desea obtener la mayor utilidad
    -------------------------------------------------------------------------------------------
    Maximo de paquetes tipo A = 40
    Maximo de paquetes tipo B = 45
    -------------------------------------------------------------------------------------------
    """
    def construct(self):
        kwargs = {
            "x_min": 0,
            "y_min": 0,
            "z_min": 0,
            "x_max": 4,
            "y_max": 4.5,
            "z_max": 3.5,
        }
        video_title = TextMobject("Tenemos el siguiente problema")
        video_title.scale(2)
        problem_title = TextMobject("Problema de la distribuidora:")
        problem_title.to_corner(UL)

        self.play(Write(video_title))
        self.wait(3)
        self.play(ReplacementTransform(video_title, problem_title))

        problem = TextMobject("""
            En una distribuidora de bebidas se dispone de\\\\
            \\textbf{180} bebidas \\textbf{Cola Light} y de \\textbf{120} bebidas \\textbf{Normales}.\\\\
            Los refrescos se venden en paquetes de dos tipos: A y B.\\\\
            Los paquetes de tipo \\textbf{A} contienen \\textbf{3} bebidas Cola Light y\\\\
            \\textbf{3} bebidas Normales. Los paquetes de tipo \\textbf{B} contienen\\\\
            \\textbf{4} bebidas Cola Light y \\textbf{2} bebidas Normales.\\\\
            El vendedor gana \\textbf{6000} pesos por cada paquete que venda de\\\\
            tipo \\textbf{A} y \\textbf{5000} pesos por cada uno que vende de tipo \\textbf{B}.\\\\
            El vendedor desea obtener la mayor utilidad.
            """)
        self.play(Write(problem))
        self.wait(20)
        self.play(FadeOutAndShiftDown(problem),FadeOut(problem_title))

        solution_title = TextMobject("Entonces, cómo podemos resolver este problema?")
        solution_title.scale(1.3)
        self.play(Write(solution_title))
        self.wait(3)

        title = TextMobject("Apliquemos el modelo matemático")
        title.scale(1.3)

        self.play(ReplacementTransform(solution_title, title))
        self.wait(3)


        #Variables# 12 - 22
        var_title = TextMobject("\\underline{Variables}")
        var_subtitle = var_title.copy()
        var_title.scale(1.25)
        self.play(ReplacementTransform(title, var_title))
        self.wait(3)

        var_subtitle.to_corner(UL)
        self.play(ReplacementTransform(var_title, var_subtitle))
        self.wait(2)

        type_a = TextMobject("Paquetes de tipo A")
        a = TextMobject("$a$")
        a.next_to(var_subtitle, DOWN)
        type_a.scale(1.25)
        self.play(Write(type_a))
        self.wait()
        self.play(ReplacementTransform(type_a, a))
        self.wait()

        type_b = TextMobject("Paquetes de tipo B")
        b = TextMobject("$b$")
        b.next_to(a, DOWN)
        type_b.scale(1.25)
        self.play(Write(type_b))
        self.wait()
        self.play(ReplacementTransform(type_b, b))
        self.wait(3)


        #Restricciones# 23-42
        restrictions_title = TextMobject("\\underline{Restricciones}")
        restrictions_subtitle = restrictions_title.copy()
        restrictions_title.scale(1.25)
        self.play(Write(restrictions_title))
        self.wait(3)

        restrictions_subtitle.to_edge(UP)
        self.play(ReplacementTransform(restrictions_title, restrictions_subtitle))
        self.wait(2)

        light_text = TextMobject("Solo tenemos \\textbf{180} bebidas de tipo light")
        light_algebra = TexMobject(
            "a",
            "\\times 3 +",
            "b",
            "\\times 4",
            "\\le 180"
        )
        light_algebra.next_to(restrictions_title, DOWN)
        self.play(Write(light_text))
        self.wait()

        self.play(ReplacementTransform(light_text, light_algebra[4]))
        self.wait()
        self.play(
            ReplacementTransform(a.copy(), light_algebra[0]),
            ReplacementTransform(b.copy(), light_algebra[2]),
            run_time = 3
        )
        self.wait()
        self.play(
            Write(light_algebra[1]),
            Write(light_algebra[3]),
            run_time = 3
        )
        self.wait()

        normal_text = TextMobject("Solo tenemos \\textbf{120} bebidas de tipo normal")
        normal_algebra = TexMobject(
            "a",
            "\\times 3 +",
            "b",
            "\\times 2",
            "\\le 120"
        )
        normal_algebra.next_to(light_algebra, DOWN)
        self.play(Write(normal_text))
        self.wait()

        self.play(ReplacementTransform(normal_text, normal_algebra[4]))
        self.wait()
        self.play(
            ReplacementTransform(a.copy(), normal_algebra[0]),
            ReplacementTransform(b.copy(), normal_algebra[2]),
            run_time = 2
        )
        self.wait()
        self.play(
            Write(normal_algebra[1]),
            Write(normal_algebra[3]),
            run_time = 2
        )
        self.wait()
        
        natural_nums_text = TextMobject("Las cantidades de paquetes no pueden ser decimales o negativas")
        natural_nums_algebra = TexMobject("a, b\\in \\mathbb{N}")
        natural_nums_algebra.next_to(normal_algebra, DOWN)
        self.play(Write(natural_nums_text))
        self.wait(2)
        self.play(ReplacementTransform(natural_nums_text, natural_nums_algebra))
        self.wait(3)

        #Función objetivo# 43 - 50
        objective_title = TextMobject("\\myul{1.2pt}{0.5pt}{1pt}{Función Objetivo}")
        objective_subtitle = objective_title.copy()
        objective_title.scale(1.25)
        self.play(Write(objective_title))
        self.wait(3)

        objective_subtitle.to_corner(UR)
        self.play(ReplacementTransform(objective_title, objective_subtitle))
        self.wait(2)

        objective_text = TextMobject("Como el problema plantea, queremos la mayor utilidad")
        objective_text2 = TextMobject("MAXIMIZAR")
        objective_text2.next_to(objective_subtitle, DOWN)
        self.play(Write(objective_text))
        self.wait(2)
        self.play(ReplacementTransform(objective_text, objective_text2))
        self.wait(2)

        #Graficacion#
        graph_intro = TextMobject("Con esto en mente, hagamos un gráfico")
        graph_intro.scale(1.25)
        self.play(Write(graph_intro))
        self.wait()

        pre_intro = VGroup(var_subtitle, a, b, restrictions_subtitle, light_algebra, normal_algebra, natural_nums_algebra, objective_subtitle, objective_text2)
        self.play(ShrinkToMobject(pre_intro, graph_intro))
        self.wait(3)

        graph_axes_text = TextMobject("Primero, tenemos los ejes")
        graph_axes_text.to_corner(UL)
        self.play(ReplacementTransform(graph_intro, graph_axes_text))
        ###GRAFICO###
        self.set_camera_orientation(phi=60 * DEGREES, theta=-135 * DEGREES)
        self.add_fixed_in_frame_mobjects(graph_axes_text)

        axes = ThreeDAxes(**kwargs)
        self.play(ShowCreation(axes))
        self.wait(2)


        graph_axes_text_x = TextMobject("En el eje $x$ ubicaremos\\\\ la cantidad de paquetes tipo A")
        graph_axes_text_x.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(graph_axes_text_x)
        self.play(Write(graph_axes_text_x))
        self.wait()
        self.move_camera(phi = 90 * DEGREES, theta = -90 * DEGREES)
        self.wait()

        label_0 = TexMobject("0")
        x_label = TexMobject("a")
        x_label1 = TexMobject("10")
        x_label2 = TexMobject("20")
        x_label3 = TexMobject("30")
        x_label4 = TexMobject("40")
        x_labels = VGroup(x_label, x_label1, x_label2, x_label3, x_label4, label_0)

        x_label.move_to(np.array([4.5, -0.5, 0]))
        x_label1.move_to(np.array([1, -0.5, 0]))
        x_label2.move_to(np.array([2, -0.5, 0]))
        x_label3.move_to(np.array([3, -0.5, 0]))
        x_label4.move_to(np.array([4, -0.5, 0]))
        label_0.move_to(np.array([0, -0.5, 0]))
        x_labels.set_color(RED)
        label_0.set_color(WHITE)
        x_labels.rotate(90 * DEGREES, axis = X_AXIS)
        self.play(
            Write(x_label),
            Write(label_0)
        )
        x_labels.rotate(-90 * DEGREES, axis = X_AXIS)
        self.add_fixed_orientation_mobjects(x_label, x_label1, x_label2, x_label3, x_label4, label_0)
        self.add(x_label1, x_label2, x_label3, x_label4)
        self.wait()
        self.play(FadeOut(graph_axes_text_x))
        self.move_camera(phi = 60 * DEGREES, theta = -135 * DEGREES)
        self.wait()

        
        graph_axes_text_y = TextMobject("En el eje $y$ ubicaremos\\\\ la cantidad de paquetes tipo B")
        graph_axes_text_y.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(graph_axes_text_y)
        self.play(Write(graph_axes_text_y))
        self.wait()
        self.move_camera(phi = 90 * DEGREES, theta = -180 * DEGREES)
        self.wait()

        y_label = TexMobject("b")
        y_label1 = TexMobject("10")
        y_label2 = TexMobject("20")
        y_label3 = TexMobject("30")
        y_label4 = TexMobject("40")
        y_label5 = TexMobject("45")
        y_labels = VGroup(y_label, y_label1, y_label2, y_label3, y_label4, y_label5)

        y_label.move_to(np.array([-0.5, 5, 0]))
        y_label1.move_to(np.array([-0.5, 1, 0]))
        y_label2.move_to(np.array([-0.5, 2, 0]))
        y_label3.move_to(np.array([-0.5, 3, 0]))
        y_label4.move_to(np.array([-0.5, 4, 0]))
        y_label5.move_to(np.array([-0.5, 4.5, 0]))
        y_labels.set_color(BLUE)
        y_labels.rotate(-90 * DEGREES, axis = Y_AXIS)
        y_labels.rotate(90 * DEGREES, axis = X_AXIS)
        self.play(
            Write(y_label)
        )
        self.add_fixed_orientation_mobjects(y_label, y_label1, y_label2, y_label3, y_label4, y_label5)
        y_labels.rotate(90 * DEGREES, axis = Y_AXIS)
        y_labels.rotate(90 * DEGREES, axis = Z_AXIS)
        self.add(y_label1, y_label2, y_label3, y_label4, y_label5)
        self.wait()
        self.play(FadeOut(graph_axes_text_y))
        self.move_camera(phi = 60 * DEGREES, theta = -135 * DEGREES)
        self.wait()


        graph_axes_text_z = TextMobject("En el eje $z$ ubicaremos\\\\ la utilidad o ganancia\\\\ y lo representaremos con una $u$")
        graph_axes_text_z.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(graph_axes_text_z)
        self.play(Write(graph_axes_text_z))
        self.wait()
        self.move_camera(phi = 90 * DEGREES, theta = -90 * DEGREES)
        self.wait()

        z_label = TexMobject("u")
        z_label1 = TexMobject("\$100.000")
        z_label2 = TexMobject("\$200.000")
        z_label3 = TexMobject("\$300.000")
        z_labels = VGroup(z_label, z_label1, z_label2, z_label3)

        z_label.move_to(np.array([-0.5, -0.5, 3.5]))
        z_label1.move_to(np.array([-0.5, -0.5, 1]))
        z_label2.move_to(np.array([-0.5, -0.5, 2]))
        z_label3.move_to(np.array([-0.5, -0.5, 3]))
        z_labels.set_color(GREEN)
        z_labels.rotate(90 * DEGREES, axis = X_AXIS)
        self.play(
            Write(z_label)
        )
        z_labels.rotate(-90 * DEGREES, axis = X_AXIS)
        self.add_fixed_orientation_mobjects(z_label, z_label1, z_label2, z_label3)
        self.add(z_label1, z_label2, z_label3)
        self.wait()
        self.play(FadeOut(graph_axes_text_z))
        self.move_camera(phi = 60 * DEGREES, theta = -135 * DEGREES)
        self.wait(3)

        graph_text = TextMobject("Ahora, veamos el gráfico")
        graph_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(graph_text)
        self.play(
            Write(graph_text),
            FadeOut(graph_axes_text)
        )
        self.wait()

        surface = Surface()
        self.play(
            ShowCreation(surface),
            FadeOut(graph_text),
            play_time = 5
        )
        self.wait(2)
        self.move_camera(phi = 90 * DEGREES, theta = 45 * DEGREES)
        #ThreeDCamera.set_frame_center(self.camera, np.array([0, 2.75, 0]))
        self.wait(2)

        graph_expl = TextMobject("Como podemos observar, este es el punto más alto")
        high_ground = Dot(np.array([2.14, 2.81, 2.65]), color = YELLOW)
        graph_expl.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(graph_expl)
        self.add_fixed_orientation_mobjects(high_ground)

        self.play(
            ShowCreation(high_ground),
            Write(graph_expl)
        )
        self.wait(2)

        dot_expl = TextMobject(
            "Esto lo interpretamos como:\\\\",
            "21 paquetes de tipo A \\\\",
            "28 paquetes de tipo B \\\\",
            "\$266.000 de utilidad"
        )
        dot_expl.next_to(graph_expl, UP)
        self.add_fixed_in_frame_mobjects(dot_expl[0])
        self.play(
            Write(dot_expl[0]),
            FadeOutAndShiftDown(graph_expl)
        )
        self.wait()
        self.move_camera(phi = 90 * DEGREES, theta = -90 * DEGREES)
        x_dot = high_ground.copy()
        x_dot.move_to(np.array([2.14, 0, 0]))
        self.add_fixed_orientation_mobjects(x_dot)
        self.add_fixed_in_frame_mobjects(dot_expl[1])
        self.play(
            ShowCreation(x_dot),
            Write(dot_expl[1])
        )
        self.wait()
        self.play(FadeOut(x_dot))

        self.move_camera(phi = 90 * DEGREES, theta = -180 * DEGREES)
        y_dot = high_ground.copy()
        y_dot.move_to(np.array([0, 2.81, 0]))
        self.add_fixed_orientation_mobjects(y_dot)
        self.add_fixed_in_frame_mobjects(dot_expl[2])
        self.play(
            ShowCreation(y_dot),
            Write(dot_expl[2])
        )
        self.wait()
        self.play(FadeOut(y_dot))
        
        self.move_camera(phi = 90 * DEGREES, theta = -90 * DEGREES)
        z_dot = high_ground.copy()
        z_dot.move_to(np.array([0, 0, 2.65]))
        self.add_fixed_orientation_mobjects(z_dot)
        self.add_fixed_in_frame_mobjects(dot_expl[3])
        self.play(
            ShowCreation(z_dot),
            Write(dot_expl[3])
        )
        self.wait()
        self.play(FadeOut(z_dot))
        
        self.move_camera(phi = 60 * DEGREES, theta = -135 * DEGREES)
        self.wait(5)

        #Outro
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.set_camera_orientation(phi = 0  * DEGREES, theta = -90 * DEGREES)
        self.wait(2)

        outro_1 = TextMobject("Gracias por ver este vídeo")
        outro_2 = TextMobject("Esta animación fue creada con Manim\\\\")
        outro_3 = TextMobject("Manim es un software de codigo abierto desarrollado por\\\\ 3blue1brown")
        github_logo = SVGMobject("github")
        github_text = TextMobject("El código de esta animación lo puedes encontrar en\\\\","github.com/MelDur22/manim")
        outro_1.scale(1.5)
        outro_3[48:52].set_color("#73C0E3")
        outro_3[53:58].set_color("#8C6138")
        self.play(Write(outro_1))
        self.wait(5)
        self.play(
            ReplacementTransform(outro_1, outro_2)
        )
        self.wait(3)
        self.play(
            ReplacementTransform(outro_2, outro_3)
        )
        self.wait(5)
        self.play(
            DrawBorderThenFill(github_logo),
            FadeOutAndShiftDown(outro_3)
        )
        self.wait()
        self.play(
            Transform(github_logo, github_logo.copy().to_edge(buff=0.75))
        )
        self.wait()

        github_text.scale(0.9)
        github_text.next_to(github_logo, RIGHT, buff = 0.5)

        self.play(Write(github_text))
        self.wait(5)
