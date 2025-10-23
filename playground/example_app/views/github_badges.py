"""
Example Module: GitHub-Style Badges (Advanced Composition)

This module illustrates Fluvel's potential for modelling visually complex designs
(such as the status badges commonly seen on GitHub) in an
extremely easy, intuitive, and robust manner.

It demonstrates the key principles of Fluvel's architecture:
--------------------------------------------------------------
1.  Composition Pattern (@Prefab): Use of nested components (RowBadges calls Badge)
    to encapsulate layout, iteration, and styling logic. This promotes
    reusability and separation of responsibilities.
2.  Declarative Programming: The final view (github-badges-example) focuses solely on
    the data structure (the BADGES list) and the placement of the final component,
    without worrying about how each individual badge is rendered.
3.  Hybrid Styling System: Demonstrates the powerful combination of predefined classes
    (such as "bg-zinc-200" or "font-bold") with the QSS preprocessor for fine-grained styling
    (e.g., "br-left[5px]", "m-0", "p-1").
"""

from fluvel import View, route
from fluvel.composer import Prefab

@Prefab
def Badge(view: View, title: str, description: str, color: str) -> View:
    """
    Defines the atomic component of a two-part badge.
    
    Abstracts the complexity of margins, zero spacing, and the application of 
    rounded edges only on the outer corners.
    
    :param title: The text for the left section (e.g., 'licence').
    :param description: The text for the right section (e.g., 'MIT').
    :param colour: The base colour for the description section (e.g., 'green', which becomes 'bg-green-400').
    """

    with view.Horizontal() as h:
        h.adjust(spacing=0, margins=(0, 0, 0, 0))

        h.Label(text=title, style="bg-gray-500 m-0 p-1 fg-white br-left[5px]", alignment="right")
        h.Label(text=description, style=f"bg-{color}-400 m-0 p-1 fg-white br-right[5px]", alignment="left")

    return view

@Prefab
def RowOfBadges(view: View, badges: list[tuple[str, str, str]]) -> View:
    """
    Container component that iterates over a list of data to generate and assemble 
    multiple Badges in a row.
    
    :param badges: List of tuples with the structure (title, description, colour).
    """

    with view.Horizontal() as h:
        
        for title, description, color in badges:
            
            # Create and insert each Badge
            h.Prefab(Badge(title=title, description=description, color=color))

    return view

@route("github-badges-example")
class GHubBadges(View):

    def build_ui(self):

        with self.Vertical(style="bg-slate-200") as v:
            v.adjust(alignment="center", spacing=10)

            # Data
            BADGES = [
                ("licence", "MIT", "lime"),
                ("python", "3.10+", "blue"),
                ("pypi", "v1.4.0", "blue"),
                ("codecov", "75%", "orange"),
                ("status", "stable", "lime"),
            ]

            # Example title with advanced text styles
            v.Label(text="Github Badges", style="text-3xl font-bold f-family[consolas]", align="center")

            # High-level component (RowOfBadges), passing data
            v.Prefab(RowOfBadges(badges=BADGES))