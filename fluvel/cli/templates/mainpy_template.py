MAINPY_TEMPLATE = """from fluvel import FluvelApp

# App
app = FluvelApp()

app.register(
    initial="home",
    views=[
        "views.home"
    ]
)

if __name__ == "__main__":
    app.run()
"""
