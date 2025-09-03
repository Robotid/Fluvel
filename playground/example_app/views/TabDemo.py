from fluvel.core import ViewBuilder

from PySide6.QtWidgets import QTabWidget, QWidget


class TabDemo(ViewBuilder):

    def view(self) -> None:

        with self.Vertical(self.parent) as v:

            self.tab = QTabWidget(self.parent)
            self.tab.setTabsClosable(True)
            self.tab.tabCloseRequested.connect(self.close_tab)

            tab_1_widget = QWidget()

            self.tab.addTab(tab_1_widget, "Tab 1")

            with self.Horizontal(v) as h:
                h.adjust(alignment=h.RIGHT)

                # Button
                btn = h.Button(
                    text="Add", on_click=self.agregar_tab, style="dark w-500"
                )

            v.addWidget(self.tab)

        with self.Horizontal(tab_1_widget) as h:
            h.adjust(alignment=h.CENTER)
            h.Button(text="Ventana 1")

    def agregar_tab(self) -> None:

        index = self.tab.addTab(QWidget(), "New Tab")

        self.tab.setCurrentIndex(index)

    def close_tab(self, index: int) -> None:

        self.tab.removeTab(index)
