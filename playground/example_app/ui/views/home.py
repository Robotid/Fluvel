from fluvel import View, route

from fluvel.composer import Prefab, Factory

@Factory.compose("FLabel")
def ColorLabel(color: str, bg_weight: int):

    return {
        "text": "",
        "style": f"bg-{color}-{bg_weight} rounded-md"
    }

@Factory.compose("FLabel")
def Label(text: str):

    return {
        "text": text,
        "style": "text-lg font-light"
    }

@Prefab
def Palette(view: View, color: str):

    with view.Grid() as grid:
            grid.adjust(min_width=125)

            c1, c2, c3 = grid.Columns(3)

            c1.add(Label(color.capitalize()), column_span=3)

            c1.add(ColorLabel(color, 100))
            c1.add(ColorLabel(color, 200))
            c1.add(ColorLabel(color, 300))

            c2.add(ColorLabel(color, 400))
            c2.add(ColorLabel(color, 500))
            c2.add(ColorLabel(color, 600))

            c3.add(ColorLabel(color, 700))
            c3.add(ColorLabel(color, 800))
            c3.add(ColorLabel(color, 900))

            c1.add(ColorLabel(color, 1000), column_span=3)

    return view

@Prefab
def ColorScaleBar(view: View, color: str) -> View:

    with view.Vertical() as v:
        v.adjust(spacing=0, fixed_width=300)

        for i in range(1, 11):
            lbl = v.Label(style=f"bg-{color}-{i*100} m-0")

            match i:
                case 1: lbl.configure(style=f"rounded-t-2xl")
                case 10: lbl.configure(style=f"rounded-b-2xl")

    return view

@route("home")
class Home(View):

    def build_ui(self):

        with self.Horizontal(style="bg-stone-300") as hbody:

            hbody.Prefab(ColorScaleBar(color="violet"))

            with self.Grid(hbody, style="bg-zinc-200 rounded-4xl") as grid:
                grid.adjust(margins=(20, 20, 20, 20))

                c1, c2, c3, c4, c5 = grid.Columns(5)

                c1.add(Palette(color="slate"))
                c1.add(Palette(color="gray"))
                c1.add(Palette(color="zinc"))
                c1.add(Palette(color="neutral"))

                c2.add(Palette(color="stone"))
                c2.add(Palette(color="red"))
                c2.add(Palette(color="orange"))
                c2.add(Palette(color="amber"))

                c3.add(Palette(color="yellow"))
                c3.add(Palette(color="lime"))
                c3.add(Palette(color="green"))
                c3.add(Palette(color="emerald"))

                c4.add(Palette(color="teal"))
                c4.add(Palette(color="cyan"))
                c4.add(Palette(color="blue"))
                c4.add(Palette(color="sky"))

                c5.add(Palette(color="violet"))
                c5.add(Palette(color="purple"))
                c5.add(Palette(color="fuchsia"))
                c5.add(Palette(color="pink"))
